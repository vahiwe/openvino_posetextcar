import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from openvino_api.settings import BASE_DIR


@csrf_exempt
def StartApp(request):
    # i = request.POST['i']
    # m = request.POST['m']
    # t = request.POST['t']
    # c = request.POST['c']
    # d = request.POST['d']
    image_url = str(BASE_DIR + "/images/carred.jpg")
    print(image_url)
    # TODO CHANGE THIS ACCORDING TO YOUR FOLDERS POSITION
    res = os.system('python app.py -i "/home/mohitp/learning/openvino_posetextcar/images/carred.jpg" -t "CAR_META" -m '
                    '"/home/mohitp/learning/openvino_posetextcar/models/vehicle-attributes-recognition-barrier-0039'
                    '.xml" -c '
                    '"/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"')

    return HttpResponse(res)
