import os
import json

input_folder_path = '/mnt/vol_b/annot/'
output_json_path = '/mnt/vol_b/seg_data/rug_annot.json'
merged_data_path = '/mnt/vol_b/seg_data/merged_data_1_class.json'

with open(merged_data_path, 'r') as json_file:
    data = json.load(json_file)

with open('/mnt/vol_b/seg_data/annotations/instances_Test.json') as json_file1:
    data1 = json.load(json_file1)

all_images = []
all_annotations = []
image_id_mapping = {}
new_image_id = 1
new_annotation_id = 1

for image_file in os.listdir(input_folder_path):
    target_file_name = image_file
    image_info = None

    for image in data['images']:
        if image['file_name'] == target_file_name:
            image_info = image
            break

    if image_info:
        original_image_id = image_info['id']
        image_id_mapping[original_image_id] = new_image_id

        target_image_id = new_image_id
        image_info['id'] = target_image_id

        target_annotations = [annotation for annotation in data['annotations'] if annotation['image_id'] == original_image_id]

        for annotation in target_annotations:
            annotation['image_id'] = target_image_id
            annotation['id'] = new_annotation_id
            new_annotation_id += 1

        all_images.append(image_info)
        all_annotations.extend(target_annotations)

        new_image_id += 1

output_json = {
    'licenses': data['licenses'],
    'info': data['info'],
    'categories': data1['categories'],
    'images': all_images,
    'annotations': all_annotations
}

with open(output_json_path, 'w') as output_json_file:
    json.dump(output_json, output_json_file, indent=2)
