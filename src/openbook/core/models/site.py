# OpenBook: Interactive Online Textbooks - Server
# © 2024 Dennis Schulmeister-Zimolong <dennis@wpvs.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

from django.db                import models
from django.utils.translation import gettext_lazy as _
from ..utils.models           import calc_file_path

class Site(models.Model):
    """
    Custom version of Django's built-in Site model with some custom fields.
    """
    # Basic site data
    id         = models.PositiveIntegerField(verbose_name=_("Id"), primary_key=True, editable=True)
    domain     = models.CharField(verbose_name=_("Domain Name"), max_length=100)
    name       = models.CharField(verbose_name=_("Display Name"), max_length=255)
    short_name = models.CharField(verbose_name=_("Short Name"), max_length=50)
    about_url  = models.URLField(verbose_name=_("Information Website"), help_text=_("URL of your website with information for your users"))

    # Icon
    def _calc_file_path(self, filename):
        return calc_file_path(self._meta, self.id, filename)

    # Django meta information
    class Meta:
        verbose_name        = _("Website")
        verbose_name_plural = _("Websites")

    def __str__(self):
        return self.name
