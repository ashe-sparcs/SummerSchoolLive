from django.db import models
import os
import datetime


# Create your models here.
class Review(models.Model):
    student = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    content = models.TextField()


class Image(models.Model):
    title = models.CharField(max_length=100, default='Photo')
    year = models.IntegerField()
    content = models.FileField(upload_to='media/image')

    def get_filename(self):
        return os.path.basename(self.content.name)


class ReviewImage(models.Model):
    content = models.FileField(upload_to='media/review_image')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def get_filename(self):
        return os.path.basename(self.content.name)

    def get_review_title(self):
        return self.review.title


class Course(models.Model):
    course_type = models.IntegerField(default=1)
    course_no = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    credit = models.IntegerField(default=3)
    professor = models.CharField(max_length=50)
    syllabus = models.FileField(upload_to='media/syllabus')
    is_edu_3 = models.BooleanField(default=False)

    def get_filename(self):
        return os.path.basename(self.syllabus.name)


class ImportantDate(models.Model):
    academic_schedule = models.CharField(max_length=100)
    date = models.CharField(max_length=50)


class QuestionAndAnswer(models.Model):
    number = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
