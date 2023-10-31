# 일경험 프로젝트 2 - 제안 프로젝트

## Gradio 코드 돌리는 방법
1. conda를 통해 가상환경 생성
2. `pip install -r requirements.txt` 통해 라이브러리 설치
3. `app.py`의 `yolov5_path`와 model 변수의 `path`의 경로 설정
4. 실행
5. 예시 이미지는 `work2/aircraft-dataset/extras`에 있음
6. 현재 사용한 데이터셋에서 제공하는 데이터 이외에는 학습해보지 않은 상황

## 향후 계획
1. YOLOv5 학습량을 늘려서 정확도 개선
2. 차량 등의 클래스 추가하여 공항 활주로 내부의 지형지물 등에 대한 인식 개선