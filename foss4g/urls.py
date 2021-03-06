from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from django.contrib import admin

import foss4g.views
import symposion.views


urlpatterns = patterns(
    "",
    url(r'^$', RedirectView.as_view(url='/account/login'), name="home"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r'^proposals/export/', foss4g.views.proposal_export,
        name='proposal_export'),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r'^reviews/export/', foss4g.views.review_export,
        name='review_export'),
    url(r"^schedule/", include("symposion.schedule.urls")),

    url(r"^teams/", include("symposion.teams.urls")),

    url(r"^boxes/", include("pinax.boxes.urls")),
    url(r'^taggit/', include('taggit_selectize.urls')),
    url(r"^", include("pinax.pages.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
