import pydicom as dicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
import os
import cv2
import PIL
import pandas as pd
import csv

#Make it True if you want in PNG format
PNG = False

# Specify the .dcm folder path
folder_path = "stage_1_test_images"

#Specify the jpg/png folder path
jpg_folder_path = "JPG_test"

image_path = os.listdir(folder_path)

# list of attributes available in dicom image

dicom_image_description = pd.read_csv("dicom_image_description.csv")
filename = './stage_1_test_images/case2_0001.dcm'

ds1 = dicom.dcmread(filename)

print(ds1.PatientName)

with open('Patient_Detail.csv', 'w', newline='') as csvfile:
    # fieldnames = list(dicom_image_description["Description"])
    writer = csv.writer(csvfile)
    # writer.writerow(fieldnames)
    writer.writerow("Group Elem Description VR value".split())
    for elem in ds1:
        writer.writerow([
            f"{elem.tag.group:04X}", f"{elem.tag.element:04X}",
            elem.description(), elem.VR, str(elem.value)
        ])