# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django import forms
from StringIO import StringIO
from PIL import Image
from models import Photo

def create_photo(user, image):
    m = Photo(user=user)
    if image:
        image.seek(0)
    m.save_file(image)
    m.save()
    lookedup = Photo.objects.get(id=m.id)
    return lookedup


class PhotoForm(forms.Form):
    photo = forms.ImageField(label="photo", required=True)


def make_direct(request):
    """This takes a direct post from the jpgencoder

    I'm having trouble getting a good image out of the encoder, but
    there live test code seems to work well. So this is to test the
    Multipart stuff isn't getting in the way.
    """
    with open("/home/nferrier/woome/localcamera/siteapp/site/file.jpg", "wb") as fd:
        fd.write(request.raw_post_data)
    return HttpResponseNotFound()

def upload_image(request):
    user, created = User.objects.get_or_create(
        username="nicferrier",
        )
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        # Handle images uploaded
        try:
            photo = create_photo(
                user,
                form.cleaned_data['photo'], 
                )
            photo_path = photo.shot.url
            return HttpResponse("""<a href="/%s"/>""" % photo_path)
        except Exception, e:
            print e
    return HttpResponseServerError()

# End
