from typing import List
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from rest_framework.decorators import api_view

from tinyurl.services import is_valid_url, push_url, get_url, get_urls, increment_hits
from tinyurl.models import Urls


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        full_url: str = request.data.get("full_url", "")
        if not is_valid_url(full_url):
            return HttpResponseBadRequest(render_to_string("tinyurl/error.html"))

        push_url(full_url)

    urls: List[Urls] = get_urls()
    return render(request, "tinyurl/index.html", {"urls": urls})


@api_view(['GET'])
def hits(request, tiny_url):

    url = get_url(tiny_url)
    if url:
        increment_hits(url)
        return redirect(url.full_url)
    else:
        return HttpResponseRedirect(reverse("tinyurl:index"))
