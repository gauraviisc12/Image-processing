
# import json
# import numpy as np 
# def extract_image_names_by_category(json_file, category_id, output_file):
#     with open(json_file, 'r') as f:
#         merged_annotations = json.load(f)

#     images_with_category = []
#     for annotation in merged_annotations['annotations']:
#         if annotation['category_id'] == category_id:
#             image_id = annotation['image_id']
#             image = next((img for img in merged_annotations['images'] if img['id'] == image_id), None)
#             if image:
#                 images_with_category.append(image['file_name'])

#     with open(output_file, 'w') as f:
#         for image_name in images_with_category:
#             f.write(image_name + '\n')
            
# json_file = "/mnt/vol_b/merged_files_final.json"
# category_id_to_extract = 5
# output_text_file = "images_with_category_5_rug.txt"

# extract_image_names_by_category(json_file, category_id_to_extract, output_text_file)

import os
import shutil
from multiprocessing import Pool, cpu_count

def copy_image(image_file):
    mask_file = os.path.join(mask_folder, image_file)
    if os.path.exists(mask_file):
        destination_path = os.path.join(destination_folder, image_file)
        shutil.copy(os.path.join(image_folder, image_file), destination_path)
    

if __name__ == "__main__":
    image_folder =  "/mnt/vol_c/test"
    mask_folder = "/mnt/vol_c/masks_rug_stable_seaformer"
    
    
    destination_folder = "/mnt/vol_c/stable_diffusion_rug_gen"
    
    image_files = os.listdir(image_folder)
    num_processes = cpu_count()
    
    with Pool(processes=num_processes) as pool:
        pool.map(copy_image, image_files)


# import cv2python 
# import os
# import multiprocessing
# input_dir = "/mnt/vol_c/5_class_new_data/masks"
# output_dir = "/mnt/vol_c/rug_masks"


# def create_binary_mask(image):
#     binary_mask = (image == 250).astype(int)
#     return binary_mask

# def process_image(image_file):

#     image = cv2.imread(os.path.join(input_dir, image_file))
    
#     binary_mask = create_binary_mask(image)
    
#     # cv2.imwrite(os.path.join(output_dir, image_file), binary_mask * 255)  

#     if 250 in image:
#         with open("images_with_250.txt", "a") as file:
#             file.write(image_file + '\n')

# if __name__ == "__main__":
  
#     image_files = [f for f in os.listdir(input_dir) if f.endswith('.png') or f.endswith('.jpg')]
    

#     pool = multiprocessing.Pool()
    

#     pool.map(process_image, image_files)
    

#     pool.close()
#     pool.join()

