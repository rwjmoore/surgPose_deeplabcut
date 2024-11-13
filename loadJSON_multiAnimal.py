import json
import csv


def remove_every_third(lst):
    # Return a new list with every 3rd item removed
    return [item for i, item in enumerate(lst, 1) if i % 3 != 0]


fileID = 000000

# Open and read the JSON file
with open("C:/Users/Randy/OneDrive - UBC/surgicalPoseEstimation/SurgPose_dev/annotations/annotations/annotation_train_new.json", 'r') as file:
    data = json.load(file)

# Print the data
#contains: 
#images: filename, height, widht, id
#annotations: keypoints: [], num_keypoints, area, iscrowd, image_id, bbox, category_id, id
#categories: id, name (toolname)
print(data['annotations'][0]['keypoints'])
print(len(data['annotations']))
print(len(data['images']))


#desired format for csv file in labeled-data
#24 columns of Randy
bodyparts = 14
bodypartsHeader = ["bodyparts","","","k1","k1","k2","k2","k3","k3","k4","k4","k5","k5","k6","k6","k7","k7","k1","k1","k2","k2","k3","k3","k4","k4","k5","k5","k6","k6","k7","k7"]
scorer = "randy"
headerScorer = ["scorer","","", scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer,scorer]
individuals = ["individuals","","","left","left","left","left","left","left","left","left","left","left","left","left","left","left","right","right","right","right","right","right","right","right","right","right","right","right","right","right"]
coords = ['coords',"",""]
for i in range(0,bodyparts):
    coords.append("x")
    coords.append("y")

#loop that formats data into csv format 
with open(str(fileID).zfill(6) + "DLCformat.csv",'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(headerScorer)
    write.writerow(individuals)
    write.writerow(bodypartsHeader)
    write.writerow(coords)

    prefix = "labeled-data"
    annotateCount = 0
    for i in range(0, len(data['images'])):
        row = []
        row.append(prefix)
        row.append("vid" + str(fileID))
        fileName =data['images'][i]["file_name"]
        print(fileName)
        row.append(fileName)
        keypoints = data["annotations"][annotateCount]['keypoints']
        annotateCount+=1
        keypoints += data["annotations"][annotateCount]['keypoints']
        annotateCount+=1
        coordRowData = remove_every_third(keypoints)
        row = row  + coordRowData
        write.writerow(row)