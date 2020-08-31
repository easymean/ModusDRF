from django.db import models
from common import models as common_models


class Somm(common_models.Common):
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_auth = models.BooleanField(default=False)
