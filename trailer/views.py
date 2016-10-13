from trailer.models import Video
from django.shortcuts import render_to_response, HttpResponseRedirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def video_list_view(requset):
    video_list = Video.objects.all()
    video = video_list[0]
    url = '/video_index/'

    print video.video_name
    return render_to_response("video_list.html", {"video_list":video_list, "first_video":video, 'url':url})

@csrf_exempt
def video_detail_view(request, video_id):
    url = '/video_index/'

    try:
        video = Video.objects.get(id=video_id)
    except Video.DoesNotExist:
        video = None
    return render_to_response("video_detail.html", {"video":video, "url":url})

@csrf_exempt
def check_product_info_view(request):
    video_id = request.POST.get('videoId', '')
    current = request.POST.get('current', '')
    response_data = {}
    if video_id != '':
        print video_id
        response_data['result'] = 'success'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
