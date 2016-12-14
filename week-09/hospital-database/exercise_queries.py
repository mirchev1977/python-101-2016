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
print()
print()
print()

# list all doctors
list_doctors = """ SELECT * FROM DOCTORS """
doctors = c.execute(list_doctors)
for doctor in doctors:
    current_doctor = ''
    current_doctor += doctor['FIRSTNAME']
    current_doctor += ' '
    current_doctor += doctor['LASTNAME']
    print(current_doctor)
print()
print()
print()

# add a new patient
insert_patient = """
INSERT INTO PATIENTS (FIRSTNAME, LASTNAME, AGE, GENDER)
VALUES (?, ?, ?, ?)
 """
# c.execute(insert_patient, ('Kirkor', 'Kirkorov', '99', 'M'))
# db.commit()

# add a new doctor
insert_doctor = """
    INSERT INTO doctors (FIRSTNAME, LASTNAME)
    VALUES (?, ?)
"""
c.execute(insert_doctor, ('Palamud', 'Palamudurjan'))
# db.commit()

# add hospital stay of a patient
hospitalize_a_patient = """
INSERT INTO hospital_stay (ROOM, STARTDATE, ENDDATE, INJURY, PATIENT)
VALUES (?, ?, ?, ?, ?)
"""
c.execute(hospitalize_a_patient, ('8', '2016-12-20',
          '2016-12-30', 'sclerosis', '8'))
# db.commit()

# update a patient's information
update_patient = """
UPDATE PATIENTS SET FIRSTNAME = 'Dyrdorko',
LASTNAME = 'DYRDORKOV', AGE = '109', GENDER = 'M',
DOCTOR = '3' WHERE ID = '10'
"""
c.execute(update_patient)
# db.commit()

# update doctor's information
update_doctor = """
UPDATE doctors SET FIRSTNAME = 'Gugutko',
LASTNAME = 'Gugutkov' WHERE ID IN (5, 6)
"""
c.execute(update_doctor)
# db.commit()

# update some hospital information
update_hospital_info = """
    UPDATE hospital_stay
    SET ROOM = 9,
    STARTDATE = '2016-10-25',
    ENDDATE = '2016-12-30', INJURY='lack of concentration',
    PATIENT = 7 WHERE ID = 10
"""
c.execute(update_hospital_info)
# db.commit()

# delete a patient
delete_patient = """
DELETE FROM patients WHERE ID = 9
"""
c.execute(delete_patient)
# db.commit()

# delete a doctor
delete_doctor = """
DELETE FROM doctors WHERE ID IN (6, 8, 9)
"""
c.execute(delete_doctor)
# db.commit()

# delete hospital stay
delete_hospital_stay = """
DELETE FROM hospital_stay
WHERE ID IN (11, 12, 13, 14)
"""
c.execute(delete_hospital_stay)
# db.commit()

# list all patients of a doctor
list_all_patients_per_doctor = """
    SELECT doc.FIRSTNAME || ' ' || doc.LASTNAME as DOCNAME,
    GROUP_CONCAT(pat.FIRSTNAME || ' ' || pat.LASTNAME, ', ')
    as PATIENT_NAME
    FROM doctors as doc
    JOIN patients pat
    ON doc.ID = pat.DOCTOR
    GROUP BY doc.ID
"""
result = c.execute(list_all_patients_per_doctor)

for doc in result:
    print(doc['DOCNAME'])
    print('    ' + str(doc['PATIENT_NAME']))

print()
print()
print()

# all sick patients group by their's sickness(injury)
group_patients_by_illness = """
    SELECT hos.INJURY,
    GROUP_CONCAT(pat.FIRSTNAME || ' ' || pat.LASTNAME, ', ')
    AS PATIENTS
     FROM patients as pat
    JOIN hospital_stay as hos
    ON pat.ID = hos.PATIENT
    GROUP BY hos.INJURY
"""
result = c.execute(group_patients_by_illness)
for illness in result:
    print(illness['INJURY'])
    print('    ' + str(illness['PATIENTS']))

# close db
db.close()
