from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Curators(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Faculties(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    financing = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f"{self.name}"


class Departments(models.Model):
    financing = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    name = models.CharField(max_length=100, unique=True, null=False)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.SET_NULL, null=True)

    # on_delete=models.CASCADE/on_delete=models.SET_DEFAULT, default=0

    def __str__(self):
        return f"{self.name}"


class Groups(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    year = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    department_id = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.year}"


class GroupsCurator(models.Model):
    curators_id = models.ForeignKey(Curators, on_delete=models.SET_NULL, null=True)
    groups_id = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"GroupID:{self.groups_id} CuratorID:{self.curators_id}"


class Teachers(models.Model):
    name = models.CharField(max_length=100, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    surname = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Subjects(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.name}"


class Lectures(models.Model):
    lecture_room = models.CharField(max_length=100, null=False)
    subject_id = models.ForeignKey(Subjects, on_delete=models.SET_NULL, null=True)
    teachers_id = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Room:{self.lecture_room} SubjectID:{self.subject_id} TeacherID:{self.teachers_id}"


class GroupLectures(models.Model):
    groups_id = models.ForeignKey(Groups, on_delete=models.SET_NULL, null=True)
    lectures_id = models.ForeignKey(Lectures, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"GroupID:{self.groups_id} LectureID:{self.lectures_id}"