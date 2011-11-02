from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from .utils import get_identier
from .managers import RatingManager


class Rating(models.Model):
    user = models.ForeignKey(User)
    rated_object_id = models.PositiveIntegerField()
    rated_object_ctype = models.ForeignKey(ContentType)
    rating = models.FloatField(blank=False, null=False)

    objects = RatingManager()

    def __unicode__(self):
        return u"Rating"

    def rated_object_identifier(self):
        return get_identier(self)
