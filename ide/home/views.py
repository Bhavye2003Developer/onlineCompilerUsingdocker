from django.shortcuts import render
import subprocess
import os

from ide.settings import BASE_DIR

def index(request):
    output = ""
    if request.method == 'POST':
        userCode = request.POST.get('userCode','')

        option = request.POST.get('btnradio')
        if option == 'pylang':
            f = open("static/pythonCodes/pyCode.py","w")
            f.write(userCode)
            f.close()

            cur_dir = os.getcwd()
            os.chdir(f'{BASE_DIR}/static/pythonCodes/')

            subprocess.run("docker build -t pycode .".split())
            output = subprocess.check_output("docker run pycode".split()).decode()
            os.chdir(cur_dir)

            return render(request,"home.html",context={'output':output})

        elif option == 'cpplang':
            f = open("static/c++Codes/c++Code.cpp","w")
            f.write(userCode)
            f.close()

            cur_dir = os.getcwd()
            os.chdir(f'{BASE_DIR}/static/c++Codes/')

            subprocess.run("docker build -t cppcode .".split())
            output = subprocess.check_output("docker run cppcode".split()).decode()
            os.chdir(cur_dir)

            return render(request,"home.html",context={'output':output})
    return render(request, "home.html")