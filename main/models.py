from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Gallery(models.Model):
    img = models.ImageField(("Gallery"), upload_to='gallery')


class Faculty(models.Model):
    name = models.CharField(("Name"), max_length=50)
    img = models.ImageField(("Faculty image"), upload_to='faculty')
    des = models.CharField(("Designation"), max_length=50)

    def __str__(self):
        return self.name


class Event(models.Model):
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    title = models.CharField(("Title"), max_length=250)
    shortdis = models.CharField(("Short Discription"), max_length=200)
    content = RichTextField()
    img = models.ImageField(("image"), upload_to="events")
    date = models.DateField(("Date"), auto_now=False, auto_now_add=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Newsletter(models.Model):
    email = models.EmailField(("Email"), max_length=254,blank=True)
    def __str__(self):
        return self.email



class placements(models.Model):
    img = models.ImageField(("image"), upload_to="placements")


class studentachi(models.Model):
    name = models.CharField(("Name"), max_length=50)
    file = models.FileField(("PDF"), upload_to='studentpdf', max_length=100)

    def __str__(self):
        return self.name


class teacherachi(models.Model):
    name = models.CharField(("Name"), max_length=50)
    designation = models.CharField(("Designation"), max_length=50)
    file = models.FileField(("PDF"), upload_to='studentpdf', max_length=100)

    def __str__(self):
        return self.name


class testmonials(models.Model):
    name= models.CharField(("Name"), max_length=50)
    Profession= models.CharField(("Profession"), max_length=50)
    dis = models.TextField(("content"))
    img = models.ImageField(("image"), upload_to='testmonial')
    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    phone = models.CharField(("Mobile number"), max_length=50)
    place = models.CharField(("Place"), max_length=250)
    course = models.CharField(("Course"), max_length=50)

    def __str__(self):
        return self.name


class contactus(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.EmailField(("Email"), max_length=254,blank=True)
    subject = models.CharField(("Subject"), max_length=250)
    Message = models.TextField(("Message"))

    def __str__(self):
        return self.name