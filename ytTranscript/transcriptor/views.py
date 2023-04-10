from django.shortcuts import render
from django.http import JsonResponse
from youtube_transcript_api import YouTubeTranscriptApi as yta 

def greet(request):
    name = request.GET.get('name', 'World')
    message = f'Hello, {name}!'
    return JsonResponse({'message': message})

def transcript(request):
    video_link = request.GET.get('video_link', 'https://www.youtube.com/watch?v=oZnc6GJJl_8&t=7s&ab_channel=Hayu')
    video_id = video_link[32:]

    data = yta.get_transcript(video_id)

    transcript = ''
    for value in data:
       for key,val in value.items():
            if key == 'text':
                transcript += val

    l = transcript.splitlines()
    final_transcript = " ".join(l)


    return JsonResponse({'transcript': final_transcript})
