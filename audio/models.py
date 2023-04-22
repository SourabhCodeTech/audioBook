from django.db import models

# Create your models here.
class AudioBookName(models.Model):
    audioBookId = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=255)
    audiobookName = models.CharField(max_length=255)
    audioBookImage = models.ImageField(upload_to='ImageUpload/')

    def __str__(self):
        return self.audiobookName


class Audio(models.Model):
    # audioId = models.IntegerField(primary_key=True)
    audioName = models.CharField(max_length=255)
    audioFile = models.FileField(upload_to='AudioUpload/')
    bookName = models.ForeignKey(AudioBookName, on_delete=models.CASCADE, related_name="audio")

    def __str__(self):
        return self.audioName
    


