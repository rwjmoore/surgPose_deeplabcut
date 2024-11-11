# surgPose deeplabcut
Repository for using the [deeplabcut toolbox](https://github.com/DeepLabCut/DeepLabCut) for keypoint detection on the [SurgPose Dataset](https://github.com/zijianwu1231/SurgPose). The benchmarks in this repository were generated using the Multi-Animal configuration of the deeplabcut toolbox. 

![alt text](https://github.com/rwjmoore/surgPose_deeplabcut/blob/main/surgPoseDeeplabCut.png?raw=true)


## Instructions for Reproducing Benchmark Results 
1. Install deeplabcut3 with: `pip install deeplabcut`
2. Create a new project using the deeplabcut graphical user interface (GUI) by first running: `python -m deeplabcut`. NOTE: Any video can be selected in the GUI prompt because we will be using a custom formatted dataset. Make sure to select "multianimalproject".
3. Once the project is created, configure the model hyperparameters by editing config.yaml in the project directory or by using the template config.yaml in the templates folder of this repo. If you use the template, make sure the "task", "scorer", "project_path" and "date" fields match your projects. Key portions of the config.yaml are as follows:
   - multianimalbodyparts: These should match the template file and dictate what each keypoint is named after.
   - TrainingFraction: This is dictated by the training/test split determined in Step 5.iii. You will need to change this manually after Step 5.iv.
4. Download the SurgPose Dataset from here and place the images inside the folder: projectdirectory/labeled-data/videoName/
   1. TO BE DETERMINED ...
5. Open a new terminal window in the environment with deeplabcut3 installed and run the following commands:
   1. `ipython`
   2. `import deeplabcut`
   3. `deeplabcut.create_training_dataset("path/to/project/config.yaml",Shuffles=[0],trainIndices=[list(range(0,4505))],testIndices=[list(range(4505,5240))],net_type="resnet_101",augmenter_type="albumentations")`
   4. Note the train/test fraction that this produces. Go to the config.yaml file in the main project directory and ensure that the "TrainingFraction" field in this file matches the train/test fraction.
6. Navigate to the Train Network tab on the deeplabcut GUI. The benchmarks were generated with 17 epochs, which are selected in the Train Network tab. Once the epochs are set, click "Begin Training"
7. After Training is completed, run the following command in the terminal window from Step 5 to evaluate its results: `deeplabcut.evaluate_network("path/to/project/config.yaml",Shuffles=[0],plotting=True)`
8. The results can be found in: projectdirectory/evaluation-results-pytorch/iteration-0/CombinedEvaluation-results.csv


## Benchmark Results
| Trial         | Mean Average Precision (mAP)  |
| ------------- | ------------- |
| 1             | Content Cell  |
| 2             | Content Cell  |
| 3             | Content Cell  |

<p align="center">
  <img src="https://github.com/rwjmoore/surgPose_deeplabcut/blob/main/keypointConfidence.png" alt="Sublime's custom image"/>
   <br>
   Left Tool Keypoint Confidence on Test Set 
</p>
