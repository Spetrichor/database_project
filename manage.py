#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import pymysql



def main():
    """Run administrative tasks."""
    conn = pymysql.connect(host='localhost', user='root',
                           password='6369', port=3306, db='project_new_1')
    cursor = conn.cursor()
    cursor.execute("create table if not exists staff\
        (\
         id bigint not null primary key,\
         age varchar(255) null,\
         name varchar(255) null,\
         password varchar(255) null,\
         section varchar(255) null,\
         type varchar(255) null,\
         username varchar(255) null,\
         gender varchar(255) null,\
         constraint unique_user\
         unique (username)\
        )DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists patient\
        (\
         id bigint not null primary key,\
         age int not null,\
         gender varchar(255) null,\
         level varchar(255) null,\
         name varchar(255) null,\
         section varchar(255) null,\
         status int not null,\
         ward_name varchar(255) null,\
         ward_nurse varchar(255) null)DEFAULT CHARSET=utf8;\
        ")
    cursor.execute("create table if not exists section(id bigint not null primary key,\
         chief_nurse varchar(255) null,\
         doctor varchar(255) null,\
         level varchar(255) null)DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists section_ward_nurses\
        (\
         section_id bigint not null,\
         ward_nurses varchar(255) null,\
         constraint list_ward_nurses\
         foreign key (section_id) references section (id)\
        )DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists section_wards\
        (\
         section_id bigint not null,\
         wards varchar(255) null,\
         constraint list_wards\
         foreign key (section_id) references section (id)\
        )DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists ward\
        (\
         id bigint not null primary key,\
         capacity int not null,\
         level varchar(255) null,\
         name varchar(255) null,\
         constraint unique_ward_name\
         unique (name)\
        )DEFAULT CHARSET=utf8;\
        ")
    cursor.execute("create table if not exists ward_patients\
        (\
         ward_id bigint not null,\
         patients varchar(255) null,\
         constraint list_patients\
         foreign key (ward_id) references ward (id)\
        )DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists ward_sickbeds\
        (\
         ward_id bigint not null,\
         sickbeds int null,\
         constraint list_sickbeds\
         foreign key (ward_id) references ward (id)\
        )DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists report\
        (\
         id bigint not null primary key,\
         date varchar(255) null,\
         doctor varchar(255) null,\
         level varchar(255) null,\
         patient_id bigint null,\
         patient_name varchar(255) null,\
         positive bit not null\
        )DEFAULT CHARSET=utf8;\
        ")
    cursor.execute("create table if not exists daily_info\
        (\
         id bigint not null primary key,\
         date varchar(255) null,\
         patient_id bigint null,\
         patient_name varchar(255) null,\
         positive bit not null, \
         symptom varchar(255) null,\
         temperature double not null,\
         ward_nurse varchar(255) null\
        )DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists message\
        (\
         id bigint not null primary key,\
         message_type int not null,\
         patient_id bigint null,\
         patient_name varchar(255) null,\
         staff varchar(255) null\
        )DEFAULT CHARSET=utf8;")
    cursor.execute("create table if not exists patient_information\
            (\
             patient_id bigint not null,\
             dates date not null,\
            patient_name varchar(255) null,\
    temperature varchar(255) null,\
                positive varchar(255) null,\
       foreign key (patient_id) references patient(id)\
               )DEFAULT CHARSET=utf8;")
    conn.commit()
    cursor.close()
    conn.close()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_1.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
