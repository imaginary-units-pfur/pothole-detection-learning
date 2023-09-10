import cv2
from PIL import Image
from ultralytics import YOLO

model_path = './weights/best.pt'
img_path = './test/road_holes.png'
# Load a model
model = YOLO(model_path)

idx2label = {2: 'Продольная трещина',
 4: 'Поперечная трещина',
 0: 'Аллегаторная трещина',
 1: 'Колея, неровность, выбоина, расслоение',
 5: 'Размытие пешеходного перехода',
 3: 'Размытие дорожной разметки',
 7: 'Ремонт',
 6: 'Служебное отверстие (люк для обслуживания)'}

model.names.update(idx2label)

pred = model.predict(img_path, 
                     iou=0.1, conf=0.1, 
                     imgsz=(640, 640), augment=True,
                    )

result = cv2.cvtColor(pred[0].plot(), cv2.COLOR_BGR2RGB)

Image.fromarray(result).save('result.png')
