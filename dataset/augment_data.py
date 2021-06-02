from PIL import Image
import os

# directories 
ORIGINAL_DIR = r"C:\ce301_harding_kiernan_j_w\dataset\augmented\old_training_set\parasitized"
DEST_DIR = r"C:\ce301_harding_kiernan_j_w\dataset\augmented\training_set\parasitized"

count = 0
errors = 0
for file_name in os.listdir(ORIGINAL_DIR):
    try:
        print(str(count) + ": " + file_name)
        colourImg = Image.open(ORIGINAL_DIR + "/" + file_name)
        file_name = file_name[:-4]
        colourImg.save(DEST_DIR + "/" + file_name + "_a0.png")

        colourImg = colourImg.transpose(Image.ROTATE_90)
        colourImg.save(DEST_DIR + "/" + file_name + "_a90.png")

        colourImg = colourImg.transpose(Image.ROTATE_180)
        colourImg.save(DEST_DIR + "/" + file_name + "_a180.png")
        
        colourImg = colourImg.transpose(Image.ROTATE_270)
        colourImg.save(DEST_DIR + "/" + file_name + "_a270.png")
        
        count += 1
    except:
        errors +=1
        print("ERROR " + str(errors))

print("ERRORS: " + str(errors))