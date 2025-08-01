# Projeto Transcritor de Áudio com Whisper

## Descrição

Este projeto utiliza a biblioteca Whisper da OpenAI para transcrição de arquivos de áudio ou vídeo (formato .mp4). A transcrição é salva em um arquivo de texto e exibida no terminal.

### Requisitos:
- Python 3.11: [Download aqui](https://www.python.org/downloads/)
- Chocolatey para instalação do FFmpeg

---

## 📦 Estrutura do Projeto

```
/trascritor
├── .venv/
├── transcritor.py
└── README.md
```

---

## ✅ 1. Criação do Ambiente Virtual (venv)

1. Navegar até a pasta do projeto:

```bash
cd C:\projects\trascritor
```

2. Criar o ambiente virtual (Python 3.11):

```bash
C:\Users\your_user\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv
```

3. Ativar o ambiente:

```bash
.venv\Scripts\Activate.ps1
```

---

## 🔄 2. Atualização das Ferramentas do Ambiente

Atualizar pip, wheel e setuptools:

```bash
python -m pip install --upgrade pip wheel setuptools
```

---

## 📦 3. Instalação dos Pacotes Necessários

Instalar as bibliotecas:

```bash
pip install whisper openai-whisper ffmpeg-python certifi 
```

### Descrição dos pacotes:
- **openai-whisper**: Biblioteca de transcrição por IA.
- **ffmpeg-python**: Interface Python para FFmpeg.
- **certifi**: Bundle de certificados SSL.

---

## 🎯 5. Instalação do FFmpeg

Se o Chocolatey não estiver instalado:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
    [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Em seguida, instale o FFmpeg:

```powershell
choco install ffmpeg
```

Caso já tenha o Chocolatey instalado:

```powershell
choco install ffmpeg
```

---

## 🚀 6. Executar o Script

1. Passe o caminho para o arquivo .mp4 e rode o comando:

```bash
arquivo = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\your-User\Downloads\2025_05_07_20_08__Web Reposição 30 04_recording 1_d2be9b1b-164c-4599-aec9-d0a92ef88e69_recording.mp4"
py transcritor.py
```

2. Ou passe o caminho diretamente no terminal. Exemplo:

```bash
python .\transcritor.py "C:\Users\your-User\Downloads\[ACT- R] - Mapeamento do processo ELERA - 2024_12_18 13_58 GMT-03_00 - Recording.mp4"
```

A transcrição será salva no mesmo diretório do arquivo original, com a extensão `.txt`.