import pymysql
import datetime


# 后端交互
# 登录系统进行账号与密码验证
def find_name_password(username, password):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        # 这里面存在使用mysql加密和解密的过程，密码可以得到保护，后端是无法直接获取密码的
        sql = "select username,AES_DECRYPT(password,'coco') as password,type from staff where username = \'{username}\' \
        and password = AES_ENCRTPT((\'{password}\'),'coco');".format(
            username=username,
            password=password)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


# 注册新用户
def add_user(username, password, type):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "insert into staff(username, password, type) value " \
              "(\'{name_value}\', \'{password_value}\', \'{type_value}\');".format(name_value=username,
                                                                                   password_value=password,
                                                                                   type_value=type)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


# 为前端防止username重复，设置username函数
def find_user(username):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "select * from staff where username = \'{name_value}\';".format(name_value=username)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None


# 展示个人信息
def show_information(username):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "select name,age,gender,type,section from staff where username=\'{username}\'".format(
            username=username)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


# 修改个人信息
def modify_information(username, age, gender, section):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "update staff set age=\'{age}\' and gender=\'{gender}\' and section=\'{section}\' " \
              "where username=\'{username}\'".format(
            age=age,
            gender=gender,
            section=section,
            username=username)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


# 获取本人管理的病人信息
def my_patient(username, type):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        if type == 'doctor':
            sql = "select patient.* from patient natural join staff on section where staff.username=\'{username}\'".format(
                username=username)
            cursor.execute(sql)
            result = cursor.fetchall()
        elif type == 'chief_nurse':
            sql = "select patient.* from patient natural join staff on section where staff.username=\'{username}\'".format(
                username=username)
            cursor.execute(sql)
            result = cursor.fetchall()
        elif type == 'ward_nurse':
            sql = "select patient.* from patient natural join staff on section where patient.ward_nurse=\'{username}\'".format(
                username=username)
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    except Exception as e:
        return None


# 查看病人的历史信息
def patient_history(name):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "select * from patient_information where name=\'{name}\'".format(name=name)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


# 医生修改病人信息
def doctor_modify_my_patient(id, level, status):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "update patient level=\'{level}\' and status=\'{status}\' where id=\'{id}\'".format(level=level,
                                                                                                  status=status,
                                                                                                  id=id)
        cursor.execute(sql)
        db.commit()
        sql = "update ward_beds sickbeds=sickbeds+1 where ward_id in (select ward_id from patient where id={id} and status='出院')".format(
            id=id)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


# 护士长修改病人信息
def chiefnuerse_modify_my_patient(id, section, ward_id, ward_name):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "update ward_beds sickbeds=sickbeds+1 where ward_id in (select ward_id from patient where id={id})".format(
            id=id)
        cursor.execute(sql)
        db.commit()
        sql = "update ward_beds sickbeds=sickbeds-1 where ward_id={ward_id}".format(ward_id=ward_id)
        cursor.execute(sql)
        db.commit()
        sql = "update patient section=\'{section}\' and ward_id={ward_id} and ward_name=\'{ward_name}\' where " \
              "id=\'{id}\'".format(
            section=section,
            ward_id=ward_id,
            ward_name=ward_name,
            id=id)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


# 护士无法修改病人信息


# 获取本区域的护士信息
def section_nurses(username):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "select name,gender,type from staff where section in (select section from staff where username=\'{" \
              "username}\') "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


def find_patient(name):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "select * from patient where name=\'{name}\'".format(name=name)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


# 急诊护士新增病人
def new_patient(id, name, age, gender, level, section, ward_name, ward_nurse):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "insert into patient(id,name,age,gender,level,section,ward_name,ward_nurse) values({id},\'{name}\'," \
              "\'{age}\',\'{gender}\',\'{level}\',\'{section}\',\'{ward_name}\',\'{ward_nurse}\')".format(
            id=id,
            name=name,
            age=age,
            gender=gender,
            level=level,
            section=section,
            ward_name=ward_name,
            ward_nurse=ward_nurse
        )
        cursor.execute(sql)
        db.commit()
        sql = "update ward_beds sickbeds=sickbeds-1 where ward_id=\'{ward_id}\'".format(ward_id=ward_id)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


# 医生添加核酸报告
def new_report(id, name, date, positive):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "insert into paitent_information(id,name,date,positive) values({id},\'{name}\',\'{date}\',\'{positive}\')".format(
            id=id,
            name=name,
            date=date,
            positive=positive
        )
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


# 护士添加每日测温
def new_temperature(id, name, date, temperature):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='6369', port=3306, db='project_new_1')
        cursor = db.cursor()
        sql = "update patient_information temperature=\'{temperature}\' where id={id} and date=\'{date}\'".format(
            temperature=temperature,
            id=id,
            date=date
        )
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False
