import datetime
import os

from django.http import HttpResponse

from app import main


def StartApp(request):
    # i = request.POST['i']
    # m = request.POST['m']
    # t = request.POST['t']
    # c = request.POST['c']
    # d = request.POST['d']
    res = os.system('python app.py -i "images/blue-car.jpg" -t "CAR_META" -m '
                    '"/home/workspace/models/vehicle-attributes-recognition-barrier-0039.xml" -c '
                    '"/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"')

    return HttpResponse(res)
