# Automated Image Label Detection and Visualization with AWS Rekognition and Python

## Project Overview

This project demonstrates how to use Amazon Rekognition for detecting labels in images stored in an Amazon S3 bucket and visualize these labels with bounding boxes using Python's Pillow library. The solution includes uploading images to S3, analyzing them with Rekognition, and displaying the results with annotations.

## Technologies Used

- **Amazon Rekognition**: For image label detection.
- **Amazon S3**: For storing images.
- **IAM (Identity and Access Management)**: For user authentication and permissions.
- **AWS CLI**: For interacting with AWS services.
- **Python**: For implementing the application logic.
- **Pillow (PIL)**: For image processing and visualization.

## Project Structure

- **`detect_labels` function**: Uses Rekognition to detect labels in the specified image.
- **`show_image_with_labels` function**: Downloads the image from S3, draws bounding boxes around detected labels, and displays the annotated image.
- **`main` function**: Manages the workflow of detecting labels and visualizing them.

## Setup Instructions

1. **AWS Configuration**
   - Ensure you have AWS CLI installed and configured with your credentials. The configuration should include:
     - AWS Access Key ID
     - AWS Secret Access Key
     - Default region (e.g., `us-east-1`)
     - Default output format (e.g., `json`)

2. **Install Dependencies**
   - Install the required Python packages:
     ```bash
     pip install boto3 Pillow
     ```

3. **Upload Images to S3**
   - Upload your image to an S3 bucket. Ensure the bucket and image name are correctly specified in the script.

4. **IAM Permissions**
   - Ensure that your IAM role or user has the necessary permissions for S3 access and Rekognition operations. The required permissions include:
     - `rekognition:DetectLabels`
     - `s3:GetObject`
   - Example IAM policy:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "rekognition:DetectLabels"
           ],
           "Resource": "*"
         },
         {
           "Effect": "Allow",
           "Action": [
             "s3:GetObject"
           ],
           "Resource": "arn:aws:s3:::your-bucket-name/*"
         }
       ]
     }
     ```

## Usage

1. **Update the Script**
   - Modify the `bucket` and `photo` variables in the `main` function to match your S3 bucket name and image file name.

2. **Run the Script**
   - Execute the script using Python:
     ```bash
     python your_script_name.py
     ```
   - The script will print the detected labels and their confidence levels, and display the image with bounding boxes around the detected objects.

- **Image Visualization**: A pop-up window will show the image with red bounding boxes around detected labels.

## Challenges and Solutions

- **Handling AWS Credentials**: Managed using IAM roles and AWS CLI configuration.
- **Image Processing Accuracy**: Implemented error handling and precise bounding box calculations.

## Future Improvements

- Integrate a web interface for user interaction.
- Support additional image formats.
- Implement batch processing for multiple images.


