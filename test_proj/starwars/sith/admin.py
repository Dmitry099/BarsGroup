from django.contrib import admin

from starwars.sith import models


admin.site.register((models.Planet, models.Recruter, models.Sith,
                     models.TestExam, models.Question, models.Answer))
