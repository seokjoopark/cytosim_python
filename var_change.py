import os, sys

os.system("cd ----")



file_path = '/Users/user/Desktop/config/config.cym'
new_text1 = "clip_plane0 = 1, 1 -1 0, 0;"
new_text2 = "clip_plane1 = 0, 1 0 0, 1;"
with open(file_path, "r") as f:
    contents = f.readlines()


# contents[15] = "\t" + new_text
# for i in range(1,10,1)
# contents[15] = new_text(i)
contents[15] = new_text1
contents[16] = new_text2


with open(file_path, 'w') as f:
    f.writelines(contents)

f.close()
# print(s_list)
