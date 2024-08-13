import boto3
from PIL import Image, ImageDraw

def detect_labels(bucket, photo):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, MaxLabels=10)
    return response['Labels']  # Corrected from 'Label' to 'Labels'

def show_image_with_labels(bucket, photo, labels):
    # Download the image from S3
    s3 = boto3.resource('s3')
    s3.Bucket(bucket).download_file(photo, 'local-image.jpg')
    
    # Open the image
    image = Image.open('local-image.jpg')
    draw = ImageDraw.Draw(image)
    
    # Draw bounding boxes (if available)
    for label in labels:
        if 'Instances' in label:
            for instance in label['Instances']:
                box = instance['BoundingBox']
                left = image.width * box['Left']
                top = image.height * box['Top']
                width = image.width * box['Width']
                height = image.height * box['Height']
                draw.rectangle([left, top, left + width, top + height], outline="red", width=3)
                draw.text((left, top), label['Name'], fill="red")  # Optionally add label text
    
    # Show the image with bounding boxes
    image.show()

def main():
    bucket = 'imgae-label-bucket'  # bucket name
    photo = 'IMG_58785834CE3D-1.jpeg'  # object name

    labels = detect_labels(bucket, photo)
    
    print(f"Detected labels for {photo}:")
    for label in labels:
        print(f"{label['Name']}: {label['Confidence']:.2f}%")
    
    # Visualize detected labels with bounding boxes
    show_image_with_labels(bucket, photo, labels)

if __name__ == "__main__":
    main()
