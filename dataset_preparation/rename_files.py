# renaming all files in a folder

import os

folder_path = "/home/higopika/Desktop/dvc_model_training/downloaded_datasets/ezgif-4-c1c5a3ebf8-png-split"

file_list = os.listdir(folder_path)

j = 751
new_file_name = ""
for i in file_list:
    current_file_name = os.path.join(folder_path, i)
    new_file_name = folder_path + "/" + str(j) + ".png"
    os.rename(current_file_name, new_file_name)
    j += 1
    print("----------------------------Done with file" + i + "----------------------------")
    


