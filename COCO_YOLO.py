import json
import os
from multiprocessing import Pool
import numpy as np

annotations = []

def process_image(image_info):
    global annotations
    image_id = image_info['id']
    file_name = image_info['file_name']
    image_width = image_info['width']
    image_height = image_info['height']

    labels = []
    for annotation_info in annotations:
        if annotation_info["image_id"] == image_id:
            category_id = annotation_info['category_id']
            bbox = annotation_info['bbox']
            if len(annotation_info['segmentation'])<1:
                continue
            segmentation = np.asarray(annotation_info['segmentation'][0])
            
            assert(segmentation.shape[0] % 2 == 0)
            segmentation_rs = np.reshape(segmentation, (int(segmentation.shape[0] / 2), 2))
            x_centre = (bbox[0] + bbox[2]) / (2 * image_width)
            y_centre = (bbox[1] + bbox[3]) / (2 * image_height)
            width = np.abs((bbox[2] - bbox[0]) / image_width)
            height = np.abs((bbox[3] - bbox[1]) / image_height)
            boundary_str = ""
            for i in segmentation_rs:
                boundary_str += f"{i[0] / image_width} {i[1] / image_height} "
            boundary_str=boundary_str[:-1]
            labels.append(f"0 {boundary_str}")

    output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.txt")
    with open(output_path, 'w') as txt_file:
        txt_file.write('\n'.join(labels))


def coco_to_yolo(coco_json_path, images_folder, output_folder, num_processes=4):
    with open(coco_json_path, 'r') as json_file:
        coco_data = json.load(json_file)

    global annotations
    annotations = coco_data['annotations']
    images = coco_data['images']

    pool = Pool(num_processes)
    pool.map(process_image, images)
    pool.close()
    pool.join()

if __name__ == "__main__":
    coco_json_path = '/mnt/vol_b/segmentation_data/merged_dataset_1_class/annotations/merged_data_1_class.json'
    images_folder = '/mnt/vol_b/segmentation_data/merged_dataset_1_class/images'
    output_folder = '/mnt/vol_b/instance_training_data_segmentation/labels/train'
    
    with open(coco_json_path, 'r') as json_file:
        coco_data = json.load(json_file)

    annotations = coco_data['annotations']
    images = coco_data['images']
    
    

    pool = Pool(4)
    pool.map(process_image, images) 
    pool.close()