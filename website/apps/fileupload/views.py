import json
from django.http import HttpResponse
from django.views.generic import View, CreateView, DeleteView, ListView
from .models import File
from .response import JSONResponse, response_mimetype
from .serialize import serialize


class FileCreateView(CreateView):
    model = File

    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(
            content=data,
            status=400,
            content_type='application/json')


class FileDeleteView(DeleteView):
    model = File

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class FileListView(ListView):
    model = File

    def render_to_response(self, context, **response_kwargs):
        files = [serialize(p) for p in self.get_queryset()]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class JSONResponseMixin(object):

    def render_to_response(self, context, **response_kwargs):
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class FileHandlingView(View, JSONResponseMixin):
    def get(request, **kwargs):
        pass
    def post(request, **kwargs):
        pass
    def put(request, **kwargs):
        pass


    def delete(request, **kwargs):
        pass

    def render_to_response(self, context, **response_kwargs):
        response = Super().render_to_response(self, context, **response_kwargs)

        resonse.lalal =123

        return response


