#! python3
# fileMover.py will take files from a specified directory and move them to a different location

import os, shutil, datetime, re
print(os.getcwd())

# specify target path to look in and destination path to move to
target = "C:\\Users\\mc_sk\\Desktop\\TestDir\\"
destination = "C:\\Users\\mc_sk\\PycharmProjects\\Automation\\"

print('Does the target exist?: ' + str(os.path.exists(target)) + '\nDoes the destination exist?: ' + str(os.path.exists(destination)))
files = {}       # dict = {folder : filename}
folder_regex = re.compile(r'^\d{6}')
time_r = datetime.datetime.now() - datetime.timedelta(minutes=20)

# check if files in target recently modified
for filename in os.listdir(target):
    f_time = datetime.datetime.fromtimestamp(os.path.getmtime(target + filename))
    if f_time >= time_r:
        folder = folder_regex.search(filename)                  # check if file has ticket number in beginning
        print(filename + '\'s last modified time was less than 5 minutes ago so it will be moved.')
        files.setdefault(str(folder.group()) + '\\', filename)  # if folder present in filename, add folder and corresponding filename to dictionary

print('printing items:')
# moves files in list from target to destination
for folder, filename in files.items():
    print('Moving ' + filename)
    print(str(folder) + ' ' + str(filename))
    shutil.move(target + filename, destination + folder + filename)
    print(filename + ' moved !')\
