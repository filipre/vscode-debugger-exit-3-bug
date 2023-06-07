import functions_framework

# raise Exception("Error")

@functions_framework.http
def service(request):
    return "OK", 200