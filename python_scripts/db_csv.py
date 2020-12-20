### This script is used to download files from your database to a csv file. 
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Input key generated on firebase into the credentials.Certificate
cred = credentials.Certificate('../testkey.json') # **TODO** input filepath to your secret key into the certificate
firebase_admin.initialize_app(cred)

db = firestore.client()

# Helper function for reading subject data from database
def subjcsvread(subjects, csvFileName, db, collection):
    subjectList = []
    for subj in subjects:

        try:
            docs = db.collection(collection).where(u'id', u'==', subj).stream()
            for doc in docs:
                fields = doc.to_dict()
                info = (fields.get('id'), 
                        fields.get('age'), 
                        fields.get('comments'), 
                        fields.get('currTrial'), 
                        fields.get('handedness'), 
                        fields.get('ethnicity'), 
                        fields.get('mousetype'), 
                        fields.get('race'), 
                        fields.get('returner'), 
                        fields.get('sex'), 
                        fields.get('tgt_file'))
                subjectList.append(info)
        except:
            print(subj + "doesn't exist!")
            continue

    return subjectList


def getSubjectData(subjects, csvFileName, db, collection):
    subjectList = subjcsvread(subjects, csvFileName, db, collection)

    #Set up file to write to
    file = open(csvFileName, 'w')
    writer = csv.writer(file)
    header = ('Subject ID', 'Age', 'Comments', 'Completed Trials', 'Handedness', 'Ethnicity', 'Mouse Type', 'Race', 'Returner', 'Sex', 'Target File')
    writer.writerow(header)
    writer.writerows(subjectList)
    file.close()

def addSubjectData(subjects, csvFileName, db, collection):
    subjectList = subjcsvread(subjects, csvFileName, db, collection)

    #Set up file to write to
    file = open(csvFileName, 'a')
    writer = csv.writer(file)
    writer.writerows(subjectList)
    file.close()
 
# Helper function for reading trial data from database
def trialcsvread(collection, numTrials, csvFileName, subjects, db):   
    
    #Setup chonky array with every trial inside
    trials = []
    
    for trialID in subjects:
        try:
            # You can replace 'id' with any valid field in the database documents, and change the values in "subjects" accordingly
            docs = db.collection(collection).where(u'id', u'==', trialID).stream()
            for doc in docs:
                fields = doc.to_dict()
                exp_ID = fields.get('experimentID')
                name = fields.get('id')
                group = fields.get('group_type')
                currDate_arr = fields.get('currentDate')
                trialnum_arr = fields.get('trialNum')
                tgtAng_arr = fields.get('target_angle')
                trialType_arr = fields.get('trial_type')
                rot_arr = fields.get('rotation')
                handang_arr = fields.get('hand_fb_angle')
                rt_arr = fields.get('rt')
                mt_arr = fields.get('mt')
                search_arr = fields.get('search_time')
                reachfb_arr = fields.get('reach_feedback')
                for i in range(len(currDate_arr)):
                    trial = (exp_ID, name, currDate_arr[i], trialnum_arr[i], tgtAng_arr[i], trialType_arr[i], rot_arr[i], 
                    handang_arr[i], rt_arr[i], mt_arr[i], search_arr[i], reachfb_arr[i], group)
                    trials.append(trial)

                trials.append(trial)
        except:
            print(trialID + "wasn't completed!")
            continue
    
    return trials
    
    
def getTrialData(collection, numTrials, csvFileName, subjects, db):
   
    trials = trialcsvread(collection, numTrials, csvFileName, subjects, db)
    
    #Set up file to write to
    file = open(csvFileName, 'w')
    writer = csv.writer(file)
    header = ('Experiment Name', 'Subject ID', 'Start Time', 'Trial Number', 'Target Angle', 'Cursor FB', 'Rotation', 'Hand Angle', 'RT', 'MT', 'Search Time', 'Reach FB', 'Group')
    writer.writerow(header)
    writer.writerows(trials)
    file.close()

def addTrialData(collection, numTrials, csvFileName, subjects, db):
    
    trials = trialcsvread(collection, numTrials, csvFileName, subjects, db)
    
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
subjects = ['asdf'] # **TODO** Fill in subjects list with an appropriate field saved in the database

### Select one of the following methods:
### "get" indicates you are starting a new csv, "add" indicates you are adding to an existing csv
### Subject data is the information subjects provide about themselves and trialData is trials

getSubjectData(subjects, 'your_csv_name.csv', db, 'Subjects')
#addSubjectData(subjects, 'your_csv_name.csv', db, 'Subjects')
getTrialData('Trials', 20, 'your_csv_name2.csv', subjects, db)
#addTrialData('Trials', 294, 'you_csv_name.csv', subjects, db)

