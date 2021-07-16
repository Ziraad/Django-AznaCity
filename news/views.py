from ckeditor_uploader.forms import SearchForm
from django.shortcuts import render, get_object_or_404


# Create your views here.
from city.forms import CommentForm
from city.models import IpClass
from city.views import get_client_ip
from news.models import News, Category

category = Category.objects.all()


def news_detail_page(request, slug, sub_slug, title):
    # print('slug', slug)
    # print('sub_slug', sub_slug)
    # print("title: ", title)
    try:
        news = get_object_or_404(News, category__parent__slug=slug, category__slug=sub_slug, slug=title)
        comments = news.comments.filter(news__slug=title, is_access=True).order_by('-submit_date')

        ip = get_client_ip(request)
        # print('news: ', news)

        if not IpClass.objects.filter(ip=ip).exists():
            IpClass.objects.create(ip=ip)

        news.views.add(IpClass.objects.get(ip=ip))

        new_comment = None
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.news = news
                new_comment.save()
        else:
            comment_form = CommentForm()

        # search_form = SearchForm(data=request.GET)
        comment = news.comments.all
        context = {
            'news': news,
            'category': category,

            'comments': comments,
            'comment': comment,
            'new_comment': new_comment,
            'comment_form': comment_form,
            # 'search_form': search_form,
            # 'advertising': advertising,
            # 'is_liked': is_liked,
            # 'total_likes': news.total_likes(),
        }

        is_liked = False
        ip = get_client_ip(request)
        # get_comment = comments.likes.all()
        ip_object = IpClass.objects.get(ip=ip)
        target = news.comments.filter()
        print('ip_object', ip_object)
        print('target', target)
        try:
            # if news.comments.filter(likes__ip=IpClass.objects.get(ip=ip)).exists():
            if news.comments.filter(id=IpClass.objects.get(ip=ip).id).exists():
                print('exists')
                is_liked = True
            else:
                print('not exists')
                is_liked = False
            context['is_liked'] = is_liked
        except:
            print('error received')

        # search_form_method(request, context)

        return render(request, 'news/news-detail_page.html', context=context)
    except:
        return render(request, 'city/404_page.html')
