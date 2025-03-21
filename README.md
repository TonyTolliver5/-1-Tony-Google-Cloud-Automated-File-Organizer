# (1) Tony's Google Cloud Automated File Organizer  

## Project Overview  
This project **automatically organizes files** uploaded to a **Google Cloud Storage bucket** by sorting them into pre-existing folders based on file type. It uses a **Google Cloud Run Python script** and **EventArc triggers** to detect new file uploads and move them accordingly.  

## Technology Used  
- **Google Cloud Storage** – Upload, categorize, and store files  
- **EventArc** – Trigger Google Cloud Run when a file is uploaded  
- **Python** – Script to automatically move files into the correct folders based on file type  
- **Google Cloud Run** – Execute the Python script  

## Architecture Diagram  

![Architecture Diagram](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/main/architecture_file_png.png)

## Set-Up and Deployment  

### Prerequisites  
Before deploying this project, ensure you have:  
- A **Google Cloud account** with billing enabled  
- The **Google Cloud CLI** installed  
- Basic knowledge of **Google Cloud Storage, Cloud Run, and Python**

### Step 1: Sign into Google Cloud  
**A.** Create a project to work on.

### Step 2: Create a Cloud Storage Bucket  
**A.** This bucket will be a source bucket where the files will be uploaded and processed by Cloud Run.  
**B.** Navigate to Cloud Storage.  
**C.** Click **"Create Bucket"**.  
**D.** Set the following:  
   - **Bucket Name:** `tony-file-organizer-source`  
   - **Storage Class:** Standard  
   - **Location:** Multi-Region (United States) *(The location of this bucket must match the location of the Cloud Run app to avoid errors!)*  
   - **Access Control:** Uniform  
**E.** Click **"Create"**. 

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/sep%201_finished%20bucket.png)


### Step 3: Create a Cloud Run Service  
**A.** Enter the Google Cloud Console.  
**B.** Navigate to Google Cloud Run.  
**C.** Click **"Create a Service"** or **"Write a Function"**.  
**D.** Set the following:  
   - **Service Name:** `tony-file-organizer-app`  
   - **Deployment Platform:** Managed  
   - **Region:** `us-central1 (Iowa)` *(Must be compatible with the bucket's Multi-Region setting: United States.)*  
   - **Runtime:** Python 3.12 (latest version)  
   - **Authentication:** Allow all Traffic  



![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/Cloud_run_service.png)

**E. Connect Event Trigger**  
   - EventArc will ensure Cloud Run is triggered whenever a file is uploaded.  
   - Click **"Add Trigger"** and select **Cloud Storage** as the Event Provider.  
   - In the **EventArc** window, configure the following settings:  
     - **Trigger Name:** `file-organizer-trigger`  
     - **Trigger Type:** Google Sources  
     - **Event Provider:** Cloud Storage (confirm again)  
     - **Event Type:** `google.cloud.storage.object.v1.finalized`  
     - **Bucket:** Select `tony-file-organizer-source` (bucket created in Step 2)  
     - **Service Account:** Default Compute Service Account  
     - **Service Path URL:** `/`  

**F. Click "Create"**  

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/step%203_completed%20trigger.png)

### Step 4: Upload the Python Script

**A.** We need to write and deploy a Python script that will organize the uploaded files into the correct folder.  
**B.** Inside of the `tony-file-organizer-app`, navigate to the **Source**.  
**C.** On the left-hand side, move to **main.py**.  
**D.** Delete all of the code in `main.py`.  
**E.** Paste the Python script below:  

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/python_screenshot_script_20.jpg)

[View full main.py] (https://github.com/TonyTolliver5/Anthony-Reprository/blob/main/main.py)

**F.** Go to the `requirements.txt` source code.  
**G.** Paste the following code below:  

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/requirements_image.jpg)

[View Requirements.txt] (https://github.com/TonyTolliver5/Anthony-Reprository/blob/main/requirements.txt)

**H.** Click "Save and Redeploy".  

**I.** Fix any errors.  
   - If errors occur, review the logs for `main.py` and `requirements.txt`.  
   - Troubleshoot and update files accordingly.


![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/error.png)

**J.** Save and redeploy again.  
   - Ensure **all green checkmarks** appear.  
   - There should be **no error logs** if successful.  

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/successful_deployment.jpg)


### Step 5: Test the File Organizer  

**A.** Navigate to **Cloud Storage** and click **Buckets**.  
**B.** Open the `tony-file-organizer-source` bucket.  
**C.** Click **Upload**.  
**D.** Upload a **document (PDF)**.  
**E.** Click the **Documents** folder to ensure the PDF **automatically moved** to the correct folder.  
**F.** Repeat **Steps D and E** for:  
   - **Video files**  
   - **Image files**  
   - **Other file types**  
   - Ensure all files **automatically move** to their respective folders.  

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/working_document.png)


![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/working_image.png)


![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/working_other.png)

## How it Works

1. A user uploads a file to the **Google Storage Bucket** (document, image, video, or other type of file).  
2. **EventArc** triggers to notify **Google Cloud Run** that a file has been uploaded.  
3. **Cloud Run** executes the `main.py` Python script.  
4. The Python script determines the correct folder for the file based on its type:  
   - **Documents** (PDF, TXT, DOCX, etc.)  
   - **Images** (JPG, PNG, GIF, etc.)  
   - **Videos** (MP4, MOV, AVI, etc.)  
   - **Others** (Uncategorized files)  
5. The file is automatically moved into the appropriate folder category.
   

## File Categorization  

The Python script categorizes files based on their extensions and moves them into the appropriate folders inside the **Google Cloud Storage bucket**.  

- **Documents:** PDF, TXT, DOCX, etc.  
- **Images:** JPG, PNG, GIF, etc.  
- **Videos:** MP4, MOV, AVI, etc.  
- **Others:** Any files that do not fit into the above categories. 

![Image](https://raw.githubusercontent.com/TonyTolliver5/-1-Tony-Google-Cloud-Automated-File-Organizer/refs/heads/main/file_types.jpg)


## Example Use Case: Automated File Management for a Manufacturing Company  

### Problem  
A machine manufacturing company generates thousands of files related to the machines they build. These include:  

- **Images & schematics** (layouts, electrical/hydraulic designs)  
- **Documents** (bills of materials, regulatory paperwork)  
- **Videos** (production and instructional content)  
- **Data files** (energy consumption, MES integration, analytics)  

Each machine can have hundreds of files, and with **10,000+ machines sold annually**, manually organizing these files is overwhelming. Misplacing documents can lead to **production delays, compliance risks, and inefficiencies**.  

### Solution  
An **automated file organization system** using **Google Cloud Run** and **Google Storage Buckets** can:  

✅ Detect new file uploads using **EventArc triggers**  
✅ **Categorize files** automatically based on their type  
✅ Move files to correct folders (e.g., **Images, Schematics, Videos, Regulatory Docs**)  
✅ Ensure **consistency and easy retrieval** for engineers, compliance teams, and sales staff  

### Example Flow  
- A **production engineer** uploads a **machine schematic (.jpg)** → stored in **"Schematics"** folder  
- A **quality control manager** uploads a **regulatory PDF** → stored in **"Compliance Documents"** folder  
- A **marketing team** uploads a **product demo video** → stored in **"Marketing Videos"** folder  

### Impact  
🚀 **Saves 100s of manual work hours per year**  
📂 **Reduces errors & lost files**  
⚡ **Boosts efficiency across teams**  


## Author  

**Anthony (Tony) Tolliver**  
**Tech Sales & AI/Cloud Enthusiast** | Passionate about leveraging AI to drive cloud innovation & automation  

- **GitHub:** [github.com/TonyTolliver5](https://github.com/TonyTolliver5)  
- **LinkedIn:** [linkedin.com/in/anthony-tolliver-1b9b167b](https://www.linkedin.com/in/anthony-tolliver-1b9b167b)  
- **Personal Website:** [AnthonyTolliver.Net](https://AnthonyTolliver.Net)  
