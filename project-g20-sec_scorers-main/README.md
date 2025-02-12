[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7886092&assignment_repo_type=AssignmentRepo)
# Crops and Weeds detection
<!-- Replace the "RENAME_ME_WITH_YOUR_PROJECT_TITLE" in the text above with your project Title -->
Course: **CSE 702 - Artificial Intelligence Lab**            
Offered for: Session *2017-18*, Dept. of CSE, SEC
### Group \# **20**
<!-- Replace the "00" in the text above with your project group number. It should be anything between 01 to 25 -->
Group Name: **SEC_SCORERS**

## Contributors' Info
<!-- Fill the blanks with your information. change the last two letter of the registration numbers with the respective digits. Correct the "Session" if needed. -->
|                 |  Member 1  |  Member 2  |
| --------------: | :--------: | :--------: |
|            Name |Redwanul Islam Arif            | Tonoy Chandra Kar           |
| Registration \# | 2017331508 | 2017331558 | 
|         Session |  2017-18   |  2017-18   |
| GitHub Username |RedwanIA            |tonoykar58            |
|            Cell |01688433248            |0170093297            |
|           Email |redwanulislama@gmail.com            |tonoykar71@gmail.com            |


Supervisor
-----------
**Enamul Hassan**         
Assistant Professor     
Department of Computer Science and Engineering          
Shahjalal University of Science and Technology       
[Faculty Profile](https://www.sust.edu/d/cse/faculty-profile-detail/590) and [GitHub Profile](https://github.com/enamcse)


## Project Idea
### Motivation
<!-- Describe here why this project is being done. -->
Weeds in crop fields are a great deal. They share limited resources of a field resulting in lower production of crops. Weed control is vital to agriculture, because weeds decrease yields, increase production costs, interfere with harvest, and lower product quality. Weeds also impede irrigation water flow, compete for natural resources such as sunlight,  interfere with pesticide application, and harbor disease organisms. Our project implements precision firming in which we use YOLOv3 Computer Vision Algorithm in order to distinguish between Weeds and Crops and apply herbicide to weeds. 
### Scope
<!-- Describe the domain space of the project. -->
Our goal is to implement a computer vision algorithm that can be integrated with drones and actuators that detect weeds with cameras and apply certain herbicides with the help of mechanical actuators.
### Platform
<!-- What is the environment requirement of the project? What is the OS? Is it for mobile, web, or general API? -->
We used Python and the OpenCV library in developing the project. This ensures that it can be used in most environments with minor alterations to the source code. However, we have developed the code having Windows OS in mind. As Windows OS provides the most user-friendly environment. 
To run this project "Python>=3.6.0" and the latest release of "OpenCV" is required. 
In a real scenario, the project can be loaded into an Arduino.

### Project Brief
<!-- Describe the project in brief. -->
In this project we developed a python program that utilizes YOLOv3 object detection algorithm to distinguish between Sesame crops and weeds. At first we create a trained YOLO weight using a diversed set of data. In our program, we used this pre-trained weight to detect crops and weeds from live feed of a camera(In application the camera will be attached to a drone). We have utilized OpenCV library for manipulation of media files. 

## Project Deliverables
<!-- This table should reflect what are you going to submit. How your progresses would be visible. Note that, you have to create a corresponding issue in the GitHub issue to submit the work of any milestone. -->
<table>
<thead>
    <tr>
        <th>SL</th>
        <th>Milestone</th>
        <th>Details</th>
        <th>Comments</th>
        <th>Expected Submission Date</th>
        <th>Submission Date</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td> 1 </td>
        <td>40% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 40% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>Data Collection</li>
            <li>Data labeling</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>Collecting and Labeling the data specifically for the project was very time consuming task.</td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>May 10, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>May 25, 2022</td>
    </tr>
    <tr>
        <td> 2 </td>
        <td>70% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 70% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>Training a Weight using the collected dataset</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>Faced some unexpected errors that took a lot of time for troubleshooting.</td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>June 5, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>June 20, 2022</td>
    </tr>
    <tr>
        <td> 3 </td>
        <td>100% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 100% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>Developing the main source code</li>
            <li>Testing</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>The developing stage was challenging.</td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>June 30, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>July 04, 2022</td>
    </tr>
</tbody>
</table>

## Project Presentation Slide
<!-- Upload the project presentation slide in GitHub in pdf format and drop a link here. The current link is a dummy one. -->
[Here](http://surl.li/cikyx) is the presentation slide of the project.

Technical Documentation/ Instruction to Deploy the Project
----------------------------------------------------------
<!-- Write a detailed documentation for a technical user who want to DEPLOY your project. It should be as detailed as possible. You can add a FAQ section if needed where basic troubleshooting questions should be answered. Adding Screenshot is appreciated. -->
1. Download and Install Python from [this](https://www.python.org/downloads) website.
2. Download and install OpenCV form [this](https://opencv.org/releases/) website.
3. Make sure to add them into Environment Variable [here](https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows) is the instruction to check or add Python to environment.
4. Download the weights from [this](https://drive.google.com/drive/folders/1kOKFCs3v98VPb0wSeE07yg09rXdb9XjB?usp=sharing) link as they are Lager than 100MB, They cannot be uploaded to Github. 

5. keep the weights, cfg and name file in the "related_files" folder. 
6. Keep the source file in the base folder.
7. Keep the test images in the "images" folder.


Non-Technical Documentation/ User-guide for the End-Users of the Project
------------------------------------------------------------------------
<!-- Write a detailed documentation for a non-technical user who want to USE THE FEATURES of your project. It should be as detailed as possible with proper screenshots. You may add a FAQ section if needed where common questions should be answered. Adding Screenshot is MUST. -->
1. Run the project on Windows Powershell or Visual Studio Code or any other editor of your choice. 
2. There is two separate files one for image detection(detection_in_still_image.py) and another(detection_in_video) for detection in Live video feed from camera.

Acknowledgement
---------------
<!-- You should acknowledge every external help here. A table could be a good option. From Stackoverflow question to any conference/journal paper everything should be mentioned including its use in your project. You should include the contribution of your friend if you take it from anyone. -->
<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Details</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Dataset</td>
        <td>We have used a dataset from kaggle(https://www.kaggle.com/datasets/ravirajsinh45/crop-and-weed-detection-data-with-bounding-boxes)</td>
    </tr>
    <tr>
        <td>Learning OpenCV</td>
        <td>We Learned to use OpenCV library from a freecodecamp youtube video(https://www.youtube.com/watch?v=oXlwWbU8l2o).</td>
    </tr>
    <tr>
        <td>Training Data</td>
        <td>YOLO's GitHub forum(https://github.com/ultralytics/yolov3) helped us in training the dataset. Their Detailed explanation was fascinating</td>
    </tr>
    <tr>
        <td>Solving Bugs</td>
        <td>We have faced numerous bugs during this project. StackOverflow was the first go-to place whenever we faced a bug. </td>
    </tr>
</tbody>
</table>

Disclaimer and Non-Disclosure Agreement (NDA)
---------------------------------------------
<!-- In the following TWO pairs of square brackets, put an 'x' without quotes after reading and accepting the statements. -->
- [ ] This is to certify that this project is done by the *Contributors* mentioned above and nothing is hidden from the supervisor. The external resource(s) used here is/are properly acknowledged above. If any proof of falsifying is found, then the supervisor and the corresponding authority would take the necessary actions.
- [ ] This is to certify that the above mentioned *Contributors* are fully responsible for the confidentiality of the project. Any part of the project would NOT be shared publicly or privately without the prior permission of the supervisor mentioned above even after the publication of the result. If anything else happens, then the supervisor and the corresponding authority would take the necessary actions.

<!-- Thank you so much. -->