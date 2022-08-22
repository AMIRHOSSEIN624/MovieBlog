from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie, Comment, Category
from .forms import CommentForm
from django.http import HttpResponseRedirect


class ListMovie(generic.ListView):
    model = Movie
    template_name = 'pages/home.html'
    paginate_by = 4
    context_object_name = 'movies'


def detail_page(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    # 'comment code

    comment = movie.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.movie = movie
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    # comment code
    return render(request, 'pages/detail_page.html',
                  {'movie': movie, 'comments': comment, 'comment_form': comment_form})


def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.like.filter(id=request.user.id).exists():
        comment.like.add(request.user)
        comment.dislike.remove(request.user)
    else:

        comment.like.add(request.user)
        comment.dislike.remove(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comment_dislike(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.dislike.filter(id=request.user.id).exists():
        comment.dislike.add(request.user)
        comment.like.remove(request.user)
    else:

        comment.dislike.add(request.user)
        comment.like.remove(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def category_filter(request, pk):
    movie = Movie.objects.filter(genre=pk)
    return render(request, 'pages/category_filter.html', {'movies': movie})
