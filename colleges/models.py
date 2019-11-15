# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class College(models.Model):

    collegeName = models.CharField(max_length=200, null=False)
    collegeAddress = models.CharField(max_length=200, null=False)

    # add more attributes
