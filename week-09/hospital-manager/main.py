import sqlite3
from random import choice
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


def promote_to_doctor(baseuser):
    academic_titles = ['general practicioner',
                       'surgeon', 'anaestologist']
    title = choice(academic_titles)

    c.execute(PROMOTE_USER_TO_DOCTOR, (baseuser, title))
    db.commit()


def promote_to_patient(baseuser, doctor=None):
    c.execute(PROMOTE_USER_TO_PATIENT, (baseuser))
    db.commit()


def decide_if_doctor(userId):
    patient = c.execute(GET_USER_BY_ID, (userId,))
    current = [x for x in patient]
    middle = current[0]['USERNAME']
    name = middle.split(' ')

    if name[0] == 'dr.':
        promote_to_doctor(str(current[0]['ID']))
        return

    promote_to_patient(str(current[0]['ID']))
    return


def create_user(username, password, age, is_active):
    c.execute(CREATE_NEW_USER,
              (username, password, age, is_active))
    db.commit()
    lastId = c.lastrowid
    decide_if_doctor(lastId)


create_user('dr. pesho', 'az_sym_dr_pesho', 55, 0)
create_user('pesho', 'az_sym_pesho', 22, 0)
