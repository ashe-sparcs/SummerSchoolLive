from django.contrib import admin
from .models import *
from django import forms


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year']
    list_display_links = ['id', 'title']


class ImportantDateAdmin(admin.ModelAdmin):
    list_display = ['id', 'academic_schedule', 'date']
    list_display_links = ['id', 'academic_schedule', 'date']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_type', 'course_no', 'course_title', 'professor']
    list_display_links = ['id', 'course_no', 'course_title']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'title', 'year']
    list_display_links = ['id', 'title']


class QuestionAndAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'question']
    list_display_links = ['id', 'number', 'question']


class MyReviewChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.title


class MyReviewForm(forms.ModelForm):
    review = MyReviewChoiceField(queryset=Review.objects.all())

    class Meta:
        model = ReviewImage
        fields = ['content', 'review']


class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'get_review_title']
    list_display_links = ['id', 'get_review_title']
    form = MyReviewForm


# Register your models here.
admin.site.register(Review, ReviewAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ReviewImage, ReviewImageAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ImportantDate, ImportantDateAdmin)
admin.site.register(QuestionAndAnswer, QuestionAndAnswerAdmin)
