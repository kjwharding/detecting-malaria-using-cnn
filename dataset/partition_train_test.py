import os
import random
from shutil import copyfile

# directories 
ORIGINAL_DIR = r"C:\ce301_harding_kiernan_j_w\dataset\download\cell_images\Uninfected"
TESTING_DEST_DIR = r"C:\ce301_harding_kiernan_j_w\dataset\testing_set\uninfected"
TRAINING_DEST_DIR = r"C:\ce301_harding_kiernan_j_w\dataset\training_set\uninfected"

# finding number of files in dir
num_of_files = 0
for path in os.listdir(ORIGINAL_DIR):
    if os.path.isfile(os.path.join(ORIGINAL_DIR, path)):
        num_of_files += 1
print("Number of total files: " + str(num_of_files))

# creating random number list 
RANDOMLIST = random.sample(range(0, num_of_files+1), int(num_of_files/5))
print("20% Partition: " + str(len(RANDOMLIST)))


# creating a test partition with a sample 
count = 0
print("Creating random copies...")
for file_name in os.listdir(ORIGINAL_DIR):
    if (count in RANDOMLIST):
        copyfile(ORIGINAL_DIR + "/" + file_name, TESTING_DEST_DIR + "/" + file_name)
    else:
        copyfile(ORIGINAL_DIR + "/" + file_name, TRAINING_DEST_DIR + "/" + file_name)
    count += 1

# checking there are no duplicates
for file_name_outer in os.listdir(TESTING_DEST_DIR):
    for file_name_inner in os.listdir(TRAINING_DEST_DIR):
        if ((TESTING_DEST_DIR + "/" + file_name_outer) == (TRAINING_DEST_DIR + "/" + file_name_inner)):
            print("Duplicate: " + file_name_outer)


