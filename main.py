from google.cloud import storage
import functions_framework

# Triggered by a new file upload in Cloud Storage
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data
    bucket_name = data["bucket"]
    file_name = data["name"]

    print(f"File {file_name} was uploaded to {bucket_name}")

    # Initialize Google Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Define file categories and ensure case consistency
    file_types = {
        "Images": ["jpg", "jpeg", "png", "gif"],
        "Documents": ["pdf", "docx", "txt"],
        "Videos": ["mp4", "mov", "avi"]
    }

    # Determine file category
    file_extension = file_name.split(".")[-1].lower()
    category = next(
        (folder for folder, extensions in file_types.items() if file_extension in extensions),
        "Other"
    )

    # Set destination folder (use case-sensitive match for pre-existing folders)
    destination_folder = category  # Ensures "Documents" instead of "documents"

    # Avoid moving files if they are already inside the correct folder
    if file_name.startswith(f"{destination_folder}/"):
        print(f"File {file_name} is already inside the correct category folder.")
        return

    # Move file to the correct existing folder
    destination_blob_name = f"{destination_folder}/{file_name.split('/')[-1]}"
    blob = bucket.blob(file_name)
    new_blob = bucket.rename_blob(blob, destination_blob_name)

    print(f"Moved {file_name} to {destination_blob_name}")
