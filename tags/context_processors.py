from .models import Tag

def menu_link(request):
    links = Tag.objects.all()
    return dict(links=links)