from django.views.generic import TemplateView
from youtube.libs.api_wrapper import YouTubeApi
from django.contrib.auth.mixins import LoginRequiredMixin


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = 'youtube/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        youtube_api = YouTubeApi(self.request.user)
        search = youtube_api.search()
        context['search'] = search
        return context
