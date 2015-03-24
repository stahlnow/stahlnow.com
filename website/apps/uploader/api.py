import base64
import os
import mimetypes
from django.core.files.uploadedfile import SimpleUploadedFile
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie.fields import FileField
from tastypie.authorization import Authorization
from uploader.models import File


class Base64FileField(FileField):

    """
    A django-tastypie field for handling file-uploads through raw post data.
    It uses base64 for en-/decoding the contents of the file.
    Usage:

    class MyResource(ModelResource):
        file_field = Base64FileField("file_field")

        class Meta:
            queryset = ModelWithFileField.objects.all()

    In the case of multipart for submission, it would also pass the filename.
    By using a raw post data stream, we have to pass the filename within our
    file_field structure:

    file_field = {
        "name": "myfile.png",
        "file": "longbas64encodedstring",
        "content_type": "image/png" # on hydrate optional
    }

    Your file_field will by dehydrated in the above format if the return64
    keyword argument is set to True on the field, otherwise it will simply
    return the URL.
    """

    def __init__(self, **kwargs):
        print "init"
        self.return64 = kwargs.pop('return64', False)
        super(Base64FileField, self).__init__(**kwargs)

    def _url(self, obj):
        instance = getattr(obj, self.instance_name, None)
        try:
            url = getattr(instance, 'url', None)
        except ValueError:
            url = None
        return url

    def dehydrate(self, bundle, **kwargs):
        print "dehydrate"
        if not self.return64:
            print self._url(bundle.obj)
            return self._url(bundle.obj)
        else:
            if (not self.instance_name in bundle.data
                    and hasattr(bundle.obj, self.instance_name)):
                file_field = getattr(bundle.obj, self.instance_name)
                if file_field:
                    content_type, encoding = mimetypes.guess_type(
                        file_field.file.name)
                    b64 = open(
                        file_field.file.name, "rb").read().encode("base64")
                    ret = {"name": os.path.basename(file_field.file.name),
                           "file": b64,
                           "content-type": (content_type or
                                            "application/octet-stream")}
                    return ret
            return None

    def hydrate(self, obj):
        print "hydrate"
        value = super(Base64FileField, self).hydrate(obj)
        if value and isinstance(value, dict):
            print value["name"]
            return SimpleUploadedFile(value["name"],
                                      base64.b64decode(value["file"]),
                                      value.get("content_type",
                                                "application/octet-stream"))
        elif isinstance(value, basestring):
            if value == self._url(obj.obj):
                return getattr(obj.obj, self.instance_name).name
            return value
        else:
            return None


class FileResource(ModelResource):

    file = Base64FileField()

    class Meta:
        queryset = File.objects.all()
        resource_name = 'uploader/file'
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        always_return_data = True
        api_name = 'v1'  # settings.API_VERSION

        ordering = ['created']

        filtering = {
            'name': ALL_WITH_RELATIONS,
        }
