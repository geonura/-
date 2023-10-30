import torch
from PIL import Image, ImageDraw
import sys
import numpy as np
import os
from django.conf import settings

# YOLOv5의 저장소 경로와 관련 라이브러리 경로를 sys.path에 추가
yolov5_path = 'C:/Users/NAGEON/Documents/GitHub/crackdown_on_illegal_parking/coip/ai/yolov5'
sys.path.append(yolov5_path)

# YOLOv5 모델 불러오기
model = torch.hub.load(yolov5_path,
                       'custom',
                       path='C:/Users/NAGEON/Documents/GitHub/crackdown_on_illegal_parking/coip/ai/yolov5/runs/train/exp/weights/best.pt',
                       source='local')

title = "AI 공항 안전 시스템"
desc = "왼쪽 이미지 입력창에 이미지를 입력하세요.\n오른쪽 이미지 출력창에 예측 결과를 보여줍니다."

def process_and_render(image_path):
    # 이미지 파일을 PIL로 읽어들이기
    img_pil = Image.open(image_path)
    img = np.array(img_pil)
    
    # 이미지 예측
    results = model(img)
    
    draw = ImageDraw.Draw(img_pil)
    # 바운딩 박스만 그리기
    for det in results.pred[0]:
        x1, y1, x2, y2 = map(int, det[:4])
        draw.rectangle([x1, y1, x2, y2], outline="red", width=5)

    # 변환된 이미지를 임시 파일로 저장
    temp_file_path = os.path.join(settings.MEDIA_ROOT, 'temp', 'processed_image.jpg')
    img_pil.save(temp_file_path)
    return temp_file_path