from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video
from ai.app import process_and_render
from django.conf import settings
import os
def main(request):
    video_path = '/videos/original.mp4/' #비디오 파일 경로
    context = {
        'video': video_path,
        'MEDIA_URL': settings.MEDIA_URL,
    }        
    return render(request, 'coip/main.html', context)

def main2(request):
    video_path = '/videos/detected.mp4/'  # 비디오 파일 경로
    context = {
        'video': video_path,
        'MEDIA_URL': settings.MEDIA_URL,
    }        
    return render(request, 'coip/main2.html', context)

def team(request):
    return render(request, 'coip/team.html')

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return redirect('result_video', video_id=video.id)  # 저장된 비디오의 ID를 전달
    else:
        form = VideoForm()
    return render(request, 'coip/upload_video.html', {'form': form})

def result_video(request, video_id):
    video = Video.objects.get(id=video_id)
    if video:
        # video.video_file.path로 파일 경로 얻기
        processed_image_path = process_and_render(video.video_file.path)  
        context = {
            'file_data': video.video_file,
            'processed_data_url': os.path.join(settings.MEDIA_URL, 'temp', 'processed_image.jpg'),
        }
        return render(request, 'coip/result_video.html', context)
    else:
        return redirect('upload_video')