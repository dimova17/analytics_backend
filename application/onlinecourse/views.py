from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Institution, Platform, OnlineCourse, CourseCredit, CourseRequirement, CourseFieldOfStudy, \
    CourseLearningOutcome, CourseWorkProgram
from workprogramsapp.models import FieldOfStudy
from dataprocessing.models import Items

from .serializers import InstitutionSerializer, PlatformSerializer, OnlineCourseSerializer, \
    CourseCreditSerializer, CourseRequirementSerializer, CourseFieldOfStudySerializer, CourseLearningOutcomeSerializer,\
    CourseWorkProgramSerializer

from .data_onlinecourse import get_data


class InstitutionViewSet(viewsets.ModelViewSet):
    """Контроллер для модели Правообладатель"""
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']


class PlatformViewSet(viewsets.ModelViewSet):
    """Контроллер для модели Платформа"""
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']


class OnlineCourseViewSet(viewsets.ModelViewSet):
    """Контроллер для модели Онлайн курс"""
    queryset = OnlineCourse.objects.all()
    serializer_class = OnlineCourseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'platform__title', 'institution__title']
    ordering_fields = ['title', 'platform__title', 'institution__title', 'language', 'started_at', 'rating']
    filterset_fields = ['platform__title', 'institution__title', 'language']


class CourseCreditViewSet(viewsets.ModelViewSet):
    """Контроллер для модели Перезачет"""
    queryset = CourseCredit.objects.all()
    serializer_class = CourseCreditSerializer


class CourseRequirementViewSet(viewsets.ModelViewSet):
    """Контроллер для модели Требования для онлайн курса"""
    queryset = CourseRequirement.objects.all()
    serializer_class = CourseRequirementSerializer


class CourseFieldOfStudyViewSet(viewsets.ModelViewSet):
    """Контроллер для модели Требования для онлайн курса"""
    queryset = CourseFieldOfStudy.objects.all()
    serializer_class = CourseFieldOfStudySerializer


class CourseLearningOutcomeViewSet(viewsets.ModelViewSet):
    """Контроллер для модели Требования для онлайн курса"""
    queryset = CourseLearningOutcome.objects.all()
    serializer_class = CourseLearningOutcomeSerializer


class CourseWorkProgramViewSet(viewsets.ModelViewSet):
    """Контроллер для модели РПД и онлайн курс"""
    queryset = CourseWorkProgram.objects.all()
    serializer_class = CourseWorkProgramSerializer


class CourseDataAPIView(APIView):
    """
    Контроллер для загрузки данных из реестра онлайн курсов
    """

    def post(self, request):
        print('Data parsing started')
        data_Platform, data_Rigthholder, data_OnlineCourse, data_CourseFieldOfStudy, data_CourseCredit, \
        data_CourseRequirement, data_CourseLearningOutcome, data_CourseCompetence = get_data()
        print('Data parsing ended')

        """
        Adding data to Platform
        """

        for i in range(len(data_Platform)):
            if Platform.objects.filter(id=data_Platform.index[i]).exists():
                continue
            else:
                platform = Platform.objects.create(id=data_Platform.index[i],
                                                   title=data_Platform.title[i], )
                platform.save()

        """
        Adding data to Institution
        """

        for i in range(len(data_Rigthholder)):
            if Institution.objects.filter(id=data_Rigthholder.index[i]).exists():
                continue
            else:
                institution = Institution.objects.create(id=data_Rigthholder.index[i],
                                                         title=data_Rigthholder.title[i], )
                institution.save()

        """
        Adding data to OnlineCourse
        """

        for i in range(len(data_OnlineCourse)):
            if OnlineCourse.objects.filter(id=data_OnlineCourse.index[i]).exists():
                continue
            else:
                onlinecourse = OnlineCourse.objects.create(id=data_OnlineCourse.index[i],
                                                           title=data_OnlineCourse.title_x[i],
                                                           description=data_OnlineCourse.description[i],
                                                           institution=Institution.objects.get(
                                                               id=data_OnlineCourse.id_rightholder[i]),
                                                           platform=Platform.objects.get(
                                                               id=data_OnlineCourse.id_platform[i]),
                                                           language=data_OnlineCourse.language[i],
                                                           )
                onlinecourse.save()
            if data_OnlineCourse.started_at[i] != 'None':
                onlinecourse.started_at = data_OnlineCourse.started_at[i]
                onlinecourse.save()
            if data_OnlineCourse.created_at[i] != 'None':
                onlinecourse.created_at = data_OnlineCourse.created_at[i]
                onlinecourse.save()
            if data_OnlineCourse.record_end_at[i] != 'None':
                onlinecourse.record_end_at = data_OnlineCourse.record_end_at[i]
                onlinecourse.save()
            if data_OnlineCourse.finished_at[i] != 'None':
                onlinecourse.finished_at = data_OnlineCourse.finished_at[i]
                onlinecourse.save()
            if data_OnlineCourse.rating[i] != 'None':
                onlinecourse.rating = data_OnlineCourse.rating[i]
                onlinecourse.save()
            if data_OnlineCourse.experts_rating[i] != 'None':
                onlinecourse.experts_rating = float(data_OnlineCourse.experts_rating[i])
                onlinecourse.save()
            if data_OnlineCourse.visitors_number[i] != 'None':
                onlinecourse.visitors_number = int(data_OnlineCourse.visitors_number[i])
                onlinecourse.save()
            if data_OnlineCourse.total_visitors_number[i] != 'None':
                onlinecourse.total_visitors_number = int(data_OnlineCourse.total_visitors_number[i])
                onlinecourse.save()
            if data_OnlineCourse.duration[i] != 'None':
                onlinecourse.duration = int(data_OnlineCourse.duration[i])
                onlinecourse.save()
            if data_OnlineCourse.volume[i] != 'None':
                onlinecourse.volume = int(data_OnlineCourse.volume[i])
                onlinecourse.save()
            if data_OnlineCourse.intensity_per_week[i] != 'None':
                onlinecourse.intensity_per_week = int(data_OnlineCourse.intensity_per_week[i])
                onlinecourse.save()
            if data_OnlineCourse.content[i] != 'None':
                onlinecourse.content = str(data_OnlineCourse.content[i])
                onlinecourse.save()
            if data_OnlineCourse.lectures_number[i] != 'None':
                onlinecourse.lectures_number = int(data_OnlineCourse.lectures_number[i])
                onlinecourse.save()
            if data_OnlineCourse.external_url[i] != 'None':
                onlinecourse.external_url = str(data_OnlineCourse.external_url[i])
                onlinecourse.save()
            if data_OnlineCourse.has_certificate[i] != 'None':
                onlinecourse.has_certificate = bool(data_OnlineCourse.has_certificate[i])
                onlinecourse.save()
            if data_OnlineCourse.credits[i] != 'None':
                onlinecourse.credits = float(data_OnlineCourse.credits[i])
                onlinecourse.save()
        """
        Adding data to CourseFieldOfStudy
        """
        for i in range(len(data_CourseFieldOfStudy)):
            if CourseFieldOfStudy.objects.filter(id=data_CourseFieldOfStudy.index[i]).exists():
                continue
            else:
                if FieldOfStudy.objects.filter(number=data_CourseFieldOfStudy.field_of_study[i]).exists():
                    onlinecourse_field_of_study = CourseFieldOfStudy.objects.create(id=data_CourseFieldOfStudy.index[i],
                                                                                    course=OnlineCourse.objects.get(
                                                                                        id=data_CourseFieldOfStudy.id_course[i]),
                                                                                    field_of_study=FieldOfStudy.objects.get(
                                                                                        number=data_CourseFieldOfStudy.field_of_study[i]
                                                                                    ),)
                    onlinecourse_field_of_study.save()
        
        """
        Adding data to CourseCredit
        """
        
        for i in range(len(data_CourseCredit)):
            if CourseCredit.objects.filter(id=data_CourseCredit.index[i]).exists():
                continue
            else:
                if FieldOfStudy.objects.filter(number=data_CourseCredit.field_of_study[i]).exists():
                    onlinecourse_credit = CourseCredit.objects.create(id=data_CourseCredit.index[i],
                                                                      course=OnlineCourse.objects.get(
                                                                                        id=data_CourseCredit.id_course[i]),
                                                                      institution=Institution.objects.get(
                                                                          id=data_CourseCredit.id_institution[i]
                                                                      ),
                                                                      field_of_study=FieldOfStudy.objects.get(
                                                                                        number=data_CourseCredit.field_of_study[i]))
                    onlinecourse_credit.save()
        
        """
        Adding data to CourseRequirement
        """

        for i in range(len(data_CourseRequirement)):
            if CourseRequirement.objects.filter(id=data_CourseRequirement.index[i]).exists():
                continue
            else:
                if Items.objects.filter(name=data_CourseRequirement.item[i]).exists():
                    onlinecourse_requirement = CourseRequirement.objects.create(id=data_CourseRequirement.index[i],
                                                                                course=OnlineCourse.objects.get(
                                                                                    id=data_CourseRequirement.id_course[i]),
                                                                                item=Items.objects.get(
                                                                                    name=data_CourseRequirement.item[i]))
                    onlinecourse_requirement.save()
                else:
                    requirement = Items.objects.create(name=data_CourseRequirement.item[i])
                    requirement.save()
                    onlinecourse_requirement = CourseRequirement.objects.create(id=data_CourseRequirement.index[i],
                                                                                course=OnlineCourse.objects.get(
                                                                                    id=data_CourseRequirement.id_course[i]),
                                                                                item=Items.objects.get(
                                                                                    name=data_CourseRequirement.item[i]))
                    onlinecourse_requirement.save()
        
        """
        Adding data to CourseLearningOutcome
        """
        
        for i in range(len(data_CourseLearningOutcome)):
            if CourseLearningOutcome.objects.filter(id=data_CourseLearningOutcome.index[i]).exists():
                continue
            else:
                if Items.objects.filter(name=data_CourseLearningOutcome.item[i]).exists():
                    onlinecourse_learning_outcome = CourseLearningOutcome.objects.create(id=data_CourseLearningOutcome.index[i],
                                                                                         course=OnlineCourse.objects.get(
                                                                                             id=data_CourseLearningOutcome.id_course[i]),
                                                                                         item=Items.objects.get(
                                                                                             name=data_CourseLearningOutcome.item[i]))
                    onlinecourse_learning_outcome.save()
                else:
                    learning_outcome = Items.objects.create(name=data_CourseLearningOutcome.item[i])
                    learning_outcome.save()
                    onlinecourse_learning_outcome = CourseLearningOutcome.objects.create(id=data_CourseLearningOutcome.index[i],
                                                                                         course=OnlineCourse.objects.get(
                                                                                             id=data_CourseLearningOutcome.id_course[i]),
                                                                                         learning_outcome=Items.objects.get(
                                                                                             name=data_CourseLearningOutcome.item[i]))
                    onlinecourse_learning_outcome.save()"""
            
        return Response(status=200)
