from .models import Movie, Category


def star_movie(request):
    return {'stars': Movie.objects.filter(is_star=True)}


def cat_menu(request):
    return {'category': Category.objects.all()}
