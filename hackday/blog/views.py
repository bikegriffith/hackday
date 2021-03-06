from blog.models import Entry, STATUS
from django.http import HttpResponse
from django.template import Context, loader


def index(request):
    latest_entries = Entry.objects.filter(status=STATUS.PUBLISHED).\
            order_by('-pub_date')[:5]

    t = loader.get_template('blog/index.html')
    c = Context({
        'latest_entries': latest_entries,
    })

    return HttpResponse(t.render(c))


def entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id, status=STATUS.PUBLISHED)

    t = loader.get_template('blog/entry.html')
    c = Context({
        'entry': entry,
    })

    return HttpResponse(t.render(c))


def category(request, slug):
    entries = Entry.objects.filter(categories__slug=slug,
            status=STATUS.PUBLISHED).order_by('pub_date')

    t = loader.get_template('blog/category.html')
    c = Context({
        'slug': slug,
        'entries': entries,
    })

    return HttpResponse(t.render(c))


def tag(request, slug):
    entries = Entry.objects.filter(tags__slug=slug,
            status=STATUS.PUBLISHED).order_by('pub_date')

    t = loader.get_template('blog/tag.html')
    c = Context({
        'slug': slug,
        'entries': entries,
    })

    return HttpResponse(t.render(c))
