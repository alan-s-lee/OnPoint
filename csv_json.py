import csv, json

def jsonFromCsv(csvFilePath, jsonFilePath):
    # JSON objects
    jsonData = {}
    trialNums = {}
    aimingLandmarks = {}
    onlineFB = {}
    endpointFB = {}
    rotation = {}
    clampedFB = {}
    tgtDistance = {}
    anglesDict = {}
    betweenBlocks = {}
    targetJump = {}
    
    
    file = open(csvFilePath, 'r')
    reader = csv.reader(file)
    headings = next(reader) # Ensures we don't read the headings again
    rowCount = 0
    for row in reader:
        trialNums[rowCount] = int(row[0])
        aimingLandmarks[rowCount] = int(row[1])
        anglesDict[rowCount] = int(row[2])
        rotation[rowCount] = float(row[3])
        onlineFB[rowCount] = int(row[4])
        endpointFB[rowCount] = int(row[5])
        clampedFB[rowCount] = float(row[6])
        tgtDistance[rowCount] = int(row[7])
        betweenBlocks[rowCount] = float(row[8])
        targetJump[rowCount] = float(row[9])
        rowCount += 1
    file.close()

    jsonData["numtrials"] = rowCount
    jsonData["trialnum"] = trialNums
    jsonData["aiming_landmarks"] = aimingLandmarks
    jsonData["online_fb"] = onlineFB
    jsonData["endpoint_feedback"] = endpointFB
    jsonData["rotation"] = rotation
    jsonData["clamped_fb"] = clampedFB
    jsonData["tgt_angle"] = anglesDict
    jsonData["tgt_distance"] = tgtDistance
    jsonData["between_blocks"] = betweenBlocks
    jsonData["target_jump"] = targetJump
 
    for key in jsonData.keys():
        print ("key: ", key)
        print ("value: ", jsonData[key])
        print ("")

    with open(jsonFilePath, 'w') as outfile:
        json.dump(jsonData, outfile)


"""
Please reference 'tbt_tgtfile_04272020_V2.csv' for how csv files should be formatted.
"""
csvFilePath = 'csv_tgt_files/multiclamp_demo_csv_file.csv'
jsonFilePath = 'public/tgt_files/multiclamp_demo.json'

jsonFromCsv(csvFilePath, jsonFilePath)

