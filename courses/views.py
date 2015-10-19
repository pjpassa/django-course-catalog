from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from courses.forms import CourseForm


class CourseAddChangeView(FormView):
    form_class = CourseForm
    template_name = "course_add_change.html"
    success_url = reverse_lazy("add")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
