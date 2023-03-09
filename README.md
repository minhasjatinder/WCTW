# **ServiceNow Women Code to Win**
## Problem Statement : Future of Sustainable Environment
### **Project : IOT based Electricity Consumption Analysis and Automation of Appliances**
#### **Description About the Project** : 
The basic idea is to reduce the electricity consumption by automating the electrical appliances 
The prototye functions as follows :
1. Whenever a person is detected in room connected appliances automatically turn on . 
2. Whenever no person is detected in the room , appliances are not turned off immediately , rather a fixed number of reminders are sent on the connected user's phone to turn off the appliances but if the reminder limit exceeds and still the person is not detected , then the appliances will be turned off automatically . 
3. The data related to consumption trends of the electrical appliances is visualised using a dashboard and the dashboard is integrated into a website.
### GOAL 1 . We have created a hardware prototype for the Automation of Appliances to reduce the electricity wastage when appliances are left turned on by mistake .
### HARDWARE SETUP :
1 . Connecting the appliances to the program .
### **Platform Used**  : Arduino IDE 
    
    Step 1 . Connecting the arduino UNO through the port to the device 
<img width="700" alt="ss-4" src="https://user-images.githubusercontent.com/91667539/224037407-71f6f443-edce-4f27-afc0-be686143ca27.png">

    Step 2 . Including Cvzone library so that the human recognition program successfully gets connected to the arduino and hence to the appliances. 
<img width="700" alt="ss-7" src="https://user-images.githubusercontent.com/91667539/224037853-242c1c0c-2e01-4701-aaab-10fe82e40a26.png">

    Step 3 . Writing the logic to turn on and off LED's . 
<img width="700" alt="ss-8" src="https://user-images.githubusercontent.com/91667539/224037913-279e740c-f829-4e95-9266-f1dd019b7c2c.png">



### Code for detecting humans and controlling the appliances accordingly. 
Using OpenCv (OpenCV is a library of programming functions mainly for real-time computer vision) . [OpenCv](https://g.co/kgs/mrAQVM) for the detection of a human body and writing a logic to turn on and off the appliances accordingly. 


## **SEE CODE** [here](https://github.com/minhasjatinder/WCTW/tree/main/Automation%20of%20Appliances)

### Goal 2. The second part is the Dashboard created which shows the consumption trends so that we can analyse and work on the areas where there is more electricity wastage.

LIVE DASHBOARD : [Click here and login with the given credentials to see experience the dashboard ](https://minhasjatinder-wctw-test-7sb27s.streamlit.app/)

Email : 2023minhas2023@gmail.com
Password : DummyAccount@001
![Screenshot 2023-03-06 185506](https://user-images.githubusercontent.com/91667539/224035638-4993755f-99f6-4bfa-9b35-33f2d5812d1d.png)
