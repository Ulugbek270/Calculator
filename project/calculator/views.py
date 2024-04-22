from django.http import HttpResponse
from django.shortcuts import render
from .models import Calculator
from sympy import symbols


def calculator(request):
    history = Calculator.objects.all().order_by('-created_at')[:10]
    result = 0
    operation = None
    if request.method == 'POST':
        num1 = int(request.POST.get('number1', 0))
        num2 = int(request.POST.get('number2', 0))
        operation = request.POST.get('operation')
        if operation == "add":
            result = num1 + num2
            result = f"{num1} + {num2} = {result}"
            Calculator.objects.create(history=f'{result}')


        elif operation == "subtract":
            result = num1 - num2
            result = f"{num1} - {num2} = {result}"
            Calculator.objects.create(history=f'{result}')

        elif operation == "multiply":
            result = num1 * num2
            result = f"{num1} * {num2} = {result}"
            Calculator.objects.create(history=f'{result}')

        elif operation == "divide":
            result = num1 / num2
            result = f"{num1} / {num2} = {result}"
            Calculator.objects.create(history=f'{result}')
    context = {
        'result': result,
        'history': history,
        'operation': operation,
    }
    return render(request, 'base.html', context)
