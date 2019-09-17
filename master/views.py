from django.shortcuts import (render_to_response)
from django.template import RequestContext


# HTTPS Error 404
def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


# HTTPS Error 500
def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response


# HTTPS Error 403
def handler403(request, exception, template_name="403.html"):
    response = render_to_response("403.html")
    response.status_code = 403
    return response


# HTTPS Error 400
def handler400(request, exception, template_name="400.html"):
    response = render_to_response("400.html")
    response.status_code = 400
    return response
