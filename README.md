# 🖼️ Image Processing Navpack

Um projeto Python para processamento de imagens, utilizando bibliotecas como `scikit-image` e `imageio` para comparar, transformar e salvar imagens.

## 📁 Estrutura do Projeto

```plaintext
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

🚀 Instalação

Clone o Repositório:


Copiar código
git clone https://github.com/Fabianonavarro/image_processing_navpack.git
Navegue para o Diretório do Projeto:

Copiar código
cd image_processing_navpack
Crie e Ative um Ambiente Virtual (opcional, mas recomendado):

Copiar código
python -m venv .venv
source .venv/bin/activate  # No Windows, use `.venv\Scripts\activate`
Instale as Dependências Usando pip:

Copiar código
pip install -r requirements.txt
Instale o Pacote Localmente:

Copiar código
pip install .

🛠️ Uso

Coloque suas Imagens no Diretório image_processing_navpack/imgs.

Execute o Script Principal para Processar as Imagens:

Copiar código

image-processing
Os resultados serão salvos no diretório image_processing_navpack/imgs com os seguintes nomes:

difference_image.jpg
histogram_matched_image.jpg

🧪 Testes

Para executar os testes, use o comando:

bash
Copiar código

pytest

📋 Contribuições

Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.

📜 Licença

Este projeto está licenciado sob a Licença MIT.

📚 Referências

Scikit-Image Documentation
ImageIO Documentation
markdown
Copiar código

### Alterações

1. **Atualizei o comando para executar o script principal** após a instalação do pacote, de acordo com a definição no `setup.py`.
2. **Adicionei uma etapa para instalar o pacote localmente** usando `pip install .` após a instalação das dependências.

Se precisar de mais ajustes ou tiver outras perguntas, só avisar!



