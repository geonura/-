import gradio as gr
import torch
from PIL import Image, ImageDraw
import sys

# YOLOv5의 저장소 경로와 관련 라이브러리 경로를 sys.path에 추가
yolov5_path = '/Users/yujunwon/Work/work2/yolov5'
sys.path.append(yolov5_path)

# YOLOv5 모델 불러오기
model = torch.hub.load(yolov5_path,
                       'custom',
                       path='/Users/yujunwon/Work/work2/yolov5/runs/train/exp/weights/best.pt',
                       source='local')

title = "AI 공항 안전 시스템"
desc = "왼쪽 이미지 입력창에 이미지를 입력하세요.\n오른쪽 이미지 출력창에 예측 결과를 보여줍니다."

def process_and_render(img):
    # 이미지 예측
    results = model(img)

    # 원본 이미지 받아오기
    img_pil = Image.fromarray(img.astype('uint8'))
    draw = ImageDraw.Draw(img_pil)

    # 바운딩 박스만 그리기
    for det in results.pred[0]:
        x1, y1, x2, y2 = map(int, det[:4])
        draw.rectangle([x1, y1, x2, y2], outline="red", width=5)

    return img_pil

gr.Interface(inputs="image",
             outputs="image",
             fn=process_and_render,
             title=title,
             description=desc).launch()
