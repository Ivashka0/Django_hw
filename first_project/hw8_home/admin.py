from django.contrib import admin
from hw8_home.models import Department, Doctor, Examination, Ward, Sponsor, DoctorsExamination, Donation

admin.site.register(Department)
admin.site.register(Sponsor)
admin.site.register(Doctor)
admin.site.register(Examination)
admin.site.register(Ward)
admin.site.register(Donation)
admin.site.register(DoctorsExamination)
