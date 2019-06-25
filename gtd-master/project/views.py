from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import FormQuestions


@method_decorator(staff_member_required, name='dispatch')
class BgCreate(CreateView):
    model = FormQuestions
    fields = ['gm_name', 'product_type', 'assigned_by']
    success_url = "http://127.0.0.1:8000/todo/"


class BgUpdate(UpdateView):
    model = FormQuestions
    fields = ['question1', 'question2', 'question3', 'question4', 'question5']
    success_url = "http://127.0.0.1:8000/todo/mine/"


class BgView(generic.ListView):
    template_name = 'my_forms.html'
    context_object_name = 'all_forms'

    def get_queryset(self):
        return FormQuestions.objects.filter(gm_name=self.request.user.username, editable='Yes')



