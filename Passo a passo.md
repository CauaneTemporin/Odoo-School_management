# Odoo-School_management
Modulo escola com Odoo13 e pyhton


 #######Tutorial para instalação e configrações inicias básicas de ambiente Odoo versão 13#######
Este passo a passo tem o objetivo de auxiliar com os passos minimos na inicialização de um novo ambiente Odoo 13.

                                                #####Configurações de Ambiente######

                                            ######Sistema Operacioanl######

1 - O Framework Odoo tem melhor desempenho em ambiente Linux por tanto abaixo estão algumas dicas para melhor funcionamento:

A - Caso esteja em uma máqui com windows você pode fazer download de um software para simular o linux
basta realizar o download através do seguinte link: https://download.virtualbox.org/virtualbox/7.0.4/VirtualBox-7.0.4-154605-Win.exe

B - Após instalação e configuração de  máquina virtual 
é necessário um arquivo de iumagem (ISO) linux que pode ser baixada através do link: https://releases.ubuntu.com/22.04/ubuntu-22.04.1-desktop-amd64.iso


                                                #####Configurações de máquina virtual######

1 - Crie um anova máquina com as especifiações abaixo, se disponível 
memória ram 3GB
hd: 30 GB 

                                                ######Arquivos Odoo######

1 - Precisamos obter os arquivos do Odoo para iniciar as configrações então basta copiar e colar o link abaixo em sua barra de endereços no browser, ou
segurar tecla ctrl + click com botão esquerdo e o download ja deve começar automáticamente.
link: https://github.com/odoo/odoo/archive/refs/heads/13.0.zip

2 - Após concluir o download vá até a pasta e extraia o arquivo .zip para uma pasta de sua escolha de preferência com facíl acesso.                                                

                                                
                                                ######Python######
Para utilizar a versão 13 do Odoo é necessário ter instalada a versão 3.6 ou 3.7 do python, para prosseguir com a instalação utilize os comandos abaixo:
A - sudo apt update
B - sudo apt install software-properties-common
C - sudo add-apt-repository ppa:deadsnakes/ppa    --- após este comando aperte (ENTER) quando solicitar na tela
D - sudo apt install python3.7
Certifique se que ocorreu tudo bem executando o comando:
python3.7 --version
Caso esteja tudo ok você deve ter a saída: 
Python 3.7.xxx


                                                ######Banco de dados######

O Framework Odoo utiliza por padrão o banco de dados PostgreSQL e faremos a instalçao seguindo os passos abaixo.

1 - Para instalar o banco de dados utilize o comando abaixo:

A - sudo apt install postgresql postgresql-client

2 - Crie um novo usuário com o comando abaixo basta copiar e colar linha por linha:

A - sudo -u postgres createuser -s odoo
B - utilize o comando: psql
C - create database odoo;
D - ALTER DATABASE odoo OWNER TO odoo;
E - GRANT ALL PRIVILEGES ON DATABASE "odoo" to odoo;
F - ALTER USER odoo WITH PASSWORD 'sua nova senha';


3 Instale as dependências necessárias para correto funcionamneto utilizando o comando abaixo (Rodar comando no terminal):
 
 A- sudo apt install python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
    libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev

Obs(copie as três linhas e cole de uma vez)


                                                #####Configuração do Python######

1 -Para o correto funcionamneto do Odoo de forma isolada se faz necessário a criação de um ambiente virtual:
Um ambiente virtual é um "local isolado" onde todas as bibliotecas instaladas ficam isoladas de outros projetos, para que não hajam conflitos de depêndencias:

A - Navegue até a pasta com os arquivos que foram extraídos e abra um terminal.
Abrir terminal: utilize o atalho ctrl + t ou vá até a pasta extraída clique com o botão direito e procure pela opção "Abrir no terminal".
Obs: Você pode utilizar o comando cd (nome do diretório para ir até o diretório) 
exemplo: cd Área\ de\ Trabalho/odoo-13.0/
e também pode utilizar a tecla tab para completar o resto da frase
exemplo cd Áre + tecla tab ....

B - Utilize o seguinte comando para criar seu ambiente virtual: 
python3 -m venv odoo_env  (este ultimo paramentro (odoo_env) pode ser modificado para o nome que você desejar).
Obs: Após este comando ser executados sem falhas uma nova pasta será gerada com o nome odoo_env ou o nome 
escolhido na hora de sua criação.                                             

2 - Dentro da pasta extraída de nome (odoo-13.0) existe um arquivo chamado requirements.txt, este arquivo carrega todas as dependências necessárias para iniciar o Odoo.
Utilizando o terminal certifique se de estar no mesmo diretório que o arquivo requirements.txt
Obs: Você pode utilizar o comando cd (nome do diretório para ir até o diretório desejado) 
exemplo: cd Área\ de\ Trabalho/odoo-13.0/
e também pode utilizar a tecla tab para completar o resto da frase
exemplo cd Áre + tecla tab ....

3 - Dentro deste diretório execute os comandos:

A - Para ativação do ambiente virtual:
source odoo_env/bin/activate
Obs: Após executado, no inicio da linha de comando aparecerá o nome do ambiente virtual entre parenteses ex:(odoo_env) teste@jsouza:~/Área de Trabalho/odoo-13.0$

B - pip3 install setuptools wheel

C - Para instalação das dependências utilize o comando abaixo 
pip install -r ./caminho/requirements.txt
Aguarde a finalização.
##################################################
Copie e cole os comandos abaixo.
1. pip3 install libsass==0.12.3


2.sudo apt update
  sudo apt install sassc
  
##################################################


                                                #####Configuração do arquivo Odoo######

1 - Dentro da pasta que foi extraída existe um subpasta de nome debian, localize dentro da mesma o arquivo de nome (odoo.conf) 
e atualize conforme demonstrado abaixo pode copiar e colar:

[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = localhost
db_port = False
db_user = odoo
db_password = Aqui vai a senha definida no passo D da configuração do bando de dados.
db_name = odoo
addons_path = /home/teste/Área de Trabalho/odoo-13.0/addons, /home/teste/Área de Trabalho/odoo-13.0/odoo/addons                            

2 - Para adicionar seus módulos customizados ou módulos externos basta incluir o caminho de sua pasta com módulos no final da ultima linha 
do arquivo odoo.conf que está na pasta debian
precedido por virgula.
Exemplo:
addons_path = /home/teste/Área de Trabalho/odoo-13.0/addons, /home/teste/Área de Trabalho/odoo-13.0/odoo/addons,   /home/teste/Área de Trabalho/odoo-13.0/odoo/meus_modulos
(não pode haver espaços no caminho da pasta)


Possiveis erros:
Caso apareça algo do tipo
(ModuleNotFoundError: No module named '
basta utilizar o comando: pip3 install + o nome do módulo, neste caso babel (pip3 install babel')

Por fim utilize o seguinte comando para iniciar o Framework
Obs: é necessário estar dentro da pasta onde se encontram os arquivos do Odoo
Comando: ./odoo-bin -c ./debian/odoo.conf -i odoo
ou ./odoo-bin -c ./odoo.conf -d base_teste


Coloca na aba projetos 
source odoo_env/bin/activate

Caso não rode
python3 odoo-bin -u odoo -d base_teste


criar banco de dados
http://localhost:8069/web/database/manager

bibliotecas com erro 
psutil==5.6.6
