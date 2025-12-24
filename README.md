# SABER-Net: Enhanced SAR Ship Detection through Structure-Aware and Boundary-Enhanced Network

**This is the official implementation of our paper, "[Enhanced SAR Ship Detection through Structure-Aware and Boundary-Enhanced Network](https://[此处可留空或将来放论文链接])", which has been submitted to *The Visual Computer*.**

Our work proposes SABER-Net, a structure-aware and boundary-enhanced network designed to address the challenges of ship detection in SAR images.

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
4.  **Dataset Preparation:**
    ```bash
    1.HRSID: Please download the dataset from its official source [https://github.com/chaozhong2010/HRSID].
    2.SSDD: Please download the dataset from its official source [https://github.com/TianwenZhang0825/Official-SSDD].
    ```
