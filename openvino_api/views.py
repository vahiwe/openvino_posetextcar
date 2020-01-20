from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from openvino_api.app import main


@csrf_exempt
def StartApp(request):
    try:
        image = request.FILES['image']
    except MultiValueDictKeyError:
        return HttpResponse("incorrect image provided !!!")
    try:
        type = request.POST['type']
    except MultiValueDictKeyError:
        return HttpResponse("incorrect type provided !!!")

    if type == 'TEXT':
        model = "/models/text-detection-0004.xml"

    elif type == 'CAR_META':
        model = "/models/vehicle-attributes-recognition-barrier-0039.xml"

    elif type == 'POSE':
        model = "/models/human-pose-estimation-0001.xml"
    else:
        return HttpResponse("wrong type")
    fs = FileSystemStorage()
    img = fs.save(image.name, image)
    main(img, type, model)
    return HttpResponse("Inference Successful")
