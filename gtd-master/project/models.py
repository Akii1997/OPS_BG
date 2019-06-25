from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from todo.models import Task, TaskList
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings


Property_CHOICES = (
    ('all', 'All'),
    ('townhouse', 'TownHouse'),
    ('collection_o', 'Collection O'),
    ('flagship', 'Flagship'),
    ('silver_key', 'Silver Key'),
)
question_type = (
    ('Yes or No type', 'yes_no'),
    ('Integer Type', 'number'),
    ('Others', 'others'),
)
answer_type = (
    ('yes', 'Yes'),
    ('no', 'No'),
)


class Questions(models.Model):
    question = models.CharField(max_length=2500, default='Please type Question', unique=True)

    def __str__(self):
        return str(self.id) + " - " + self.question


class StandardAnswer(models.Model):
    question_name = models.ForeignKey(Questions, on_delete=models.CASCADE)
    question = models.CharField(max_length=2500, default='Please type Question')
    property_type = models.CharField(max_length=50, choices=Property_CHOICES, default='all')
    answer_choice = models.CharField(max_length=3, choices=answer_type, default='yes')
    task_name = models.CharField(max_length=500, default='Task Heading')
    task_description = models.CharField(max_length=1000, default='Task Description')
    task_deadline_expected = models.IntegerField(default=2, verbose_name=_('Number of Days for task completion'))
    priority = models.PositiveIntegerField(default=5, verbose_name=_('Priority as a number between 1 to 5'))

    def __str__(self):
        return self.property_type + " - " + str(self.question_name)


class FormQuestions(models.Model):
    all_users = User.objects.filter(is_staff=False)
    all_user_choices = ((x.username, x.username) for x in all_users)
    user_default = User.objects.get(username='12345').username
    all_creators = User.objects.filter(is_staff=True)
    all_user_choices_creators = ((x.username, x.username) for x in all_creators)
    user_default_creator = User.objects.get(username='Akash').username
    question1 = models.CharField(max_length=3, choices=answer_type, default='no', verbose_name=_('1st question'))
    question2 = models.CharField(max_length=3, choices=answer_type, default='no', verbose_name=_('2nd question'))
    question3 = models.CharField(max_length=3, choices=answer_type, default='no', verbose_name=_('3rd question'))
    question4 = models.CharField(max_length=3, choices=answer_type, default='no', verbose_name=_('4th question'))
    question5 = models.CharField(max_length=3, choices=answer_type, default='no', verbose_name=_('5th question'))
    gm_name = models.CharField(max_length=50, choices=all_user_choices, default=user_default, verbose_name=_('GM Name'))
    product_type = models.CharField(max_length=30, choices=Property_CHOICES, default='TownHouse',
                                    verbose_name=_('OYO Product'))
    assigned_by = models.CharField(max_length=50, choices=all_user_choices_creators, default=user_default_creator,
                                   verbose_name=_("Assigned By"))
    editable = models.CharField(max_length=10, choices=answer_type, default='Yes')

    def get_absolute_url(self):
        return reverse('BgCreate')

    def __str__(self):
        return str(self.id)

    def __init__(self, *args, **kwargs):
        super(FormQuestions, self).__init__(*args, **kwargs)
        self.old_question1 = self.question1

    def save(self, *args, **kwargs):
        if self.old_question1 != self.question1:
            self.editable = 'No'
            for value in self._meta.get_fields():
                if value.name.lower() in ['id', 'editable', 'gm_name', 'product_type', 'assigned_by']:
                    pass
                else:
                    std = StandardAnswer.objects.get(property_type=self.product_type,
                                                     question=value.verbose_name)
                    if getattr(std, "answer_choice").lower() == getattr(self, value.name).lower():
                        pass
                    else:
                        Task(title=value.verbose_name, task_list=TaskList.objects.get(name='OPS BG TASKS'),
                             due_date=timezone.now()+timedelta(days=std.task_deadline_expected),
                             created_by=User.objects.get(username=self.assigned_by),
                             assigned_to=User.objects.get(username=self.gm_name),
                             priority=std.priority).save()
            subject = 'BG FORM Filled by - ' + self.gm_name
            message = 'Hi ' + self.assigned_by + ',\nBG Form assigned to ' + \
                      self.gm_name + ' has benn filled at - ' + str(timezone.now()) + "\n\nFrom - Admin"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [User.objects.get(username=self.assigned_by).email]
            send_mail(subject, message, email_from, recipient_list)
        else:
            subject = 'BG FORM Assigned by - ' + self.assigned_by
            message = 'Hi ' + self.gm_name + ',\nBG Form assigned to you by ' + \
                      self.assigned_by + "\n\nFrom - Admin"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [User.objects.get(username=self.gm_name).email]
            send_mail(subject, message, email_from, recipient_list)
        super(FormQuestions, self).save(*args, **kwargs)

