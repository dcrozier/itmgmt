<<<<<<< HEAD
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
=======
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
>>>>>>> a784ca2f5f897a81f4b4db13769e5b593e944234
