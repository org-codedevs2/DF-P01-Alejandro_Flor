from django.shortcuts import render

from .forms import SumaForm


def sumar(request):
    form = SumaForm(request.POST if request.method == "POST" else None)
    resultado = None

    if request.method == "POST" and form.is_valid():
        resultado = form.cleaned_data["numero1"] + form.cleaned_data["numero2"]

    return render(
        request,
        "suma/index.html",
        {"form": form, "resultado": resultado},
    )