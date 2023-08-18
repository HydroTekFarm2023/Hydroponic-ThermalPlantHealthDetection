# from flask import Flask, request, jsonify
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# app = Flask(__name__)

# @app.route('/color-detection', methods=['GET'])
# def detect_color():
#     # Get the file path from the request arguments
#     file_path = request.args.get("file_path")

#     # Read the image
#     img = cv2.imread(file_path)

#     # Convert the image to HSV color space
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     # Define the range of colors in HSV
#     lower_red = np.array([0, 100, 100])
#     upper_red = np.array([10, 255, 255])

#     lower_orange = np.array([10, 100, 100])
#     upper_orange = np.array([20, 255, 255])

#     lower_yellow = np.array([20, 100, 100])
#     upper_yellow = np.array([30, 255, 255])

#     lower_green = np.array([36, 25, 25])
#     upper_green = np.array([70, 255, 255])

#     lower_blue = np.array([100, 100, 100])
#     upper_blue = np.array([130, 255, 255])

#     # Create binary masks for each color
#     red_mask = cv2.inRange(hsv, lower_red, upper_red)
#     orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
#     yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
#     green_mask = cv2.inRange(hsv, lower_green, upper_green)
#     blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

#     # Calculate the number of pixels for each color
#     red_pixels = cv2.countNonZero(red_mask)
#     orange_pixels = cv2.countNonZero(orange_mask)
#     yellow_pixels = cv2.countNonZero(yellow_mask)
#     green_pixels = cv2.countNonZero(green_mask)
#     blue_pixels = cv2.countNonZero(blue_mask)

#     # Calculate the total number of pixels in the image
#     total_pixels = img.shape[0] * img.shape[1]

#     # Calculate the percentage of each color in the image
#     red_percentage = round((red_pixels / total_pixels) * 100, 2)
#     orange_percentage = round((orange_pixels / total_pixels) * 100, 2)
#     yellow_percentage = round((yellow_pixels / total_pixels) * 100, 2)
#     green_percentage = round((green_pixels / total_pixels) * 100, 2)
#     blue_percentage = round((blue_pixels / total_pixels) * 100, 2)

#  # Plot the pie chart
#     labels = ['Red', 'Orange', 'Yellow', 'Blue', 'Green']
#     sizes = [red_percentage, orange_percentage, yellow_percentage, blue_percentage, green_percentage]
#     colors = ['red', 'orange', 'yellow', 'blue', 'green']
#     plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
#     plt.axis('equal')
#     plt.show()

#     # Return the results as a JSON object
#     return jsonify({
#         "Red Percentage": red_percentage,
#         "Orange Percentage": orange_percentage,
#         "Yellow Percentage": yellow_percentage,
#         "Green Percentage": green_percentage,
#         "Blue Percentage": blue_percentage,
#     })

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify
import cv2
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/color-detection', methods=['GET'])
def detect_color():
    # Set the file path of the image you want to process
    file_path = "Images\L4.jpeg"

    # Read the image
    img = cv2.imread(file_path)

    #Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the range of colors in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([20, 255, 255])

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    lower_green = np.array([36, 25, 25])
    upper_green = np.array([70, 255, 255])

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    # Create binary masks for each color
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Calculate the number of pixels for each color
    red_pixels = cv2.countNonZero(red_mask)
    orange_pixels = cv2.countNonZero(orange_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)
    green_pixels = cv2.countNonZero(green_mask)
    blue_pixels = cv2.countNonZero(blue_mask)

    # Calculate the total number of pixels in the image
    total_pixels = img.shape[0] * img.shape[1]

    # Calculate the percentage of each color in the image
    red_percentage = round((red_pixels / total_pixels) * 100, 2)
    orange_percentage = round((orange_pixels / total_pixels) * 100, 2)
    yellow_percentage = round((yellow_pixels / total_pixels) * 100, 2)
    green_percentage = round((green_pixels / total_pixels) * 100, 2)
    blue_percentage = round((blue_pixels / total_pixels) * 100, 2)

 # Plot the pie chart
    # labels = ['Red', 'Orange', 'Yellow', 'Blue', 'Green']
    # sizes = [red_percentage, orange_percentage, yellow_percentage, blue_percentage, green_percentage]
    # colors = ['red', 'orange', 'yellow', 'blue', 'green']
    # plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    # plt.axis('equal')
    # plt.show()

    # Return the results as a JSON object
    return jsonify({
        "Red Percentage": red_percentage,
        "Orange Percentage": orange_percentage,
        "Yellow Percentage": yellow_percentage,
        "Green Percentage": green_percentage,
        "Blue Percentage": blue_percentage,
    })

if __name__ == '__main__':
    app.run(debug=True)