from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect

from openvino_api.app import main


@csrf_exempt
def StartApp(request):
    if request.method == 'POST':
        image = request.FILES['file']
        print(image)
        type = request.POST['optradio']
        print(type)
        # try:
        #     image = request.FILES['image']
        # except MultiValueDictKeyError:
        #     return HttpResponse("incorrect image provided !!!")
        # try:
        #     type = request.POST['type']
        # except MultiValueDictKeyError:
        #     return HttpResponse("incorrect type provided !!!")

        if type == 'TEXT':
            model = "/models/text-detection-0004.xml"

        elif type == 'CAR_META':
            model = "/models/vehicle-attributes-recognition-barrier-0039.xml"

        elif type == 'POSE':
            model = "/models/human-pose-estimation-0001.xml"
        else:
            return render(request, "home.html")
        fs = FileSystemStorage()
        fs.save(image.name, image)
        res = main(image, type, model)
        request.session['picture'] = res
        return redirect('/feedback')
    return render(request, "home.html")

@csrf_exempt
def feedback(request):
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url == None:
        return redirect('/')
    if request.method == 'POST':
        message = request.POST['message']
        message = str(message)
        feedback = open("static/feedback.txt", "a+")
        feedback.write(message+"\n\n")
        feedback.close()
        return redirect('/')
    picture = request.session.get('picture')
    return render(request, "feedback.html", {"picture": picture})