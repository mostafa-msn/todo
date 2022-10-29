from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50, blank=False, null=False)
    description = models.CharField(_("description"), max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ManyToManyField(User, verbose_name=_("assignee"), related_name="task_assignee")
    title = models.CharField(_("title"), max_length=50, blank=False, null=False)
    description = models.CharField(_("description"), max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.title
