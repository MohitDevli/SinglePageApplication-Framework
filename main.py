import sys
import os

def touch(file):
    open(file, 'w').close()

def makeSoftProject(appName):
    try:
        os.mkdir(os.path.join(os.getcwd(), appName))
        os.mkdir(os.path.join(os.path.join(os.getcwd(), appName) , 'headersfile'))
        os.mkdir(os.path.join(os.path.join(os.getcwd(), appName) , 'templates'))
        os.mkdir(os.path.join(os.path.join(os.getcwd(), appName) , 'staticfiles'))
    except FileExistsError:
        print("Project with same name already exists, please try with a diffreny name.\n")
        _PageType()

    touch(os.path.join(os.path.join(os.path.join(os.getcwd(), appName) , 'headersfile'), 'index.html'))
    touch(os.path.join(os.path.join(os.path.join(os.getcwd(), appName) , 'headersfile'), 'header.js'))
    touch(os.path.join(os.path.join(os.getcwd(), appName) , 'projectsettings.py'))
    touch(os.path.join(os.path.join(os.path.join(os.getcwd(), appName) , 'templates'), 'main.html'))

    with open(os.path.join(sys.path[0], 'staticfiles/soft/header.js'), 'r') as js:
        with open(os.path.join(os.path.join(os.getcwd(), appName) , 'headersfile/header.js'), 'w') as usrJS:
            usrJS.write(js.read())

    with open(os.path.join(sys.path[0], 'staticfiles/soft/index.html'), 'r') as html:
        with open(os.path.join(os.path.join(os.getcwd(), appName) , 'headersfile/index.html'), 'w') as usrhtml:
            usrhtml.write(html.read())

    with open(os.path.join(sys.path[0], 'staticfiles/soft/projectsettings.py'), 'r') as settings:
        with open(os.path.join(os.path.join(os.getcwd(), appName) , 'projectsettings.py'), 'w') as usrsetting:
            usrsetting.write(settings.read())

    with open(os.path.join(sys.path[0], 'staticfiles/soft/main.html'), 'r') as main:
        with open(os.path.join(os.path.join(os.getcwd(), appName) , 'templates/main.html'), 'w') as usrmain:
            usrmain.write(main.read())

    usrmain.close()
    main.close()
    usrsetting.close()
    settings.close()
    usrhtml.close()
    html.close()
    usrJS.close()
    js.close()


def _PageType():
    pageType = input('which type of application you want (1: Soft, 2: Strong), press 1 or 2: ')
    
    if pageType == "1":
        print("Creating a Soft web app........")
        makeSoftProject(input("Enter the project name: "))

    elif pageType == "2":
        print("Crating a Strong web app........")
        
    else:
        print("please choose 1 or 2 only.\n")


argv = sys.argv
if 'startproject' in argv:
    _PageType()

""" updatesettings """
