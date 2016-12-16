import sqlite3
from queries import *

# connection
DB_NAME = 'hospital2.db'
db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

c.execute(DROP_USER_TABLE)
c.execute(DROP_PATIENT_TABLE)
c.execute(DROP_DOCTOR_TABLE)
c.execute(DROP_HOSPITAL_STAY_TABLE)
c.execute(DROP_VISITATION_TABLE)

c.execute(CREATE_USER_TABLE)
c.execute(CREATE_DOCTOR_TABLE)
c.execute(CREATE_PATIENT_TABLE)
c.execute(CREATE_HOSPITAL_STAY_TABLE)
c.execute(CREATE_VISITATION_TABLE)

# create a user


def create_user(username, password, age, is_active):
    c.execute(CREATE_NEW_USER,
              (username, password, age, is_active))
    db.commit()



def promote_to_doctor(baseuser):
    pass


def promote_to_patient(baseuser, doctor=None):
    pass


create_user('dr. pesho', 'az_sym_pesho', 55, 0)
