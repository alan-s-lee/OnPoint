### This script is used to download files from your database to a csv file. 
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Input key generated on firebase into the credentials.Certificate
cred = credentials.Certificate('your-secret-key.json') # **TODO** input your secret key into the certificate
firebase_admin.initialize_app(cred)

db = firestore.client()

# This function is a quick check to see if the mechanisms work (obsolete)
def minitest():
    sub = 'SubjectInfo'
    
    #Edit duck to be a valid id of a document on the database
    duck = 'bobthebuilder'

    docs = db.collection(sub).where(u'id', u'==', duck).stream()

    for doc in docs:
        fields = doc.to_dict()
        print(fields.get("age"))

def getSubjectData(subjects, csvFileName, db, collection):
    subjectList = []
    for subj in subjects:

        try:
            # You can replace 'currTrial' with any valid field in the database documents, and change the values in "subjects" accordingly
            docs = db.collection(collection).where(u'currTrial', u'==', subj).stream()
            for doc in docs:
                fields = doc.to_dict()
                info = (fields.get('id'), fields.get('age'), fields.get('clampQ'), fields.get('comments'), fields.get('currTrial'), fields.get('handedness'), fields.get('ethnicity'), fields.get('mousetype'), fields.get('race'), fields.get('returner'), fields.get('sex'), fields.get('tgt_file'))
                subjectList.append(info)
        except:
            print(subj + "doesn't exist!")
            continue

    #Set up file to write to
    file = open(csvFileName, 'w')
    writer = csv.writer(file)
    header = ('Subject ID', 'Age', 'Clamp Question', 'Comments', 'Completed Trials', 'Handedness', 'Ethnicity', 'Mouse Type', 'Race', 'Returner', 'Sex', 'Target File')
    writer.writerow(header)
    writer.writerows(subjectList)
    file.close()

def addSubjectData(subjects, csvFileName, db, collection):
    subjectList = []
    for subj in subjects:

        try:
            # You can replace 'currTrial' with any valid field in the database documents, and change the values in "subjects" accordingly
            docs = db.collection(collection).where(u'currTrial', u'==', subj).stream()
            for doc in docs:
                fields = doc.to_dict()
                info = (fields.get('id'), fields.get('age'), fields.get('clampQ'), fields.get('comments'), fields.get('currTrial'), fields.get('handedness'), fields.get('ethnicity'), fields.get('mousetype'), fields.get('race'), fields.get('returner'), fields.get('sex'), fields.get('tgt_file'))
                subjectList.append(info)
        except:
            print(subj + "doesn't exist!")
            continue

    #Set up file to write to
    file = open(csvFileName, 'a')
    writer = csv.writer(file)
    writer.writerows(subjectList)
    file.close()

def getTrialData(collection, numTrials, csvFileName, subjects, db):
    #Create array with complete set of id's in database
    #Comment out this portion if you are not using 'id' as your field
    ids = []
    for subj in subjects:
        for i in range(1, numTrials + 1):
            ids.append(subj + str(i))
    #Setup chonky array with every trial inside
    trials = []
    #Change "ids" to "subjects" if not using 'id' as your indicated field below
    for trialID in ids:
        try:
            # You can replace 'id' with any valid field in the database documents, and change the values in "subjects" accordingly
            docs = db.collection(collection).where(u'id', u'==', trialID).stream()
            for doc in docs:
                fields = doc.to_dict()
                trial = (fields.get('experimentID'), fields.get('name'), fields.get('currentDate'), fields.get('trialNum'), fields.get('target_angle'), fields.get('trial_type'), fields.get('rotation'), fields.get('hand_fb_angle'), fields.get('rt'), fields.get('mt'), fields.get('search_time'), fields.get('reach_feedback'), fields.get('group_type'))
                trials.append(trial)
        except:
            print(trialID + "wasn't completed!")
            continue

    #Set up file to write to
    file = open(csvFileName, 'w')
    writer = csv.writer(file)
    header = ('Experiment Name', 'Subject ID', 'Start Time', 'Trial Number', 'Target Angle', 'Cursor FB', 'Rotation', 'Hand Angle', 'RT', 'MT', 'Search Time', 'Reach FB', 'Group')
    writer.writerow(header)
    writer.writerows(trials)
    file.close()

def addTrialData(collection, numTrials, csvFileName, subjects, db):
    #Create array with complete set of id's in database
    #Comment out this portion if you are not using 'id' as your field
    ids = []
    for subj in subjects:
        for i in range(1, numTrials + 1):
            ids.append(subj + str(i))
    #Setup chonky array with every trial inside
    trials = []
    #Change "ids" to "subjects" if not using 'id' as your indicated field below
    for trialID in ids:
        try:
            # You can replace 'id' with any valid field in the database documents, and change the values in "subjects" accordingly
            docs = db.collection(collection).where(u'id', u'==', trialID).stream()
            for doc in docs:
                fields = doc.to_dict()
                trial = (fields.get('experimentID'), fields.get('name'), fields.get('currentDate'), fields.get('trialNum'), fields.get('target_angle'), fields.get('trial_type'), fields.get('rotation'), fields.get('hand_fb_angle'), fields.get('rt'), fields.get('mt'), fields.get('search_time'), fields.get('reach_feedback'), fields.get('group_type'))
                trials.append(trial)
        except:
            print(trialID + "wasn't completed!")
            continue

    #Set up file to write to
    file = open(csvFileName, 'a')
    writer = csv.writer(file)
    emptyrow = []
    #writer.writerow(emptyrow)
    writer.writerows(trials)
    file.close()

### Update subjects to be the proper parameter you select to choose from firebase
### IMPORTANT NOTE: Depending on what field you choose to access the database, you may have to edit the functions slightly.
### Refer to comments in the functions themselves to make changes
subjects = [] # **TODO** Fill in subjects list with an appropriate field saved in the database

### Select one of the following methods:
### "get" indicates you are starting a new csv, "add" indicates you are adding to an existing csv
### Subject data is the information subjects provide about themselves and trialData is trials

#getSubjectData(subjects, 'your_csv_name.csv', db, 'Subjects')
#addSubjectData(subjects, 'your_csv_name.csv', db, 'Subjects')
#getTrialData('Trials', 270, 'your_csv_name.csv', subjects, db)
#addTrialData('Trials', 294, 'you_csv_name.csv', subjects, db)
#minitest()
