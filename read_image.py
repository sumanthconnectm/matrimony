# import cv2
# import pytesseract

# # Load image
# img = cv2.imread("test.jpg")

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Threshold (helps with designed backgrounds)
# _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# # OCR config (digits only)
# custom_config = r'--oem 3 --psm 6 outputbase digits'
# text = pytesseract.image_to_string(thresh, config=custom_config)

# print("Detected number:", text.strip())

#==================================================================================================

# import pytesseract
# from PIL import Image

# # Name of the uploaded image file
# image_path = 'test.jpg'

# # Open the image using the Pillow (PIL) library
# image = Image.open(image_path)

# # Use pytesseract to perform OCR on the image
# extracted_text = pytesseract.image_to_string(image)

# # Print the extracted text
# print(extracted_text)


# import os

# for file in os.listdir(path = "photos/"):

#     if os.path.exists("renamed/"+file):
#         pass
#     else:
#         os.rename("photos/"+file, "renamed/"+file)



# import cv2
# import pytesseract
# from PIL import Image
# import os

# detect_nums = [ '296', '388', '678', '388', '372', '546', '372', '296', '711', '670', '352', '322', '373', '351', '307', '819', '473', '557', '730', '740', '761', '466', '848', '850', '851', '862', '852', '856', '854', '841', '829', '828', '827', '826', '820', '813', '812', '811', '803', '798', '800', '797', '795', '794', '789', '791', '655', '655', '638', '638', '888', '888', '169', '169', '900', '900', '658', '658', '196', '196', '906', '906', '548', '548', '828', '828', '411', '633', '756', '655', '775', '694', '864', '775', '915', '774', '434', '613', '809', '464', '920', '638']
# detected_numbers = []
# for file in os.listdir(path = "detected/"):

#     try:
#         if file.endswith(".jpg"):
#             image_path = "detected//"+file
#         else:
#             continue
#         # Name of the uploaded image file
#         # image_path = 'test.jpg'

#     # Load the image using OpenCV
#         # print(image_path)
#         image = cv2.imread(image_path)

#         # Convert the image from BGR to HSV color space
#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#         # Define the lower and upper bounds for the color red in HSV
#         # Red has a wide range in HSV, so two ranges are often needed
#         lower_red_1 = (0, 100, 100)
#         upper_red_1 = (10, 255, 255)
#         lower_red_2 = (160, 100, 100)
#         upper_red_2 = (179, 255, 255)

#         # Create a mask to isolate the red color
#         mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
#         mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
#         red_mask = mask1 + mask2

#         # Find contours in the red mask
#         contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         if contours:
#             # Find the largest contour, assuming it is the badge
#             largest_contour = max(contours, key=cv2.contourArea)

#             # Get the bounding box of the largest contour
#             x, y, w, h = cv2.boundingRect(largest_contour)

#             # Use the bounding box coordinates to crop the original image
#             cropped_image = image[y:y+h, x:x+w]

#             # Convert the cropped image to PIL format for pytesseract
#             cropped_pil_image = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

#             # Perform OCR on the cropped image with a specific configuration
#             extracted_text = pytesseract.image_to_string(cropped_pil_image, config='--psm 6')

#             if len(extracted_text.strip()) in [2,3]:
#                 if extracted_text.strip() in detect_nums:   
#                     # if not os.path.exists(f"renamed//{extracted_text.strip()}"):
#                         # os.makedirs("renamed")
#                     os.rename(image_path, os.path.join("duplicates", f"{extracted_text.strip()}.jpg"))                               
#                     print(f"The number found is: {extracted_text.strip()}")
#                             # detected_numbers.append(extracted_text.strip())
                    
    
#     except Exception as e:
#         # print(f"An error occurred: {e}")
#         pass

# print(detected_numbers)

# import os

# import cv2
# import pytesseract
# from PIL import Image
# import numpy as np


# for file in os.listdir(path = "photos/"):

#     try:
#         # Name of the uploaded image file
#         image_path = "photos//"+file

#         # Load the image using OpenCV
#         image = cv2.imread(image_path)

#         # Convert the image to HSV color space
#         hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#         # Define the range for red color in HSV
#         # Red has two ranges in HSV, so we'll use both
#         lower_red1 = np.array([0, 100, 100])
#         upper_red1 = np.array([10, 255, 255])
#         lower_red2 = np.array([160, 100, 100])
#         upper_red2 = np.array([179, 255, 255])

#         # Create masks for the two red ranges
#         mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
#         mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
#         red_mask = mask1 + mask2

#         # Find contours in the mask
#         contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         if contours:
#             # Find the largest contour by area, which corresponds to the number 346
#             largest_contour = max(contours, key=cv2.contourArea)

#             # Get the bounding box of the largest contour
#             x, y, w, h = cv2.boundingRect(largest_contour)

#             # Crop the original image using the bounding box
#             cropped_image = image[y:y+h, x:x+w]

#             # Convert the cropped image to PIL format for pytesseract
#             cropped_pil_image = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

#             # Perform OCR on the cropped image with specific configuration for numbers
#             extracted_text = pytesseract.image_to_string(cropped_pil_image, config='--psm 6')

#             print(f"The number found is: {extracted_text.strip()}")
#         else:
#             print("No red-colored objects were found in the image.")
    
#     except Exception as e:
#         print(f"An error occurred: {e}")
