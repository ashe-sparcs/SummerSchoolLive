from django.shortcuts import render
from .models import *
from django.db.models import Q
import math


# Create your views here.
def home(request):
    context = {}
    review = Review.objects.filter(id=12)[0]
    # id=... 부분에 넣고 싶은 후기에 해당하는 id를 적어넣으시면됩니다. id는 admin page -> review에서 보실 수 있습니다.
    review_image = review.reviewimage_set.all()
    review_image_filename_list = [x.get_filename() for x in review_image[:2]]
    context['review'] = review
    context['filename_list'] = review_image_filename_list
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def base(request):
    context = {}
    return render(request, 'base.html', context)


def gallery(request, year, page_number):
    context = {}
    divider = 9
    page_number = int(page_number)
    year = int(year)
    if page_number < 1:
        page_number = 1
    if year == 0:
        image_list = Image.objects.all()
    else:
        image_list = Image.objects.filter(year=year)
    if 'search_word' in request.GET:
        search_word = request.GET['search_word']
        image_list = Image.objects.filter(title__icontains=search_word)
        context['search_word'] = search_word
    image_list = image_list.order_by('-id')
    image_list_length = image_list.count()
    max_page_number = math.ceil(image_list_length / divider)
    if page_number > max_page_number:
        page_number = max_page_number
    if image_list_length == 0:
        image_list_sliced = []
    else:
        image_list_sliced = image_list[(page_number - 1) * divider:min([page_number * divider, image_list_length])]
    image_title_filename_list = [(img.title, img.get_filename()) for img in image_list_sliced]
    if year == 0:
        context['year'] = 'all years'
    else:
        context['year'] = year
    context['image_title_filename_list'] = image_title_filename_list
    context['pages'] = [(x + 1) for x in range(max_page_number)]
    context['current_page'] = page_number
    context['previous_page'] = max([page_number - 1, 1])
    context['next_page'] = min([page_number + 1, len(context['pages'])])
    return render(request, 'gallery.html', context)


def faq(request):
    context = {}
    context['faq'] = QuestionAndAnswer.objects.all()
    return render(request, 'faq.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def review(request, page_number):
    context = {}
    page_number = int(page_number)
    if page_number < 1:
        page_number = 1
    if 'search_word' in request.GET:
        search_word = request.GET['search_word']
        query = Q(student__icontains=search_word) | Q(title__icontains=search_word) | Q(content__icontains=search_word)
        review_list = Review.objects.filter(query)
        context['search_word'] = search_word
    else:
        review_list = Review.objects.all()
    review_list = review_list.order_by('-id')
    review_list_length = review_list.count()
    max_page_number = math.ceil(review_list_length / 10)
    if page_number > max_page_number:
        page_number = max_page_number
    if review_list_length == 0:
        review_list_sliced = []
    else:
        review_list_sliced = review_list[(page_number-1)*10:min([page_number*10, review_list_length])]
    context['reviews'] = review_list_sliced
    context['pages'] = [(x+1) for x in range(max_page_number)]
    context['current_page'] = page_number
    context['previous_page'] = max([page_number - 1, 1])
    context['next_page'] = min([page_number + 1, len(context['pages'])])
    return render(request, 'review.html', context)


def review_one(request, number):
    context = {}
    review = Review.objects.filter(id=number)[0]
    review_image_list = review.reviewimage_set.all()
    review_image_name_list = [x.get_filename() for x in review_image_list]
    context['review'] = review
    context['review_image_name_list'] = review_image_name_list
    return render(request, 'review_one.html', context)


def dates(request):
    context = {}
    context['dates'] = ImportantDate.objects.all().order_by('id')
    return render(request, 'dates.html', context)


def track1(request):
    context = {}
    context['morning'] = Course.objects.filter(course_type=1)
    context['afternoon'] = Course.objects.filter(course_type=2)
    context['kschool'] = Course.objects.filter(course_type=3)
    return render(request, 'track1.html', context)


def track2(request):
    context = {}
    return render(request, 'track2.html', context)
