import os

# folder path
dir_paths = ["data_docreq", "data_nodoc", "data_other"]

# list to store files
res = []

for dir_path in dir_paths:
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            if file.split(".")[-1] == "txt":
                res.append(f"{dir_path}/{file}")
count = 0
for i in res:
    with open(i, "r") as f:
        lines = len(f.readlines())
        count = lines + count
print(count)
