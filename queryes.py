import django
import os
from django.db.models import Count

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train.models import Author

    # TODO Сделайте здесь запросы
    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
    #
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)
    # print(Entry.objects.filter(headline__contains='мод'))
    # print(Author.objects.filter(gender='ж'))
    print(Author.objects.annotate(num_entries=Count('entries')).order_by('-num_entries')[:1])













