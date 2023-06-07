import functions_framework

@functions_framework.http
def service(request):
    return "OK", 201