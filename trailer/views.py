from trailer.models import Video
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def video_list_view(requset):
    video_list = Video.objects.all()
    video = video_list[0]

    print video.video_name
    return render_to_response("video_list.html", {"video_list":video_list, "first_video_path":video.video_path,})

