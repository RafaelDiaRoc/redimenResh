import os
from tkinter import filedialog, Tk
from datetime import datetime
from PIL import Image

def redimensionar_imagem(entrada, saida, largura, altura, qualidade):
    try:
        # Abre a imagem
        imagem = Image.open(entrada)

        # Redimensiona a imagem usando o algoritmo Lanczos
        nova_imagem = imagem.resize((largura, altura), Image.LANCZOS)

        # Converte a imagem para o modo RGB (sem canal alfa)
        nova_imagem = nova_imagem.convert("RGB")

        # Salva a nova imagem com a qualidade especificada
        nova_imagem.save(saida, quality=qualidade)

        print(f'Imagem redimensionada e salva em {saida} com qualidade {qualidade} e algoritmo Lanczos')

    except Exception as e:
        print(f"Erro: {e}")

def selecionar_arquivos():
    root = Tk()
    root.withdraw()

    arquivos = filedialog.askopenfilenames(
        title="Selecione os arquivos a serem redimensionados",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif")]
    )

    return arquivos

def obter_dimensoes():
    largura = int(input("Digite a largura desejada: "))
    altura = int(input("Digite a altura desejada: "))
    return largura, altura

def selecionar_pasta_destino():
    root = Tk()
    root.withdraw()

    pasta_destino = filedialog.askdirectory(title="Selecione a pasta de destino")

    return pasta_destino

def escolher_algoritmo():
    algoritmos_disponiveis = [Image.NEAREST, Image.BOX, Image.BILINEAR, Image.HAMMING, Image.BICUBIC, Image.LANCZOS]
    print("Escolha o algoritmo de redimensionamento:")
    for i, algoritmo in enumerate(algoritmos_disponiveis, start=1):
        print(f"{i}. {algoritmo}")

    escolha = int(input("Digite o número correspondente ao algoritmo desejado: "))
    algoritmo_escolhido = algoritmos_disponiveis[escolha - 1]

    return algoritmo_escolhido

def gerar_nome_saida(pasta_destino):
    data_atual = datetime.now().strftime("%d.%m.%Y")
    sugestao_nome = f"{data_atual}"
    extensao = ".png"

    nome_saida = sugestao_nome + extensao

    contador = 1
    while os.path.exists(os.path.join(pasta_destino, nome_saida)):
        nome_saida = f"{sugestao_nome}_{contador:04d}{extensao}"
        contador += 1

    return nome_saida

if __name__ == "__main__":
    arquivos_selecionados = selecionar_arquivos()
    nova_largura, nova_altura = obter_dimensoes()
    pasta_destino = selecionar_pasta_destino()
    qualidade = 100

    for caminho_entrada in arquivos_selecionados:
        nome_saida = gerar_nome_saida(pasta_destino)
        caminho_saida = os.path.join(pasta_destino, nome_saida)

        redimensionar_imagem(caminho_entrada, caminho_saida, nova_largura, nova_altura, qualidade)
