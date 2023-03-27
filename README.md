# BALF

cuda:

v11.8: https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local

torch:
```
conda install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge
```

others:
```
pip install opencv-python matplotlib pyyaml scipy pymysql sklearn
```

# Train

```
cd yolov5
python .\train.py --batch-size=2 --data=data/cancer_cell.yaml
```

# Infer

```

```