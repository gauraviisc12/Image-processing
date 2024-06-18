import os
import shutil
from multiprocessing import Pool

def copy_file(src_file, dest_directory):
    try:
        shutil.copy(src_file, dest_directory)
        print(f"Copied {src_file} to {dest_directory}")
    except Exception as e:
        print(f"Error copying {src_file}: {str(e)}")

def copy_files_parallel(src_directory, dest_directory, num_processes):
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    files_to_copy = []
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            src_file = os.path.join(root, file)
            files_to_copy.append((src_file, dest_directory))

    with Pool(processes=num_processes) as pool:
        pool.starmap(copy_file, files_to_copy)




if __name__ == "__main__":
    source_directory = '/mnt/vol_b/segmentation_data/test_set/images'
    destination_directory = '/mnt/vol_b/instance_training_data_segmentation/images/val'
    num_processes = 4
    copy_files_parallel(source_directory, destination_directory, num_processes)

    

