# Enhanced SAR Ship Detection through Structure-Aware and Boundary-Enhanced Network
This repository contains the official implementation for the manuscript ‘Enhanced SAR Ship Detection through Structure-Aware and Boundary-Enhanced Network’ submitted to The Visual Computer.”

Our work proposes SABER-Net, a structure-aware and boundary-enhanced network designed to address the challenges of ship detection in SAR images.

<details open>
    
### 0. Environment Setup
1.  **Create a new virtual environment (recommended):**
    ```bash
    conda create -n myenv python=3.9.0
    ```
2.  **Install PyTorch:**
    Please install PyTorch first by following the official instructions from [pytorch.org](https://pytorch.org/) to match your specific hardware (CUDA version or CPU). 
    ```bash
    torch>=2.1.0
    torchvision
    ```
3.  **Install other dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 1. Dataset Preparation

First, you need to prepare your dataset.

1.HRSID: Please download the dataset from its official source [https://github.com/chaozhong2010/HRSID].

2.SSDD: Please download the dataset from its official source [https://github.com/TianwenZhang0825/Official-SSDD].

The dataset should be organized in the following format:

```
dataset/
├── images/
│   ├── train/    
│   ├── val/      
│   └── test/     
└── labels/
    ├── train/   
    ├── val/   
    └── test/  
```

### 2. Dataset Configuration

Create or edit the dataset configuration file (e.g., dataset/data.yaml):

```yaml
# Dataset path
path: /home/SABER/
train: ./dataset/dataname/images/train
val: ./dataset/dataname/images/val
test: ./dataset/dataname/images/test

# Number of classes
nc: 1

# Class names
names: ['ship']
```

### 3. Model Configuration

The model configuration files are located at:
`ultralytics/cfg/models/11/`

### 4. Training

edit `train.py` file：

```python

# Load model (from configuration file or pre-trained weights)
model = YOLO('ultralytics/cfg/models/11/yolo11n.yaml')

# start train
model.train(
    data='dataset/data.yaml',    # Path to dataset configuration file
    epochs=200,                  
    imgsz=640,                  
    batch=16,                    
    device=0,                    # Device ID (use '0,1,2,3' for multi-GPU training)
    workers=4,                  
    cache=False,                 
    optimizer='SGD',             # Optimizer: SGD or Adam
    project='runs/train',        # Project save path
    name='exp',                  # Experiment name
    close_mosaic=0,              # Disable mosaic augmentation for the last N epochs (0 to keep enabled)
    # amp=False,                 
    # resume=True,               
)
```

Run train：

```bash
python train.py
```

</details>
