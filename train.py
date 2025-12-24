import warnings, os
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    #model = YOLO('ultralytics/cfg/models/11/yolo11n.yaml')
    model = YOLO('ultralytics/cfg/models/11improve/yolo11-SABER.yaml')
    
    #model.load('yolo11n.pt') # loading pretrain weights
    model.train(data='home/SABER/dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=16,
                close_mosaic=0, 
                workers=4, 
                # device='0,1', 
                optimizer='SGD', 
                # patience=0, 
                # resume=True, 
                # amp=False, 
                # fraction=0.2,
                project='runs/exp',
                name='exp',
                )
