import sqlite3

# connection
DB_NAME = 'hospital.db'
db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

# list all patients
list_patients = """ SELECT * FROM PATIENTS """
patients = c.execute(list_patients)
for patient in patients:
    current_patient = ''
    current_patient += patient['FIRSTNAME'] + ' ' + \
        patient['LASTNAME'] + ' ' + str(patient['AGE']) +\
        ' ' + patient['GENDER']
    print(current_patient)


# close db
db.close()
