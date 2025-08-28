from mixes.models import Mix
from .forms import BookingsForm
from django.contrib import messages
from .models import BioPage, Homepage
from django.shortcuts import render, redirect


def index(request):
    homepage = Homepage.objects.first()
    context = {
        'homepage': homepage,
        "bio": BioPage.objects.first(),
        'mixes': Mix.objects.all(),
        'title_tag': homepage.seo_title,
        'meta_keywords': homepage.seo_keywords,
        'meta_description': homepage.seo_description,
        'meta_thumbnail': homepage.get_meta_thumbnail,
    }
    return render(request, 'index.html', context)


def bio(request):
    bio = BioPage.objects.first()
    context = {
        'bio': bio,
        'title_tag': bio.seo_title,
        'meta_keywords': bio.seo_keywords,
        'meta_description': bio.seo_description,
        'meta_thumbnail': bio.get_meta_thumbnail,
        'bookings_form': BookingsForm(request.POST or None),
    }
    return render(request, 'bio.html', context)


def bookings(request):
    bookings_form = BookingsForm(request.POST or None)
    if request.method == 'POST':
        if bookings_form.is_valid():
            bookings_form.save()
            messages.success(request, 'Your message has been received.')
            return redirect('bookings')
        else:
            if bookings_form.errors:
                for field, errors in bookings_form.errors.items():
                    for error in errors:
                        messages.error(request, error)
    context = {
        'bookings_form': bookings_form,
        'meta_description': "Book Tophaz.",
        'title_tag': "Bookings • Tophaz | Official Website",
    }
    return render(request, 'bookings.html', context)
