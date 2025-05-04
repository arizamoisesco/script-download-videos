import yt_dlp

def descargar_video(url, ruta_descarga='./videos'):
    """
    Descarga un video de YouTube utilizando yt-dlp.
    
    Args:
        url (str): URL del video de YouTube a descargar
        ruta_descarga (str, opcional): Ruta donde se guardará el video. Por defecto es el directorio actual.
    """
    # Configuración de opciones para la descarga
    opciones = {
        # Formato de video preferido
        #'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'format': 'bv*+ba',
        
        # Configuración de ruta de descarga
        'outtmpl': f'{ruta_descarga}/%(title)s.%(ext)s',
        
        # Límite de velocidad de descarga (opcional, en bytes/s)
        # 'ratelimit': 1000000,  # Descomentar si se quiere limitar la velocidad
        
        # Ignorar errores para continuar la descarga
        'ignoreerrors': False,
        
        # Progreso de descarga
        'progress_hooks': [progreso_descarga]
    }
    
    try:
        # Crear el objeto yt-dlp con las opciones
        with yt_dlp.YoutubeDL(opciones) as ydl:
            # Extraer información del video
            info_video = ydl.extract_info(url, download=True)
            
            # Obtener el título del video descargado
            titulo = info_video.get('title', 'video_sin_titulo')
            print(f"Video descargado: {titulo}")
    
    except Exception as e:
        print(f"Error al descargar el video: {e}")

def progreso_descarga(descarga):
    """
    Función de callback para mostrar el progreso de descarga.
    
    Args:
        d (dict): Diccionario con información de progreso
    """
    if descarga['status'] == 'downloading':
        # Mostrar porcentaje de descarga si está disponible
        p = descarga.get('_percent_str', 'N/A')
        print(f"Descargando: {p}")
    
    elif descarga['status'] == 'finished':
        print("Descarga completada!")

# Ejemplo de uso
if __name__ == "__main__":
    url_video = input("Introduce la URL del video de YouTube: ")
    descargar_video(url_video)