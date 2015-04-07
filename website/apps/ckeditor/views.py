from datetime import datetime
import os
import uuid
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from ckeditor import image_processing
from ckeditor import utils

from fileupload.models import File


class ImageUploadView(generic.View):
    http_method_names = ['post']

    def post(self, request, **kwargs):
        """
        Uploads a file and send back its URL to CKEditor.
        """
        # Get the uploaded file from request.
        upload = request.FILES['upload']

        #Verify that file is a valid image
        backend = image_processing.get_backend()
        try:
            backend.image_verify(upload)
        except utils.NotAnImageException:
            return HttpResponse("""
                       <script type='text/javascript'>
                            alert('Invalid image')
                            window.parent.CKEDITOR.tools.callFunction({0});
                       </script>""".format(request.GET['CKEditorFuncNum']))

        f = File(file=upload)
        f.save()

        # Respond with Javascript sending ckeditor upload url.
        return HttpResponse("""
        <script type='text/javascript'>
            window.parent.CKEDITOR.tools.callFunction({0}, '{1}');
        </script>""".format(request.GET['CKEditorFuncNum'], f.file.url))

upload = csrf_exempt(ImageUploadView.as_view())


def get_files_browse_urls(user=None):
    files = []
    items = File.objects.all()
    for f in items:
        thumb = unicode('{0}_thumb{1}').format(*os.path.splitext(f.file.url));
        files.append({
            'thumb': thumb if os.path.isfile(thumb) else f.file.url,
            'src': f.file.url,
            'is_image': is_image(f.file.url),
            'is_movie': is_movie(f.file.url)
        })
    return files


def is_image(path):
    ext = path.split('.')[-1].lower()
    return ext in ['jpg', 'jpeg', 'png', 'gif', 'svg']

def is_movie(path):
    ext = path.split('.')[-1].lower()
    return ext in ['mp4', 'webm']

def browse(request):
    context = RequestContext(request, {
        'files': get_files_browse_urls(request.user),
    })
    return render_to_response('browse.html', context)

def get_image_files():
    files = []
    items = File.objects.all()
    for f in items:
        if (is_image(f.file.url)):
            files.append(f.file.path)
    return files