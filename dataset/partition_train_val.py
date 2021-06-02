import os
import random
from shutil import copyfile

# directories (alter for each category)
ORIGINAL_DIR = r"C:/ce301_harding_kiernan_j_w/dataset/original/training_set/parasitized"
VAL_DEST_DIR = r"C:/ce301_harding_kiernan_j_w/dataset/augmented/validation_set/parasitized"
TRAIN_DEST_DIR = r"C:/ce301_harding_kiernan_j_w/dataset/augmented/training_set/parasitized"

# finding number of files in dir
num_of_files = 0
for path in os.listdir(ORIGINAL_DIR):
    if os.path.isfile(os.path.join(ORIGINAL_DIR, path)):
        num_of_files += 1
print("Number of total files: " + str(num_of_files))

# creating random number list 
RANDOMLIST = random.sample(range(0, num_of_files+1), int(num_of_files/5))
print("20% Partition: " + str(len(RANDOMLIST)))

# creating partition
count = 0
print("Creating random copies...")
for file_name in os.listdir(ORIGINAL_DIR):
    if (count in RANDOMLIST):
        copyfile(ORIGINAL_DIR + "/" + file_name, VAL_DEST_DIR + "/" + file_name)
    else:
        copyfile(ORIGINAL_DIR + "/" + file_name, TRAIN_DEST_DIR + "/" + file_name)
    count += 1

# checking there are no duplicates
for file_name_outer in os.listdir(VAL_DEST_DIR):
    for file_name_inner in os.listdir(TRAIN_DEST_DIR):
        if ((VAL_DEST_DIR + "/" + file_name_outer) == (TRAIN_DEST_DIR + "/" + file_name_inner)):
            print("Duplicate: " + file_name_outer)