🖼️ Image Processing Navpack

Um projeto Python para processamento de imagens, utilizando bibliotecas como scikit-image e imageio para comparar, transformar e salvar imagens. 
Este guia cobre a criação, publicação e uso do pacote, e inclui ferramentas essenciais como setuptools e twine para gerenciamento de pacotes Python.

📁 Estrutura do Projeto


image_processing_navpack/
├── .venv/                     # Ambiente virtual (não deve ser incluído no pacote)
├── image_processing_navpack/  # Pasta do código fonte
│   ├── imgs/                 # Imagens usadas
│   │   ├── imagem1.jpg
│   │   └── imagem2.jpg
│   ├── processing/           # Código de processamento de imagem
│   │   ├── __init__.py
│   │   ├── combination.py
│   │   └── transformation.py
│   ├── utils/                # Código de utilitários
│   │   ├── __init__.py
│   │   ├── io.py
│   │   └── plot.py
│   └── tests/                # Testes
│       ├── __init__.py
│       ├── test_processing.py
│       ├── test_utils.py
│       └── test_image.py     # Script principal para o usuário final
├── setup.py                  # Configuração do pacote
├── MANIFEST.in                # Arquivo para incluir arquivos no pacote
└── README.md                  # Documentação do projeto

🚀 Parte 1: Criação e Publicação do Pacote

🛠️ Passo 1: Clonar o Repositório

Para começar, clone o repositório do projeto para sua máquina local:

Copiar código
git clone https://github.com/Fabianonavarro/image_processing_navpack.git

🛠️ Passo 2: Navegar para o Diretório do Projeto
Entre no diretório do projeto clonado:

cd image_processing_navpack

🛠️ Passo 3: Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto. Este passo é opcional, mas recomendado:

####Para Windows:
Copiar código
python -m venv .venv
.venv\Scripts\activate

@@@Para macOS/Linux:

Copiar código
python -m venv .venv
source .venv/bin/activate

🛠️ Passo 4: Instalar Dependências

Instale as dependências necessárias para o projeto. Se você já tem um arquivo requirements.txt, use o seguinte comando:

pip install -r requirements.txt

🛠️ Passo 5: Atualizar o pip

Certifique-se de que o pip está atualizado:

python -m pip install --upgrade pip

🛠️ Passo 6: Instalar ou Atualizar o setuptools

Instale ou atualize o setuptools, que é uma ferramenta essencial para a criação de pacotes:

pip install --upgrade setuptools

🛠️ Passo 7: Instalar o twine

Instale o twine, uma ferramenta recomendada para o upload de pacotes para o PyPI:

pip install twine

🛠️ Passo 8: Atualizar o Projeto e Gerar Distribuições

Para atualizar o projeto e criar as distribuições, execute:

python setup.py sdist bdist_wheel

🛠️ Passo 9: Publicar o Pacote no PyPI - Não esqueça de criar a conta primeiro https://pypi.org/

Use o twine para publicar o pacote:

twine upload dist/*

Após a publicação, o projeto estará disponível para futuros forks no GitHub: GitHub - image_processing_navpack.

🎬 Parte 2: Uso do Pacote

🛠️ Passo 1: Criar um Ambiente Virtual

Crie um novo ambiente virtual para o seu projeto:

###Para Windows:
python -m venv myenv

@@Para macOS/Linux:
python -m venv myenv

🛠️ Passo 2: Ativar o Ambiente Virtual

Ative o ambiente virtual que você acabou de criar:

Para Windows:
myenv\Scripts\activate

Para macOS/Linux:
source myenv/bin/activate

🛠️ Passo 3: Atualizar o pip

Com o ambiente virtual ativado, atualize o pip:

python -m pip install --upgrade pip

🛠️ Passo 4: Instalar o Pacote
Você tem duas opções para instalar o pacote:

Instalar o pacote que você criou localmente:

Se você estiver testando o pacote que você criou, use:

pip install .

Instalar a versão já publicada no PyPI para testes:

Se você deseja instalar a versão publicada para testar a funcionalidade do pacote, use:

pip install image-processing-navpack==0.2.7

🛠️ Passo 5: Atualizar o setuptools

Atualize o setuptools para garantir que você tenha a versão mais recente:

pip install --upgrade setuptools

🛠️ Passo 6: Executar o Programa
Execute o comando para rodar o programa:

image-processing
Os resultados serão salvos no diretório image_processing_navpack/imgs com os seguintes nomes:

difference_image.jpg

histogram_matched_image.jpg

Menu:
1 - Transferir Histograma entre as Imagens
2 - Mostrar Imagens
3 - Converter Imagem1 para Cinza
4 - Mostrar Imagem1 em Cinza
5 - Histograma das Imagens
6 - Histograma da Imagem Cinza
0 - Sair

🛠️ Passo 7: Desativar o Ambiente Virtual

Quando terminar de usar o ambiente virtual, desative-o com o comando:

Para Windows:
deactivate

Para macOS/Linux:
deactivate

🧪 Testes

Para executar os testes incluídos no projeto, use o comando:

pytest

📋 Contribuições

Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

📜 Licença

Este projeto está licenciado sob a Licença MIT.

📚 Referências

Scikit-Image Documentation

ImageIO Documentation
