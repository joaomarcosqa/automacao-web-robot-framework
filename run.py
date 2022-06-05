import sys
import os
import platform
from os import path

sys.path.append(path.abspath('./'))
# import config

for param in sys.argv[1:]:
    # comandos para rodar todas as suites de testes web:
    # comando a ser usado python run.py -web
    if param == "-web":
        command = "robot -d ./logs ./testes "
    # comando para rodar a suite de testes de login:
    # comando a ser usado python run.py -login
    elif param == "-login_web":
        command = "robot -d ./logs ./testes/login.robot "
    # exemplo de comando a ser criado com novas suites
    # alterar comando e o caminho
    # comando novo a ser usado será sempre python run.py e o nome desejado do comando
    elif param == "-":
        command = "robot -d ./logs ./testes/login.robot "
    # quando for necessario criar novos comenados pode ser usado o copiar e colar
    # copiar o elif e colocar o novo comando e caminho


    # comandos para rodar todas as suites de testes de api:
    # comandos para xecutar os testes de api
    elif param == "-api":
        command = "robot -d ./logs ./automacao_api/testes "

    elif param == "-login_api":
        command = "robot -d ./logs ./automacao_api/testes/login.robot "
        
    if param == "-cadastro_api":
        command = "robot -d ./logs ./automacao_api/testes/cadastro.robot "

    # comandos para rodar todas as suites de testes mobile:
    # comandos para executar os testes mobile
    elif param == "-mobile":
        command = "robot -d ./logs ./automacao_mobile/testes "

    elif param == "-login_mobile":
        command = "robot -d ./logs ./automacao_mobile/testes/login.robot "

os.system(command)
