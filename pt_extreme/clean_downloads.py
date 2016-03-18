#!/usr/bin/python
import django
django.setup()
from uploader.models import Document


def main():
    print [x for x in Document.objects.all()]
    map(lambda x: x.delete(), [x for x in Document.objects.all()])
    print [x for x in Document.objects.all()]

if __name__ == '__main__':
    main()
