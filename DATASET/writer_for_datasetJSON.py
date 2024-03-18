import json

nnUNet_dir = 'E:/4Melbourne_uni_2024_S1/research/nnUNet/DATASET/' #此路径根据自己实际修改

def sts_json():
    info = {
        "channel_names": {
            "0": "KiTS"
        },
        "labels": {
            "background": 0,
            "kidney": 1,
            "tumor": 2
        },
        "numTraining": 32,
        "file_ending": ".nii.gz"
    }
    with open(nnUNet_dir + 'nnUNet_raw/Dataset220_KiTS2019/dataset.json',
              'w') as f:
        json.dump(info, f, indent=4)

sts_json()
