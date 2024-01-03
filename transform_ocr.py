import cv2
import matplotlib.pyplot as plt
from boxdetect import config
from boxdetect.pipelines import get_boxes
import os
import boxdetect
from boxdetect.img_proc import draw_rects, get_image
import ssl
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from IPython.display import display
import torch

ssl._create_default_https_context = ssl._create_unverified_context

import os

def delete_files_in_folder(folder_path):
    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files and delete each one
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                # print(f"Deleted: {file_path}")

        print("All files deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
folder_path = "/home/vivek/Raj/PyProjects/PythonBasicsConcepts/output"
delete_files_in_folder(folder_path)



# file_path="src/input_files/Newell-Historical-08302021-01_00000174.JPG"
# file_path="/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/Newell-Historical-08302021-01_00000175.JPG"
file_path="/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/00000270.JPG"
# file_path="src/input_files/00000010.JPG"

input_image = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)

cfg = config.PipelinesConfig()

# important to adjust these values to match the size of boxes on your image
cfg.width_range = (30, 100)
cfg.height_range = (30, 100)

# the more scaling factors the more accurate the results but also it takes more time to processing
# too small scaling factor may cause false positives
# too big scaling factor will take a lot of processing time
cfg.scaling_factors = [1.2]

# w/h ratio range for boxes/rectangles filtering
cfg.wh_ratio_range = (0.5, 1.8)

# range of groups sizes to be returned
cfg.group_size_range = (1, 100)

# for this image we will use rectangles as a kernel for morphological transformations
cfg.morph_kernels_type = 'rectangles'  # 'lines'

# num of iterations when running dilation tranformation (to engance the image)
cfg.dilation_iterations = 0

def binarize_image(image_idx, image):
    thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
    image_name = "{:02}.png".format(image_idx)
    image_path = '/home/vivek/Raj/PyProjects/PythonBasicsConcepts/outuput/' + image_name
    cv2.imwrite(image_path, thresh)
    return thresh, image_path

image_path,img = binarize_image(0,input_image)

rects, grouping_rects, image, output_image = get_boxes(
    image_path, cfg=cfg, plot=False)

out_img = draw_rects(get_image(file_path), rects, thickness=3)
# plt.imshow(out_img)
# plt.show()

outputImages = []
for index,rect in enumerate(grouping_rects):
    x1 = rect[0]
    x2 = x1 + rect[2]
    y1 = rect[1]
    y2 = y1 + rect[3]
    cropped_img = out_img[y1:y2, x1:x2]
    gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Remove horizontal
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
    detect_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(cropped_img, [c], -1, (255,255,255), 5)

    # Remove vertical
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,25))
    detect_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(cropped_img, [c], -1, (255,255,255), 5)

    cv2.imwrite(f'/home/vivek/Raj/PyProjects/PythonBasicsConcepts/output/thresh{index}.png', thresh)
    cv2.imwrite(f"/home/vivek/Raj/PyProjects/PythonBasicsConcepts/output/image{index}.png", cropped_img)
    outputImages.append(f"/home/vivek/Raj/PyProjects/PythonBasicsConcepts/output/image{index}.png")

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-large-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-large-handwritten")

# def ocr_image(src_img):
#   pixel_values = processor(images=src_img, return_tensors="pt").pixel_values
#   generated_ids = model.generate(pixel_values,output_scores=True, return_dict_in_generate=True)
#   # print(generated_ids)
#   scores = generated_ids[1]
#   # Print results
#   flat_scores = [score for sublist in scores for score in sublist]
#   # Convert the flat list to a PyTorch tensor
#   tensor_scores = torch.tensor(flat_scores)
#   # Use the tensor as needed
#   print(tensor_scores)
#   for idx, confidence in enumerate(max_values_list):
#     print(f"Row {idx + 1}: Confidence: {confidence}")
#   return processor.batch_decode(generated_ids, skip_special_tokens=True)[0], 0

def ocr_image(src_img):
    pixel_values = processor(images=src_img, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values, output_scores=True, return_dict_in_generate=True)

    # Assuming scores are in the second element of the generated_ids tuple
    scores = generated_ids.scores

    # Extract max confidence values for each row
    max_values_list = [torch.max(row).item() for row in scores]

    # Print confidence values
    # for idx, confidence in enumerate(max_values_list):
        # print(f"Row {idx + 1}: Confidence: {confidence}")

    # Calculate average confidence level
    average_confidence = sum(max_values_list) / len(max_values_list)
    # print(f"Average Confidence: {average_confidence}")

    # Decode generated_ids
    decoded_results = processor.batch_decode(generated_ids["sequences"], skip_special_tokens=True)

    # Print decoded results
    # for idx, result in enumerate(decoded_results):
        # print(f"Row {idx + 1}: OCR Result: {result}")

    # Return OCR results and the average confidence value
    return decoded_results[0], average_confidence




if(file_path=="/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/Newell-Historical-08302021-01_00000175.JPG" or file_path=="/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/Newell-Historical-08302021-01_00000174.JPG"):
    for index,imagePath in enumerate(outputImages) :
        input_image = cv2.imread(imagePath)
        ocrText,score = ocr_image(input_image)
        # print(f"{index} {ocrText} score :{score}")
        if(index == 0):
            print(f"Name : {ocrText} confidance :{score}")
        elif(index == 1):
            print(f"Mailing Address : {ocrText} confidance :{score}")
        elif(index == 2):
            print(f"City : {ocrText.split()[0]} confidance :{score}")
        elif(index == 3):
            print(f"PIN Code : {ocrText} confidance :{score}")
        else:
            continue


if(file_path=="/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/00000270.JPG"):
    for index,imagePath in enumerate(outputImages) :
        input_image = cv2.imread(imagePath)
        ocrText,score = ocr_image(input_image)
        # print(f"{index} {ocrText} score :{score}")
        if(index == 0):
            print(f"First Name : {ocrText} confidance :{score}")
        elif(index == 1):
            print(f"Last Name : {ocrText.split()[0]} confidance :{score}")
        elif(index == 2):
            print(f"Street Address : {ocrText} confidance :{score}")
        elif(index == 4):
            print(f"City : {ocrText.split()[0]} confidance :{score}")
        elif(index == 7):
            print(f"PIN Code : {ocrText} confidance :{score}")
        else:
            continue



if(file_path == "/home/vivek/Raj/PyProjects/PythonBasicsConcepts/src/input_files/00000010.JPG"):
    for index,imagePath in enumerate(outputImages) :
        input_image = cv2.imread(imagePath)
        ocrText,score = ocr_image(input_image)
        # print(f"{index} {ocrText} score :{score}")
        if(index == 0):
            print(f"First Name : {ocrText} confidance :{score}")
        elif(index == 2):
            print(f"Last Name : {ocrText} confidance :{score}")
        elif(index == 3):
            print(f"Street Address : {ocrText} confidance :{score}")
        elif(index == 5):
            print(f"City : {ocrText.split()[0]} confidance :{score}")
        elif(index == 7):
            print(f"PIN Code : {ocrText} confidance :{score}")
        else:
            continue
