#_*_coding:utf-8_*_
from django.http import HttpResponse

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print("in middle ware....",response)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self,request, view_func, view_args, view_kwargs):
        print("process view:", request, view_func, view_args, view_kwargs)


    def process_exception(self,request, exception):
        print("process exception",self,request,exception)

        return HttpResponse("err happend..")
    def process_template_response(self,request, response):
        print("process_template_response", self, request, response)


        return response