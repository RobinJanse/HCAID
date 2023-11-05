from django.contrib import admin
from django.urls import include, path

from hcaidApi.app.bad import home as bad_home
from hcaidApi.app.bad import apply as bad_apply
from hcaidApi.app.bad import stats as bad_stats
from hcaidApi.app.bad import privacy as bad_privacy

from hcaidApi.app.good import home as good_home
from hcaidApi.app.good import apply as good_apply
from hcaidApi.app.good import stats as good_stats
from hcaidApi.app.good import privacy as good_privacy

bad_patterns = [
    path("", bad_home.index),
    path("apply/", bad_apply.index),
    path("stats/", bad_stats.index),
    path("privacy/", bad_privacy.index),
]

good_patterns = [
    path("", good_home.index),
    path("apply/", good_apply.index),
    path("stats/", good_stats.index),
    path("privacy/", good_privacy.index),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bad/", include(bad_patterns)),
    path("good/", include(good_patterns)),
]