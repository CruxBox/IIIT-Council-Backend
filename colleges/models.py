# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class College(models.Model):

	collegeName = models.CharField(null=False)
	collegeAddress = models.CharField(null=False)
