from django.shortcuts import render


def _error(request, status_code, reason):
    return render(
        request,
        "error.html",
        {
            "status_code": status_code,
            "reason": reason,
        },
        status=status_code,
    )


def handler403(request, exception=None):
    return _error(request, status_code=403, reason="Forbidden")


def handler404(request, exception=None):
    return _error(request, status_code=404, reason="Not Found")


def handler500(request, exception=None):
    return _error(request, status_code=500, reason="Internal Server Error")
