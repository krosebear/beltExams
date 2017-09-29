# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..main.models import User
from django.db import models


class Poke(models.Model):
    receive = models.ForeignKey(User, related_name="gotPoke")
    give = models.ForeignKey(User, related_name="gavePoke")
