from django.contrib import admin
from hw8.models import Curators, Lectures, Faculties, Teachers, Subjects, Departments, Groups, GroupsCurator, GroupLectures
# Register your models here.

admin.site.register(Curators)
admin.site.register(Lectures)
admin.site.register(Faculties)
admin.site.register(Teachers)
admin.site.register(Subjects)
admin.site.register(Departments)
admin.site.register(Groups)
admin.site.register(GroupsCurator)
admin.site.register(GroupLectures)
