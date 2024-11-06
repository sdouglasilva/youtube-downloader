import yt_dlp

def baixar_video(url, caminho_destino="."):
    ydl_opts = {
        'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    caminho_destino = input("Digite o caminho de destino (ou pressione Enter para usar a pasta atual): ") or "."
    baixar_video(url, caminho_destino)
