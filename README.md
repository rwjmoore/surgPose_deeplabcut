# surgPose deeplabcut
Repository for using the [deeplabcut toolbox](https://github.com/DeepLabCut/DeepLabCut) for keypoint detection on the [SurgPose Dataset](https://github.com/zijianwu1231/SurgPose). The benchmarks in this repository were generated using the Multi-Animal configuration of the deeplabcut toolbox. 

The main contribution of this repository is a data formatting script that can format the SurgPose dataset into a form that is suitable for deeplabcut training workflow. 
<p align="center">
  <img src="https://github.com/rwjmoore/surgPose_deeplabcut/blob/main/surgPoseDeeplabCut.png?raw=true" alt="Sublime's custom image"/>
   <br>
  Example of keypoint inference on a SurgPose dataset frame using a trained deeplabcut model   
</p>


## Instructions for Reproducing Benchmark Results 
1. Install deeplabcut3 with: `pip install deeplabcut`
2. Create a new project using the deeplabcut graphical user interface (GUI) by first running: `python -m deeplabcut`. NOTE: Any video can be selected in the GUI prompt because we will be using a custom formatted dataset. Make sure to select "multianimalproject".
3. Once the project is created, configure the model hyperparameters by editing config.yaml in the project directory or by using the template config.yaml in the templates folder of this repo. If you use the template, make sure the "task", "scorer", "project_path" and "date" fields match your projects. Key portions of the config.yaml are as follows:
   - multianimalbodyparts: These should match the template file and dictate what each keypoint is named after.
   - TrainingFraction: This is dictated by the training/test split determined in Step 5.iii. You will need to change this manually after Step 5.iv.
4. Download the SurgPose Dataset from here and place the images inside the folder: projectdirectory/labeled-data/videoName/ , where videoName is the name of the video you added in Step 2. 
   1. ***The following steps assume that the data you have downloaded consists of a training set from image id 0 to image id 20019 and a test set consists of image id 26026 to image id 30028 ***
   2. A deeplabcut compatible file format for the annotations of the dataset is created using the script: "loadJSON_multiAnimal.py". This produces a file titled "000000DLCformat.csv"
   3. For the deeplabcut benchmarks, this 000000DLCformat.csv file was downsampled (in the training set) to include every fourth image. The actual 000000DLCformat.csv file is attached as CollectedData_example.csv. To replicate the benchmarks, place this CollectedData_example file into the folder from Step 4. Change the file "CollectedData_example.csv" to CollectedData_scorer.csv" where "scorer" is the name in the "scorer" field from Step 3. Change the second column in "CollectedData_example.csv" to be the name of the video from Step 5. Make sure to replace the "example" in the first row of CollectedData_example.csv to this as "scorer" field as well. 
   1. Finally, convert this .csv to a .h5 file by running the command:
      1.`ipython`
      2. `import deeplabcut`
      3. `deeplabcut.convertcsv2h5('path_to_config.yaml', scorer= 'experimenter')` where experimenter is the "scorer" from Step 3.
   2. These steps follow the source: https://deeplabcut.github.io/DeepLabCut/docs/recipes/OtherData.html 
6. Open a new terminal window in the environment with deeplabcut3 installed and run the following commands:
   1. `ipython`
   2. `import deeplabcut`
   3. `deeplabcut.create_training_dataset("path/to/project/config.yaml",Shuffles=[0],trainIndices=[list(range(0,4505))],testIndices=[list(range(4505,7509))],net_type="resnet_101",augmenter_type="albumentations")`
   4. Note the train/test fraction that this produces. Go to the config.yaml file in the main project directory and ensure that the "TrainingFraction" field in this file matches the train/test fraction.
7. Navigate to the Train Network tab on the deeplabcut GUI. The benchmarks were generated with 17 epochs, which are selected in the Train Network tab. Once the epochs are set, click "Begin Training"
8. After Training is completed, run the following command in the terminal window from Step 5 to evaluate its results: `deeplabcut.evaluate_network("path/to/project/config.yaml",Shuffles=[0],plotting=True)`
9. The results can be found in: projectdirectory/evaluation-results-pytorch/iteration-0/CombinedEvaluation-results.csv


## Benchmark Results
| Trial         | Mean Average Precision (mAP)  |
| ------------- | ------------- |
| 1             | 67.9  |
| 2             | 63.4  |
| 3             | 67.95  |

<p align="center">
  <img src="https://github.com/rwjmoore/surgPose_deeplabcut/blob/main/keypointConfidence.png" alt="Sublime's custom image"/>
   <br>
   Left Tool Keypoint Confidence on Test Set 
</p>
