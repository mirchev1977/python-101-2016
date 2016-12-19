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


def get_all_patient_ids():
    patients = c.execute(GET_ALL_PATIENTS)
    lst_patient_ids = []
    for x in patients:
        lst_patient_ids.append(x['id'])

    return lst_patient_ids


def hospitalize_patients():
    lst_patient_ids = get_all_patient_ids()
    illnesses = ['sclerosis', 'diabetes', 'arm fracture',          'cold', 'flu', 'insomnia']
    rooms = ['101', '102', '205', '208', '313', '458']
    startDate = ['2016-05-14', '2016-06-17', '2016-07-25', '2016-08-03', '2016-09-19', '2016-10-24', '2016-11-13', ]
    endDate = ['2016-05-14', '2016-06-17', '2016-07-25', '2016-08-03', '2016-09-19', '2016-10-24', '2016-11-13', ]

    currentId = choice(lst_patient_ids)
    print(currentId)


create_user('dr. pesho', 'az_sym_dr_pesho', 55, 0)
create_user('pesho', 'az_sym_pesho', 22, 0)
create_user('dr. kirkor', 'az_sym_dr_kirkor', 28, 0)
create_user('gosho', 'az_sym_gosho', 48, 0)
hospitalize_patients()
