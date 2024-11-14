# Konwerter FLAC do MP3

Skrypt konwertujący pliki FLAC do formatu MP3 z wysoką jakością (320kbps). Program automatycznie konwertuje wszystkie pliki FLAC z wybranego folderu, zachowując oryginalne metadane.

## Wymagania systemowe

- Windows
- Python 3.12.7 (sprawdzona wersja)
- ffmpeg (instrukcja instalacji poniżej)

## Instalacja ffmpeg

1. Najpierw zainstaluj Chocolatey (menedżer pakietów dla Windows):
   - Uruchom PowerShell jako administrator (kliknij prawym na PowerShell i wybierz "Uruchom jako administrator")
   - Wklej i wykonaj poniższą komendę:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
   - Zamknij PowerShell

2. Instalacja ffmpeg:
   - Otwórz nowe okno PowerShell jako administrator
   - Wpisz i wykonaj:
   ```powershell
   choco install ffmpeg
   ```

## Jak używać

1. Pobierz plik `flac_converter.py`

2. Otwórz plik w edytorze tekstu i zmień ścieżki do folderów:
   ```python
   if __name__ == '__main__':
       input_directory = r"ŚCIEŻKA\DO\FOLDERU\Z\PLIKAMI\FLAC"
       output_directory = r"ŚCIEŻKA\DO\FOLDERU\WYJŚCIOWEGO\MP3"
   ```
   
   Na przykład:
   ```python
   if __name__ == '__main__':
       input_directory = r"E:\muzyka\Big Room House\flaki"
       output_directory = r"E:\muzyka\Big Room House\mp3"
   ```

3. Uruchom skrypt:
   - Otwórz terminal/PowerShell w folderze ze skryptem
   - Wykonaj komendę:
   ```bash
   python flac_converter.py
   ```

## Co robi skrypt?

1. Sprawdza czy ffmpeg jest zainstalowany
2. Tworzy folder wyjściowy jeśli nie istnieje
3. Znajduje wszystkie pliki .flac w podanym folderze
4. Konwertuje je do MP3 (320kbps) zachowując:
   - Nazwy plików
   - Metadane (tagi ID3)
5. Wyświetla postęp konwersji

## Rozwiązywanie problemów

1. Jeśli pojawia się błąd "ffmpeg nie jest zainstalowany":
   - Sprawdź czy wykonałeś wszystkie kroki instalacji ffmpeg
   - Spróbuj zamknąć i otworzyć ponownie PowerShell/terminal
   - Sprawdź czy ffmpeg działa wpisując `ffmpeg -version` w terminalu

2. Jeśli Python nie jest rozpoznawany:
   - Upewnij się, że zainstalowałeś Python 3.12.7
   - Sprawdź czy Python jest dodany do zmiennej środowiskowej PATH
   - Spróbuj użyć komendy `py` zamiast `python`

## Wsparcie

Jeśli napotkasz problemy lub masz pytania, utwórz nowy issue w tym repozytorium.