from django.db import models


class MyDocument(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="uploads/")
    converted_file = models.FileField(upload_to='converted/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def filename(self):
        return str(self.file).split('/')[-1]

    def converted_filename(self):
        if self.converted_file:
            return str(self.converted_file).split('/')[-1]
        return "Not Converted"
