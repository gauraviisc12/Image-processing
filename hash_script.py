import imagehash
from PIL import Image
import os
from tqdm import tqdm
import json
from multiprocessing import Pool, cpu_count


def process_image(i):
    try:
        
        image = Image.open("/mnt/vol_b/detection_all_data/images/" + i)
        image_hash = imagehash.average_hash(image)
        return (str(image_hash), i)
    except:
        print("img path","/mnt/vol_b/detection_all_data/images" + i)
        print("Error on image", i)
        return ("Error", i)


def process_images_parallel(i):
    return process_image(i)


if __name__ == "__main__":
    image_hashes = {}

    images = os.listdir("/mnt/vol_b/detection_all_data/images")
    
    # image = Image.open("/mnt/vol_b/segmentation_data/merged_dataset_1_class/images" + i)
    
    # Use multiprocessing to parallelize image processing
    with Pool(cpu_count()) as pool:
        results = list(
            tqdm(pool.imap(process_images_parallel, images), total=len(images))
        )

    # Process results
    hashes = {}
    for hash, path in results:
        if hash in hashes:
            hashes[hash].append(path)
        else:
            hashes[hash] = [path]

    print("Done processing images")

    with open("image_hashes_det_check.json", "w") as f:
        json.dump(hashes, f)
    