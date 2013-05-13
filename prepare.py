from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from tastypie.models import ApiKey

a = User.objects.all()[0]
a.first_name = 'Ashier'
a.last_name = 'de Leon'
a.save()

s = Site.objects.all()[0]
s.domain = 'ashier.local:8000'
s.name = 'ashier.local:8000'
s.save()

api = ApiKey.objects
api.create(user=a)
