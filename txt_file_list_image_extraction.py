import os
import shutil
from multiprocessing import Pool

def copy_image(image_info):
    filename, image_folder, output_dir = image_info
    image_path = os.path.join(image_folder, filename)
    if os.path.exists(image_path):
        shutil.copy(image_path, output_dir)
    else:
        print(f"File '{filename}' not found in '{image_folder}'")

def extract_images(txt_file, image_folder, output_dir):
    

    with open(txt_file, 'r') as file:
        image_filenames = file.read().splitlines()

    image_info = [(filename, image_folder, output_dir) for filename in image_filenames]

    with Pool() as pool:
        pool.map(copy_image, image_info)

txt_file = '/mnt/vol_c/file_list.txt'
image_folder = '/mnt/vol_c/stable_diff_0.8_masks'
output_dir = '/mnt/vol_c/filtered_rug_stable_diff_masks'

extract_images(txt_file, image_folder, output_dir)
