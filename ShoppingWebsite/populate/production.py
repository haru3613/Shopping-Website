from populate import base

from django.contrib.auth.models import User


print('Creating admin account ... ', end='')
User.objects.create_superuser(username='admin', password='azx9885798', email=None)
print('done')