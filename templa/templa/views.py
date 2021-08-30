#This file is created by me
# https://docs.djangoproject.com/en/3.2/intro/tutorial02/ documentation/github

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def contact(request):
    # Fetch the Data
    mytext=request.GET.get('n1','default')
    myCheck=request.GET.get('check','off')
    myCheck1=request.GET.get('upperChar','off')
    myLower=request.GET.get('lowerChar','off')
    removenewline=request.GET.get('removenewline','off')
    removespace=request.GET.get('removespace','off')
    countchar=request.GET.get('countchar','off')

    # print(mytext)
    # print(myCheck)
    if myCheck=='on':
        analyzation=""
        punchtuation= '''!()[]-{}&%$*,\<>./?@";:^&_~'''
        for i in mytext:
            if i not in punchtuation:
                analyzation=analyzation+i

        if(myCheck1=="on"):
            analyzation=analyzation.upper()
        params={'purpose':'Remove Punchtuation','analyse':analyzation}
        return render(request,'removePunc.html',params)

    elif myCheck1=='on':
        analyse=""
        analyse=analyse+mytext.upper()
        params={'purpose':'CAPITALIZED THE CHARACTER','analyse':analyse}
        return render(request,'removePunc.html',params)

    elif myLower=='on':
        analyse=""
        analyse=analyse+mytext.lower()
        params={'purpose':'Lower Character','analyse':analyse}
        return render(request,'removePunc.html',params)

    elif removenewline=="on":
        analyse=""
        for i in mytext:
            if i!="\n":
                analyse=analyse+i
        params={'purpose':'Remove New Line','analyse':analyse}
        return render(request,'removePunc.html',params)

    elif removespace=="on":
        analyse=""
        mytext=mytext.strip()
        for i,j in  enumerate(mytext):
           if not(mytext[i]==" " and mytext[i+1]==" "):
               analyse=analyse+j
        params={'purpose':'Remove New Line','analyse':analyse}
        return render(request,'removePunc.html',params)

    elif countchar=="on":
        analyse=f"Total number of character is {len(mytext)}"
        params={'purpose':'Count Character','analyse':analyse}
        return render(request,'removePunc.html',params)

    else:
        return  HttpResponse("<h1>Error</h1>")
