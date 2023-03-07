from django.shortcuts import render
import random


def index(request):
    return render(request, "input.html")


def randomnum(request):
    num1 = request.POST["num1"]
    num2 = request.POST["num2"]

    if num1.isdigit() and num2.isdigit() or num1 > num2:
        a = int(num1)
        myGame = [n + 1 for n in range(a)]

        b = int(num2)

        if a < b:
            wrong =  "The first number should be greater."
            context = {'wrong':wrong}
            return render(request, "result.html", context)
            
        res = random.sample(myGame, b)
        res.sort()

        greet = "Here are yours numbers!"

        # return render(request, "result.html", {"result":res})
        return render(
            request, "result.html", {"result": (",  ".join(str(e) for e in res)), 'greet':greet}
        )

    else:
        res = "Only digits are allowed."
        return render(request, "result.html", {"result": res})