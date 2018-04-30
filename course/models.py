from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


FIRST = '1'
SECOND = '2'
THIRD = '3'
FORTH = '4'
FIFTH = '5'
SIXTH = '6'
SEVENTH = '7'
EIGHTH = '8'

SEMESTER = (
    (FIRST,'First'),
    (SECOND,'Second'),
    ( THIRD,'Third',),
    ( FORTH,'Forth'),
    ( FIFTH,'Fifth'),
    ( SIXTH,'Sixth'),
    ( SEVENTH, 'Seventh'),
    ( EIGHTH,'Eighth'),
)


class Subject(models.Model):
    """
    """
    department =models.ForeignKey(Department, on_delete=models.PROTECT)
    semester = models.CharField(max_length=2, choices=SEMESTER)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    image = models.ImageField(upload_to='Subject/', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='subject_creaded_by', on_delete=models.SET(0))
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='subject_updated_by', on_delete=models.SET(0))

    def __str__(self):
        return '{} : {} : {}'.format(self.name, self.code , self.semester)

    def sub_image(self):
        return (u'<img src="{}" style="width:100px;height:100px;"/>'.format(self.image.url))
    sub_image.short_description = 'Image'
    sub_image.allow_tags = True


class Note(models.Model):
    """
    """
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    author = models.CharField(max_length=200)
    college = models.CharField(max_length=200, null=True, blank=True)
    note_upload = models.FileField(upload_to='Note/')
    download = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='note_creaded_by', on_delete=models.SET(0))
    updated_by = models.ForeignKey(User, null=True, blank=True, related_name='note_updated_by', on_delete=models.SET(0))

    def __str__(self):
        return 'Subject: {} Author: {}'.format(self.subject.name, self.author)


class Rating(models.Model):
    """
    """
    user = models.ForeignKey(User, on_delete=models.SET(0))
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ['user', 'note']

    def __str__(self):
        return 'Subject: {} User: {} Rating: {}'.format(self.note.subject.name, self.user.username, self.count)
