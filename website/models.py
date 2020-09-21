from django.db import models
from tinymce.models import HTMLField

# Create your models here.






class Presentation(models.Model):

    logo = models.ImageField(upload_to="logo/Presentation")
    nom = models.CharField(max_length=255)
    description = models.TextField()
    message_welcome = HTMLField('Content')


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.nom






class Infosite(models.Model):
    """Model definition for Infosite."""

    # TODO: Define fields here
    nom = models.CharField(max_length=100)
    adress = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    numero = models.PositiveIntegerField()
    site = models.URLField()
    image = models.ImageField(upload_to="images/infosite")
    message = HTMLField('Content')



    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Infosite."""

        verbose_name = 'Infosite'
        verbose_name_plural = 'Infosites'

    def __str__(self):
        """Unicode representation of Infosite."""
        return self.nom
