import util
from libs import textprocessing

def MainPage(request):
    return util.request.print_html('System Working!')

def tp(request):    
    text = request.GET.get('text', None)
    return util.json.JSONResponse(textprocessing.adapter.query(text))
