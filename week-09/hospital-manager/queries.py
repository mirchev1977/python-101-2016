DROP_USER_TABLE = '''
    DROP TABLE IF EXISTS USER
'''

DROP_PATIENT_TABLE = '''
    DROP TABLE IF EXISTS PATIENT
'''

DROP_DOCTOR_TABLE = '''
    DROP TABLE IF EXISTS DOCTOR
'''

DROP_HOSPITAL_STAY_TABLE = '''
    DROP TABLE IF EXISTS HOSPITAL_STAY
'''

DROP_VISITATION_TABLE = '''
    DROP TABLE IF EXISTS VISITATION
'''


CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS User (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        IS_ACTIVE INTEGER NOT NULL DEFAULT 0,
        AGE INTEGER
    )
'''

CREATE_DOCTOR_TABLE = '''
    CREATE TABLE IF NOT EXISTS DOCTOR (
        ID INTEGER PRIMARY KEY,
        ACADEMIC_TITLE TEXT,
        FOREIGN KEY (ID) REFERENCES USER(ID)
    )
'''

CREATE_PATIENT_TABLE = '''
    CREATE TABLE IF NOT EXISTS PATIENT (
        ID INTEGER PRIMARY KEY,
        DOCTOR_ID INTEGER,
        FOREIGN KEY (ID) REFERENCES USER(ID),
        FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(ID)
    )
'''

CREATE_HOSPITAL_STAY_TABLE = '''
    CREATE TABLE IF NOT EXISTS HOSPITAL_STAY (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        STARTDATE TEXT NOT NULL,
        ENDDATE TEXT,
        ROOM INTEGER NOT NULL,
        INJURY TEXT NOT NULL,
        PATIENT_ID INTEGER,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(ID)
    )
'''

CREATE_VISITATION_TABLE = '''
    CREATE TABLE IF NOT EXISTS HOSPITAL_STAY (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PATIENT_ID INTEGER,
        DOCTOR_ID INTEGER NOT NULL,
        START_HOUR TEXT NOT NULL,
        FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(ID),
        FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(ID)
    )
'''