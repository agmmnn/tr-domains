import os
from rich import print

dir_paths = ["data_docreq", "data_nodoc", "data_other"]
domain_list = [
    [
        "gov.tr",
        "bel.tr",
        "pol.tr",
        "edu.tr",
        "k12.tr",
        "av.tr",
        "dr.tr",
        "tsk.tr",
        "gov.ct.tr",
    ],
    [
        "com.tr",
        "net.tr",
        "org.tr",
        "biz.tr",
        "info.tr",
        "tv.tr",
        "gen.tr",
        "web.tr",
        "name.tr",
        "bbs.tr",
    ],
    ["istanbul", "ist"],
]

# list to store files
res = []
for dir_path in dir_paths:
    lst = []
    for file in os.listdir(dir_path):
        if (
            os.path.isfile(os.path.join(dir_path, file))
            and file.split(".")[-1] == "txt"
        ):
            lst.append(f"{dir_path}/{file}")
    res.append(lst)

count = 0
for idx, j in enumerate(res):
    print(" Count\t\t|")
    print("-\t\t|")
    a = [
        tuple
        for i in domain_list[idx]
        for tuple in j
        if tuple.split("/")[1].split(".txt")[0] == i
    ]
    totalcount = 0
    for i in a:
        with open(i, "r") as f:
            lines = len(f.readlines())
        totalcount = lines + totalcount
        print(f"_`{lines}`_|")
    count = totalcount + count
    print(f"_`{totalcount}`_|")
    print()

print("total: ", count)
