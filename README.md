# Projeto Base -- Interface Gráfica X "Banco de Dados" --

Pensando na constante vontade do ser humano de evoluir, partindo da ideia de que o conforto e a simplicidade são essenciais, decedi então começar um pequeno projeto de unir uma interface gráfica a um "banco de dados".

Entretanto, este projeto ainda não possui a parte de banco de dados no que se refere à linguagem de programação SQL. Fora utilizada uma outra alternativa mais simples e pouco menos complexa, um arquivo .xlsx, ou seja uma planilha.

Com essa alternativa é notório que não é possível manusear uma planilha comum da mesma forma que fazemos com um banco de dados. Contudo, torna-se possível, aquilo que consideramos favoravelmente básico para um banco de dados, utilizá-lo como uma planilha no que se refere a 2 subconjuntos da linguagem SQL:
  
  DQL (Data Query Language):
  * SELECT.

  DML (Data Manipulation Language):
  * INSERT;
  * UPDATE;
  * DELETE.

Portanto, desenvolvi uma interface gráfica em Python com auxílio das bibliotecas Tkinter e CustomTkinter visando a facilidade de utilização e manipulação de dados dentro desta planilha.
Vale ressaltar que, julgando pelas limitações de usar planilhas e não um banco de dados a princípio, inspirado nas 4 execuções citadas anteriormente, esta interface somente é capaz de VISUALIZAR, CADASTRAR, ALTERAR e APAGAR os dados!


## 🚀 Let's get started!!

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento, teste ou até mesmo, utilização própria.

### 📋 Pré-requisitos
Primeiro consulte **[Instalação](#-Instala%C3%A7%C3%A3o)** para saber como instalar a base para toda a execução.

* Instalar Python na sua máquina;
* Instalar as bibliotecas que serão utilizadas.

### 🔧 Instalação

- Instalar PYTHON

  -> leia este passo a passo:

    [Como instalar Python? (WINDOWS)](https://python.org.br/instalacao-windows/)

    [Como instalar Python? (LINUX)](https://python.org.br/instalacao-linux/)

    [Como instalar Python? (MAC)](https://python.org.br/instalacao-mac/)

- Instalar as bibliotecas:
  - pandas
  - customtkinter

    -> Siga o passo-a-passo abaixo para instalar as bibliotecas

    - Tecla "Windows" -> digite "cmd" e aperte "Enter"
    - Aparecerá o prompt de comando (uma tela preta com códigos)
    - Digite:
      ```
      py -m pip install "pandas"
      ```
    - Espere terminar de carregar e logo após digite:
      ```
      py -m pip install "customtkinter"
      ```

## ⚙️ Executando os testes

Fique calmo! A interface gráfica completa foi projetada para lhe guiar no que você precisar! Intuitiva e facilitada.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implementar cada parte do projeto.

Logo após a instalação e implemetação completa, se realizada corretamente, o projeto poderá ser usado sem moderação!

## 📦 Implantação

Siga este passo-a-passo:

* Clique no botão verde **"Code <>"**

![Imagem1](https://private-user-images.githubusercontent.com/92381281/354704815-94edd0a3-c712-4de3-895f-55220f02939b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI2Mjc1ODYsIm5iZiI6MTcyMjYyNzI4NiwicGF0aCI6Ii85MjM4MTI4MS8zNTQ3MDQ4MTUtOTRlZGQwYTMtYzcxMi00ZGUzLTg5NWYtNTUyMjBmMDI5MzliLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODAyVDE5MzQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ2ZDYyZjM4MjI4YTQ2MjUyYTg2YzU4NjQ3MWNjYzRiYjFjOTQxODcwZTlmNDI1NzRmMmRiNWUxNmNjOGU0MGQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.xJEn8Obvsy0v3TMKcCq20509WTK9Tt-0ArtptCckRs8)

* Clique no botão **"Download ZIP"**

![Imagem2](https://private-user-images.githubusercontent.com/92381281/354704818-4a6c87d1-8d29-45f7-8830-cdd66f1c8260.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI2Mjc4NTAsIm5iZiI6MTcyMjYyNzU1MCwicGF0aCI6Ii85MjM4MTI4MS8zNTQ3MDQ4MTgtNGE2Yzg3ZDEtOGQyOS00NWY3LTg4MzAtY2RkNjZmMWM4MjYwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODAyVDE5MzkxMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU1ZjkxNGZkZDg4OGM0YWU3ZmJmMjI4ZDBhYjQ4MzkzZjU4OGEwYWJmZjdmZWZkMTRkMTQxNzE0YmJlZWIzZGImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.KFEJBq-E36nVa3mz-jwyWKwTxJziV08rl5GyOcPesKo)

* Extraia os arquivos do ZIP para a pasta que desejar (Fique tranquilo! Será apenas uma pasta contendo tudo)
* Dentro da pasta que você extraiu, terá um arquivo chamado *credenciais.txt*
  - Esse arquivo txt possui apenas 2 linhas
      ```
      usuario
      senha
      ```
  - Você irá alterar essas linhas para o usuário e senha que desejar
  - ATENCÃO!! Não adicione linhas ou espaço entre elas, ela deve possuir exclusivamente 2 linhas (uma para o Usuário e outra para a Senha)

* Para executar o projeto você deve abrir o arquivo *cadastros.py*
* Ele, então, irá abrir uma janela preta do Python e a janela da execução em si
* Você deve minimizar a janela do Python e seguir com sua execução na janela de LOGIN
* NÃO FECHE A JANELA DO PYTHON! APENAS MINIMIZE-A!

## 🛠️ Construído com

* [Pandas](https://pandas.pydata.org/docs/) - Tratamento de dados
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - Base GUI
* [CustomTkinter](https://customtkinter.tomschimansky.com/) - GUI atualizada

## ✒️ Autor

* **Enzzo Dias Nogueira** - *Planejador/Arquiteto de Software/Desenvolvedor do projeto geral* - [enzzodn](https://github.com/enzzodn)

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.
