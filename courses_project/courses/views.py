from urllib import request
from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from courses.models import *

# Landing page ------------------------------------------------------------------------------

def landing_page(request):
    return render(request, 'landing_page.html')

# Lis Views ----------------------------------------------------------------------------------

class CourseUserListView(ListView):
    model = CourseUser
    template_name = 'user_course_list.html'
    context_object_name = 'user_courses_list'

class CourseListView(ListView):
    model = Course
    template_name = 'course_list_view.html'
    context_object_name = 'courses'

class CourseStatusListView(ListView):
    model = Status
    template_name = 'course_status_list.html'
    context_object_name = 'course_statuses'

class UserCertificateListView(ListView):
    model = 'profile_user'
    template_name = 'user_certification_list.html'
    context_object_name = 'usercertificates'

class CertificateListView(ListView):
    model = Certificate
    template_name = 'certificate_list.html'
    context_object_name = 'certificates'

class ReviewListView(ListView):
    model = Review
    template_name ='review_list.html'
    context_object_name ='reviews'

# class CategoryListView(ListView):
#     model = Category
#     template_name = 'category_list.html'
#     context_object_name = 'categories'

# class SectorListView(ListView):
#     model = Sector
#     template_name ='sector_list.html'
#     context_object_name ='sectors'

class LessonListView(ListView):
    model = Lesson
    template_name = 'lesson_list.html'
    context_object_name = 'lessons'

class ResourceListView(ListView):
    model = Resource
    template_name ='resource_list.html'
    context_object_name ='resource_list'

class ModuleListView(ListView):
    model = Module
    template_name ='module_list.html'
    context_object_name ='modules'

class ProfileTeacherListView(ListView):
    model = ProfileTeacher
    template_name = 'profile_teacher_list.html'
    context_object_name = 'teacher-list'

class CertificateListView(ListView):
    model = Certificate
    template_name = 'certificate_list.html'
    context_object_name = 'certificates'
    success_url = reverse_lazy('certificate-list')

# Create Views ----------------------------------------------------------------------------

class ProfileTeacherCreateView(CreateView):
    model = ProfileTeacher
    fields = '__all__'
    template_name = 'profile_teacher_form.html'
    success_url = reverse_lazy('profile_teacher_list')

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'course_form.html'
    success_url = reverse_lazy('course-list')

class UserCertificationCreateView(CreateView):
    model = 'ProfileUser'
    fields = '__all__'
    template_name = 'user_certification_form.html'
    success_url = reverse_lazy('usercertification-list')

class CertificateCreateView(CreateView):
    model = Certificate
    fields = '__all__'
    template_name = 'certificate_form.html'
    success_url = reverse_lazy('certificate-list')

# Update Views ----------------------------------------------------------------------

class CertificateUpdateView(UpdateView):
    model = Certificate
    fields = '__all__'
    template_name = 'certificate_form.html'
    success_url = reverse_lazy('certificate-list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'course_form.html'
    success_url = reverse_lazy('course-list')

class UserCertificationUpdateView(UpdateView):
    model = 'ProfileUser'
    fields = '__all__'
    template_name = 'user_certification_form.html'
    succes_url = reverse_lazy('user_certification-list')




    