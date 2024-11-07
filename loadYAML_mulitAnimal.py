#loads in a SurgPose .yaml file with keypoints and formats the data into DeepLabCut format
#NOTE: Works for multi-animal project in deeplabcut
import yaml
import csv
# Open and read the JSON file
fileID = 000000
with open("C:/Users/Randy/Documents/Github/surgPoseDeepLabCut/SurgPose_DATA/annotations/keypoints_000000_left.yaml", 'r') as file:
    data = yaml.safe_load(file)
    print(data[0])
# Print the data
#contains: 
#{id:[x,y]}

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
    for i in range(0, len(data)):
        row = []
        row.append(prefix)
        row.append("vid" + str(fileID))
        row.append(str(i).zfill(12) + ".png")
        coordRowData = []
        for key in data[i]:
            coordRowData = coordRowData + data[i][key]
        row = row  + coordRowData
        write.writerow(row)

