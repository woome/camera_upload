from django.db import models
from django.contrib.auth.models import User
from os.path import splitext

IMAGE_SIZE = [300, 300]
THUMBNAIL_SIZE = [100, 100]
UPLOAD_TO="photos/%Y/%m/%d/%H/%M"

class Photo(models.Model):
    user = models.ForeignKey(User)
    shot = models.ImageField(upload_to=UPLOAD_TO)
    
    def __str__(self):
        return self.name
        
    def __unicode__(self):
        return self.name
        
    def save_file(self, uploaded_file):
        filename = uploaded_file.name
        basename, extension = splitext(filename)
        basename = self.user.username
        value = self.shot.save(basename + ".jpg", uploaded_file, save=False)
        return value

# End
