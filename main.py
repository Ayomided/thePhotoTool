# from flask import Flask, request, jsonify
from exif import Image

# app = Flask(__name__)

# @app.route('/')
# def photoTool():
#     return 'Welcome to The Photo Tool'


# if __name__ == '__main__':
#     app.run(debug=True)

with open('/Users/davidayomide/Documents/apic.jpeg', 'rb') as test_image_file:
    test_image_file = Image(test_image_file)

with open('/Users/davidayomide/Downloads/anoPic.jpeg', 'rb') as test_image_file_1:
    test_image_file_1 = Image(test_image_file_1)

images = [test_image_file_1]

# image_members = []

# for image in images:
#     image_members.append(dir(image))

# for index, image_member_list in enumerate(image_members):
#     print(f"Image {index} contains {len(image_member_list)} members:")
#     print(f"{image_member_list}\n")

for index, image in enumerate(images):
    if len(image.make) & len(image.model) > 0:
        print(f'Device Information - Image {index}')
        print('----------------------------')
        print(f'Make: {image.make}') 
        print(f'Model: {image.model}')
        # print(f'Location: {image.gps_latitude}, {image.gps_longitude}\n')
    elif len(image.make) & len(image.model) < 0:
        print(f'This image {index}, is maybe a screenshot')
