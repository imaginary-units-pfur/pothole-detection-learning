## Training code

1. Data was taken from open source: https://github.com/sekilab/RoadDamageDetector/tree/master .
2. We kept 8 class labels: 
            0: 'Аллегаторная трещина',
            1: 'Колея, неровность, выбоина, расслоение'
            2: 'Продольная трещина'
            3: 'Размытие дорожной разметки'
            4: 'Поперечная трещина'
            5: 'Размытие пешеходного перехода,
            6: 'Служебное отверстие (люк для обслуживания)'
            7: 'Ремонт'
3. For training we used YOLOv8 small version


To reproduce:
1. Download data from: https://drive.google.com/drive/folders/1dkVJo78kwZFchYE-7IeKLjpsuuf1kmQX?usp=sharing
2.
    ```
     unzip data.zip
    ```
4. Change cfg.yaml "data" variable for path where train and valid were unzipped
5. For training run:
    ```
         python train.py
    ```
5. For inference run:
   ```
    python predict.py
   ```
