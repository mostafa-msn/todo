from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserProfile(models.Model):
    DEVELOPER = 1
    PROJECT_MANAGER = 2
    ROLE_CHOICES = (
        (DEVELOPER, _("Developer")),
        (PROJECT_MANAGER, _("Project Manager")),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(_("Role"), choices=ROLE_CHOICES, default=DEVELOPER)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profile")

    def __str__(self):
        return self.user.username
