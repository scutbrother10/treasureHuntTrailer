from trailer.models import Video, Product
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
    current_time = request.POST.get('time', '')
    print(int(float(current_time)))
    try:
        video = Video.objects.get(id=video_id)
        products = Product.objects.filter(video = video, product_show_time = int(float(current_time)))
        print products
    except Video.DoesNotExist:
        video = None

    if products.exists:
        product = products[0]
    response_data = {}
    if video_id != '':
        response_data['result'] = 'success'
        response_data['product_name'] = product.product_name
        return HttpResponse(json.dumps(response_data), content_type="application/json")
