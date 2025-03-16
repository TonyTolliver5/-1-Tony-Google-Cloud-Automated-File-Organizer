**Project Title:** 
(1) Tony's Google Cloud Automated File Organizer

**Project Overview:** 
This project automatically organizes files uploaded to a Google Cloud Storage bucket by sorting them into pre-existing folders based on file type. It uses a Google Cloud Run python script and Eventarc triggers to detect new file uploads and move them accordingly.

**Technology Used:** 
Google Cloud Storage - to upload, categorize, and store files
EventArc - to trigger Google Cloud Run when a file is uploaded
Python- script to automatically move files into correct folders based on file type
Google Cloud Run - to execute a python script

**Architecture Diagram:** 

![Architecture Diagram](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/main/architecture_file_png.png)

**Set-Up and Deployment:**

**Step 1:** Sign into Google Cloud and create a project to work on.

**Step 2:** Create a Cloud Storage Bucket
A. This bucket will be a source bucket where the files will be uploaded and processed by Cloud Run.
B. Navigate to Cloud Storage
C. Click Create Bucket
D. Set the Following:
-Bucket Name: tony-file-organizer-source
-Storage Class: Standard
-Location: Multi-Region (United States) - the location of this bucket must match the location of the cloud run app to avoid errors!
-Access Control: Uniform
E. Click Create

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/sep%201_finished%20bucket.png)


**Step 3:** Create a Cloud Run Service
A. Enter the Google Cloud Consol
B. Navigate to Google Cloud Run
C. Click Create a Service or Write a Function
D. Set the Following:
-Service Name: tony-file-organizer-app
-Deployment Platform: Managed
-Region: us-central1 (Iowa) - this will be compatible with the bucket Multi-Region (United States)
-Runtime: Python 3.12 (latest version)
-Authentication: Allow all Traffic



![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/Cloud_run_service.png)

E. Connect Event Trigger
-EventArc will ensure Cloud Run is triggered whenever a file is uploaded
-Click Add Trigger and click Cloud Storage as the Event Provider
-In the EventArc window, change the trigger name: file-organizer-trigger
-Trigger Type: Google Sources
-Event Provider: Cloud Storage (confirm again)
-Event Type: google.cloud.storage.object.v1.finalized
-Bucket: Select tony-file-organizer-source (bucket created in Step 2)
-Service Account: Default compute service account
Service Path URL: /
F. Click Create

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/step%203_completed%20trigger.png)

**Step 4:** Upload the Python Script
A. We need to write and deploy a python scrip that will organize the uploaded files into the correct folder
B. Inside of the tony-file-organizer-app, navigate to the Source
C. On the lefthand side, move to the main.py
D. Delete all of the code in main.py
E. Paste the python script below:

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/python_screenshot_script_20.jpg)

[View full main.py] (https://github.com/TonyTolliver5/Anthony-Reprository/blob/main/main.py)

F. Go to the requirements.txt source code
G. Paste this code below:

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/requirements_image.jpg)

[View Requirements.txt] (https://github.com/TonyTolliver5/Anthony-Reprository/blob/main/requirements.txt)

H. Click save and redeploy

I. Fix any errors. (In the error below, I had a problem with the main.py and the requirements.txt. After troubleshooting, I updated with files above)


![Image](https://github.com/user-attachments/assets/362de4cb-8f36-4d01-9c99-70258034674d)


J. Save and redeploy. There should be all green checkmarks and no error logs if successful

![Image](https://github.com/user-attachments/assets/b41c7179-8ca3-45fc-a7d4-37b3f1d72080)

**Step 5: Test the File Organizer**
A. Navigate to Cloud Storage and click Buckets
B. Open the tony-file-organizer-source bucket
C. Click Upload
D. Upload a document (pdf)
E. Click the document folder to ensure the pdf automatically moved to the document folder. 
F. Repeat steps D and E for video files, image files, and others. Ensure they automatically moved to the correct folders

![Image](https://github.com/user-attachments/assets/7ec8ceaa-d306-4bd9-846d-40ae68d9b217)

![Image](https://github.com/user-attachments/assets/698c4e93-cf3a-4386-b6ef-eb88644ed8ed)

![Image](https://github.com/user-attachments/assets/8947f436-8976-4365-b71b-25e94e3ac675)
 
**How it Works:**
1. A user uploads a file to the Google Storage Bucket (document, image, video, or other type of file)
2. EventArc triggers to notify Google Cloud Run that a file has been uploaded
3. Cloud Run will run and execute the main.py python script
4. The python script tells the file which folder to go into based on the file type (Documents, Images, Videos, or Others)
5. The file will move into the appropriate folder category automatically 

**File Categorization:**
The Python script categorizes files based on their extensions and moves them into the appropriate folders inside the Google Cloud Storage bucket.

![Image](https://github.com/user-attachments/assets/69517b54-59cf-4acc-a5e5-cccdc607ad17)

**Example Use Case:**
_Automated File Management for a Manufacturing Company_

_Problem:_ 
A machine manufacturing company generates thousands of files related to the machines they build. These include:

Images & schematics (layouts, electrical/hydraulic designs)
Documents (bills of materials, regulatory paperwork)
Videos (production and instructional content)
Data files (energy consumption, MES integration, analytics)

Each machine can have hundreds of files, and with 10,000+ machines sold annually, manually organizing these files is overwhelming. Misplacing documents can lead to production delays, compliance risks, and inefficiencies.

_Solution:_
An automated file organization system using Google Cloud Run and Google Storage Buckets can:
Detect new file uploads using EventArc triggers
Categorize files automatically based on their type
Move files to correct folders (e.g., Images, Schematics, Videos, Regulatory Docs)
Ensure consistency and easy retrieval for engineers, compliance teams, and sales staff

_Example Flow:_
A production engineer uploads a machine schematic (.jpg) → stored in "Schematics" folder
A quality control manager uploads a regulatory PDF → stored in "Compliance Documents" folder
A marketing team uploads a product demo video → stored in "Marketing Videos" folder

_Impact:_
Saves 100s of manual work hours per year
Reduces errors & lost files
Boosts efficiency across teams


**Future Improvements:**

1. Add more folders to the Google Storage Bucket so that more file types are supported, suck as spreadsheets (.csv, .xlsx)
2. Improve error handling & logging - ensure errors are more easily identifiable for troubleshooting
3. Add user customization so that users can define their own file types instead of predefined ones
4. Optimize Performance- improve the script to handle larger file types
5. Integrate Google Cloud Vision AI (for Images) and Google NLP (Natural Language Processing) (for documents) for smarter document classifications


Author:

Anthony (Tony) Tolliver
Tech Sales & AI/Cloud Enthusiast | Passionate about leveraging AI to drive cloud innovation & automation

Github: https://github.com/TonyTolliver5

LinkedIn: [linkedin.com/in/anthony-tolliver-1b9b167b](https://www.linkedin.com/in/anthony-tolliver-1b9b167b)

Personal: AnthonyTolliver.Net
