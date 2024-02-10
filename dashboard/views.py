import json
from typing import Collection

from django.db.models import Avg, Count, F, FloatField, Max, Q, Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from calendar_app.models import Category, Event
from exam.models import Etapa, Exam

# Create your views here.
# Importante detalhe para o sistema funcionar de Dashboard deve haver no banco de dados: createsuperuser // --syncdb // alguma etapa // categorias dos eventos da calendário

class Dashboard(View):
    def get(self, request):
        exames_mes = []
        evento_mes = []
        lazer = []
        estudos = []
        trabalhos = []
        lazer = Category.objects.filter(
            name__icontains='lazer'
        )[0].categorias.all().count()
        estudos = Category.objects.filter(
            name__icontains='estudos'
        )[0].categorias.all().count()
        trabalhos = Category.objects.filter(
            name__icontains='trabalho'
        )[0].categorias.all().count()
        for month in range(1, 13):
            evento_mes.append(Event.objects.filter(
                start__month=month).count())
            exames_mes.append(Exam.objects.filter(
                start__month=month
            ).count())
        print(exames_mes,evento_mes)
        return render(request, 'dashboard.html', {
            'evento_mes': evento_mes,
            'exames_mes': exames_mes,
            "lazer":lazer,
            'estudos':estudos,
            'trabalhos':trabalhos
        })


class humanas(View):
    def get(self, request):
        etapa1 = Etapa.objects.filter(etapa=1)[0]
        etapa2 = Etapa.objects.filter(etapa=2)[0]
        etapa3 = Etapa.objects.filter(etapa=3)[0]
        notasGeo = Exam.objects.filter(
            subject='Geography',
            marks__gte=0,
            marks__isnull=False,

        ).aggregate(Sum('marks'))['marks__sum'] or 0
        notasHist = Exam.objects.filter(
            subject='History',
            marks__gte=0,
            marks__isnull=False,
        ).aggregate(Sum('marks'))['marks__sum'] or 0
        notasfilo = Exam.objects.filter(
            subject='Philosophy',
            marks__gte=0,
            marks__isnull=False,
        ).aggregate(Sum('marks'))['marks__sum'] or 0


        notasExamesEtapas = {
            'Geo': [etapa1.etapas.filter(marks__isnull=False, subject='Geography').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False,subject='Geography').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False,subject='Geography').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
            'Hist': [etapa1.etapas.filter(marks__isnull=False, subject='History').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False, subject='History').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False, subject='History').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
            'Filo': [etapa1.etapas.filter(marks__isnull=False, subject='Philosophy').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False, subject='Philosophy').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False, subject='Philosophy').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
        }

        return render(request,
                      'dashboard_humanas.html', {"notasfilo": notasfilo,
                                                 "notasGeo": notasGeo, 
                                                 "notasHist": notasHist,
                                                 "notasEtapaGeo":notasExamesEtapas['Geo'],
                                                 'notasEtapaHist':notasExamesEtapas['Hist'],
                                                 "notasEtapaFilo":notasExamesEtapas['Filo']})


class math_science(View):
    def get(self, request):
        etapa1 = Etapa.objects.filter(etapa=1)[0]
        etapa2 = Etapa.objects.filter(etapa=2)[0]
        etapa3 = Etapa.objects.filter(etapa=3)[0]
        notasMath = Exam.objects.filter(
            subject='Math',
            marks__gte=0,
            marks__isnull=False,

        ).aggregate(Sum('marks'))['marks__sum'] or 0
        notasPh = Exam.objects.filter(
            subject='Physics',
            marks__gte=0,
            marks__isnull=False,
        ).aggregate(Sum('marks'))['marks__sum'] or 0
        notasChem = Exam.objects.filter(
            subject='Chemistry',
            marks__gte=0,
            marks__isnull=False,
        ).aggregate(Sum('marks'))['marks__sum'] or 0
        notasBio = Exam.objects.filter(
            subject='Biology',
            marks__gte=0,
            marks__isnull=False,
        ).aggregate(Sum('marks'))['marks__sum'] or 0


        notasExamesEtapas = {
            'Math': [etapa1.etapas.filter(marks__isnull=False, subject='Math').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False,subject='Math').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False,subject='Math').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
            'Ph': [etapa1.etapas.filter(marks__isnull=False, subject='Physics').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False, subject='Physics').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False, subject='Physics').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
            'Chem': [etapa1.etapas.filter(marks__isnull=False, subject='Chemistry').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False, subject='Chemistry').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False, subject='Chemistry').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
            'Bio': [etapa1.etapas.filter(marks__isnull=False, subject='Biology').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False, subject='Biology').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False, subject='Biology').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
        }
        return render(request,
                      'math_science.html', {"notasMath": notasMath,
                                                 "notasPh": notasPh, 
                                                 "notasChem": notasChem,
                                                 "notasBio":notasBio,
                                                 "notasEtapas":notasExamesEtapas})



class languages(View):
    def get(self, request):
        etapa1 = Etapa.objects.filter(etapa=1)[0]
        etapa2 = Etapa.objects.filter(etapa=2)[0]
        etapa3 = Etapa.objects.filter(etapa=3)[0]
        notasPort = Exam.objects.filter(
            subject='Portguese',
            marks__gte=0,
            marks__isnull=False,

        ).aggregate(Sum('marks'))['marks__sum'] or 0
        notasPw = Exam.objects.filter(
            subject='Portuguese Writing',
            marks__gte=0,
            marks__isnull=False,
        ).aggregate(Sum('marks'))['marks__sum'] or 0
        notasEng = Exam.objects.filter(
            subject='Chemistry',
            marks__gte=0,
            marks__isnull=False,
        ).aggregate(Sum('marks'))['marks__sum'] or 0

        notasExamesEtapas = {
            'Port': [etapa1.etapas.filter(marks__isnull=False, subject='Portguese').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False,subject='Portguese').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False,subject='Portguese').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
            'Pw': [etapa1.etapas.filter(marks__isnull=False, subject='Portuguese Writing').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False, subject='Portuguese Writing').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False, subject='Portuguese Writing').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],
            'Eng': [etapa1.etapas.filter(marks__isnull=False, subject='English').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa2.etapas.filter(marks__isnull=False, subject='English').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0,
                    etapa3.etapas.filter(marks__isnull=False, subject='English').prefetch_related('marks').aggregate(Sum("marks"))['marks__sum'] or 0],

        }

        return render(request,
                      'languages.html', {"notasPort": notasPort,
                                                 "notasPw": notasPw, 
                                                 "notasEng": notasEng,
                                                 "notasEtapas":notasExamesEtapas})

