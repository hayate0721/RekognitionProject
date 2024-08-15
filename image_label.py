import boto3 # The AWS SDK for python
from PIL import Image, ImageDraw, ImageFont# Python Imaging Library 

def detect_labels(bucket, photo):
    client = boto3.client('rekognition') # Creates a Rekognition client to interact with Amazon Rekognition
    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, MaxLabels=10) # Sends a request to Rekognition to detect labels
    return response['Labels']  # Extracts and returns the list of detected labelss from the Rekognition response

def show_image_with_labels(bucket, photo, labels):
    # Download the image from S3
    s3 = boto3.resource('s3') # Connects to the S3 service
    s3.Bucket(bucket).download_file(photo, 'local-image.jpg') # Downloads the image from the specified S3 bucket and saves it locally
    
    # Open the image
    image = Image.open('local-image.jpg')
    draw = ImageDraw.Draw(image) # Creates a drawing context that allows you to draw on the image

     # Set font size and type
    fontSize = ImageFont.truetype("/Library/Fonts/Arial.ttf", 25) 
    
    # Draw bounding boxes (if available)
    for label in labels:
        if 'Instances' in label:
            for instance in label['Instances']:
                box = instance['BoundingBox']
                left = image.width * box['Left']
                top = image.height * box['Top']
                width = image.width * box['Width']
                height = image.height * box['Height']
                draw.rectangle([left, top, left + width, top + height], outline="red", width=3) # Draws a rectangle arpund the detected object
                label_text = f"{label['Name']} ({label['Confidence']:.2f}%)"  # Create the label text with confidence percentage
                draw.text((left, top), label_text, fill="red", font=fontSize)  # Optionally add label text
    
    # Show the image with bounding boxes
    image.show()

def main():
    bucket = 'imgae-label-bucket'  # bucket name
    photo = 'IMG_5215.jpg'  # object name

    labels = detect_labels(bucket, photo) # Getting lables by calling "detect_labels"
    
    # Prints the name and confidence level of each label
    print(f"Detected labels for {photo}:")
    for label in labels:
        print(f"{label['Name']}: {label['Confidence']:.2f}%")
    
    # Visualize detected labels with bounding boxes
    show_image_with_labels(bucket, photo, labels)

if __name__ == "__main__":
    main()
