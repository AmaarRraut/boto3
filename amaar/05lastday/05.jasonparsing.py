import json
import pathlib

BASE_DIR=pathlib.Path(__file__).parent.resolve()
#FILE_DIR=f"{BASE_DIR}\\files"

data={
    "Id":1,
    "UserName":"Apple",
    "Password":"Orange"
}

with open(f"{BASE_DIR}\\data.json","w") as fp:
    json.dump(data,fp)
    fp.write("\n")



