import whisper
import sys
import os

# Caminho do arquivo (argumento ou padrão fixo)
arquivo = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\User\Downloads\2025_05_07_20_08__Web Reposição 30 04_recording 1_d2be9b1b-164c-4599-aec9-d0a92ef88e69_recording.mp4"

# Verifica se o arquivo existe
if not os.path.exists(arquivo):
    print(f"❌ Arquivo não encontrado: {arquivo}")
    sys.exit(1)

# Escolha do modelo (tiny, base, small, medium, large)
modelo_nome = "base"
print(f"🔍 Carregando modelo Whisper ({modelo_nome})...")
modelo = whisper.load_model(modelo_nome)

# Transcrição
print("📝 Transcrevendo, aguarde...\n")
resultado = modelo.transcribe(
    arquivo,
    language="pt",
    verbose=True
)

# Cria pasta de saída se necessário
pasta_saida = "transcriptions"
os.makedirs(pasta_saida, exist_ok=True)

# Monta o nome do arquivo com nome do modelo
nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0] + f"_transcricao_{modelo_nome}.txt"
caminho_saida = os.path.join(pasta_saida, nome_arquivo)

# Salva transcrição
with open(caminho_saida, "w", encoding="utf-8") as f:
    f.write(resultado["text"])

print(f"\n✅ Transcrição salva em: {caminho_saida}")