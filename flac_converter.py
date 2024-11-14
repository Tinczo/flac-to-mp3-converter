import os
from pathlib import Path
import subprocess
from concurrent.futures import ThreadPoolExecutor
import shutil

def convert_flac_to_mp3(input_file: Path, output_dir: Path) -> None:
    """
    Konwertuje pojedynczy plik FLAC do MP3 używając ffmpeg.
    
    Args:
        input_file: Ścieżka do pliku FLAC
        output_dir: Katalog docelowy dla pliku MP3
    """
    output_file = output_dir / f"{input_file.stem}.mp3"
    
    cmd = [
        'ffmpeg',
        '-i', str(input_file),
        '-codec:a', 'libmp3lame',
        '-b:a', '320k',
        '-map_metadata', '0',
        '-id3v2_version', '3',
        str(output_file)
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"Przekonwertowano: {input_file.name}")
    except subprocess.CalledProcessError as e:
        print(f"Błąd podczas konwersji {input_file.name}: {e}")

def batch_convert_flac_to_mp3(input_dir: str, output_dir: str, max_workers: int = 4) -> None:
    """
    Konwertuje wszystkie pliki FLAC z folderu wejściowego do MP3 w folderze wyjściowym.
    
    Args:
        input_dir: Ścieżka do folderu z plikami FLAC
        output_dir: Ścieżka do folderu wyjściowego dla plików MP3
        max_workers: Maksymalna liczba równoległych konwersji
    """

    if shutil.which('ffmpeg') is None:
        raise RuntimeError("ffmpeg nie jest zainstalowany. Zainstaluj ffmpeg aby kontynuować.")
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Znajdź wszystkie pliki FLAC
    flac_files = list(input_path.glob('*.flac'))
    
    if not flac_files:
        print("Nie znaleziono plików FLAC w podanym folderze.")
        return
    
    print(f"Znaleziono {len(flac_files)} plików FLAC do konwersji.")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for flac_file in flac_files:
            executor.submit(convert_flac_to_mp3, flac_file, output_path)
    
    print("\nKonwersja zakończona!")

if __name__ == '__main__':
    input_directory = r"E:\muzyka\Custom Party Set\flaki"
    output_directory = r"E:\muzyka\Custom Party Set\mp3"
    
    try:
        batch_convert_flac_to_mp3(input_directory, output_directory)
    except Exception as e:
        print(f"Wystąpił błąd: {e}")