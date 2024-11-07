# surgPose deeplabcut
Repository for using the [deeplabcut toolbox](https://github.com/DeepLabCut/DeepLabCut) for keypoint detection on the [SurgPose Dataset](https://github.com/zijianwu1231/SurgPose). The benchmarks were generated using the Multi-Animal configuration of the deeplabcut toolbox. 

![alt text](https://github.com/rwjmoore/surgPose_deeplabcut/blob/main/surgPoseDeeplabCut.png?raw=true)


## Instructions for Reproducing Benchmark Results 
1. Install deeplabcut3 with: `pip install deeplabcut`
2. Create a new project using the deeplabcut graphical user interface (GUI) by first running: `python -m deeplabcut`. NOTE: Any video can be selected in the GUI prompt because we will be using a custom formatted dataset. Make sure to select "multianimalproject".
3. Once the project is created, configure the model hyperparameters by editing config.yaml in the project directory or by using the template config.yaml in the templates folder of this repo. If you use the template, make sure the "task", "scorer", "project_path" and "date" fields match your projects. Key portions of the config.yaml are as follows:
   - multianimalbodyparts: These should match the template file and dictate what each keypoint is named after.
   - TrainingFraction: This is dictated by the training/test split determined in Step X. It will need to be modified manually after Step X.
4. Download the SurgPose Dataset from here and place the images inside the labeled-data/videoName/ folder of the project

5. Open a new terminal window in the environment with deeplabuct3 installed and run the following commands:
   1. `ipython`
   2. `import deeplabcut`
   3. `deeplabcut.create_training_dataset("C:/Users/Randy/Documents/Github/surgPoseDeepLabCut/surgPoseLarge-randy-2024-09-10/config.yaml",Shuffles=[9],trainIndices=[list(range(0,4505))],testIndices=[list(range(4505,5240))],net_type="resnet_101",augmenter_type="albumentations")`
6. Navigate to the Train Network tab on the deeplabcut GUI and click "Begin Training"
7. After Training is completed, run the following command in the terminal window from Step 5: `deeplabcut.evaluate_network("C:/Users/Randy/Documents/Github/surgPoseDeepLabCut/surgPoseLarge-randy-2024-09-10/config.yaml",Shuffles=[9],plotting=True)`
