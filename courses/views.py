from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, ListView, DetailView
from courses.forms import CourseForm
from courses.models import Course


class CourseAddChangeView(FormView):
    form_class = CourseForm
    template_name = "course_add_change.html"
    success_url = reverse_lazy("list")

    # If the form is valid, save the instance
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # If we are updating, initialize the form
    def get_form(self, form_class=None):
        pk = self.kwargs.get('pk', None)
        if pk:
            course = Course.objects.get(pk=pk)
            if self.request.method == "GET" and pk:
                return self.get_form_class()(instance=course)
            elif self.request.method == "POST" and pk:
                return self.get_form_class()(self.request.POST, instance=course)
        return super().get_form(form_class)

class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"
