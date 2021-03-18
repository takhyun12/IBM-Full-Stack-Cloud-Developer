from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2

class QuestionInline (admin.StackedInline):
    model = Question
    extra = 2

class ChoiceInline (admin.StackedInline):
    model = Choice
    extra = 4

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
