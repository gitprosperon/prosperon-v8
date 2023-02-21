from django.shortcuts import render
from .models import Tool


def tool_page(request, id):
    tool = Tool.objects.get(tool_id=id)
    tool_path = tool.html_path

    return render(request, f'MainWebsite/tools/{tool_path}.html')



def mortgage_calculator(request):
    return render(request, 'MainWebsite/tools/mortgage-calculator.html')