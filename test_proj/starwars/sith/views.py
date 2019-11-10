from django.views.generic import FormView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import formset_factory
from django.core.mail import send_mail
from urllib import parse

from starwars.sith.forms import RecruterForm, AnswerForm
from starwars.sith.models import Question, TestExam, Recruter, Sith


class RecruterView(FormView):

    template_name = 'recruter.html'
    form_class = RecruterForm

    def form_valid(self, form):
        recruter = form.save()
        return redirect('answer', recruter_id=recruter.id)


class AnswerView(View):
    template_name = 'question.html'

    def get(self, request, recruter_id):
        exam = TestExam.objects.first()
        questions = Question.objects.filter(test_exam=exam)
        recruter = get_object_or_404(Recruter, id=recruter_id)
        AnswerFormSet = formset_factory(AnswerForm, extra=0)

        formset = AnswerFormSet(initial=[
            {'question': q, 'recruter': recruter} for q in questions])

        return render(request, self.template_name, context={'formset': formset})

    def post(self, request, recruter_id=None):
        AnswerFormSet = formset_factory(AnswerForm)
        formset = AnswerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
        return redirect('index')


class ChooseSithView(View):

    template_name = 'choosesith.html'

    def get(self, request):
        siths = Sith.objects.order_by('name')

        return render(request, self.template_name, context={'siths': siths})


class SithView(View):

    template_name = 'sith.html'

    def get(self, request):
        recruters = Recruter.objects.filter(is_shadow_hand=False,
                                            answers__isnull=False).distinct()
        current_url = request.build_absolute_uri()
        sith_id = parse.parse_qs(parse.urlparse(current_url).query)['sith_id'][0]

        return render(request, self.template_name, context={'recruters': recruters,
                                                            'sith_id': sith_id})


class AllSithsView(View):

    template_name = 'allsiths.html'

    def get(self, request):
        siths = Sith.objects.order_by('name')
        for sith in siths:
            recruters = Recruter.objects.filter(is_shadow_hand=True, sith=sith.id).count
            sith.recruters_count = recruters

        return render(request, self.template_name, context={'siths': siths})


class SithsMore1View(View):

    template_name = 'sithsmore1.html'

    def get(self, request):
        siths = Sith.objects.order_by('name')
        for sith in siths:
            recruters = Recruter.objects.filter(is_shadow_hand=True, sith=sith.id).count
            sith.recruters_count = recruters

        return render(request, self.template_name, context={'siths': siths})


class EnrollRecruterView(View):
    def get(self, request, recruter_id, sith_id):
        sith = Sith.objects.get(id=sith_id)
        recruter = get_object_or_404(Recruter, id=recruter_id)
        recruter.is_shadow_hand = True
        recruter.sith = sith
        recruter.save()
        send_mail(
            'Сообщение от Ситха',
            'Вы зачислены в Руку тени',
            'from@sith.com',
            [recruter.email],
            fail_silently=False,
        )
        return redirect('index')
