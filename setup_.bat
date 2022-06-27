python -m pip install pystyle
python -m pip install pytube
python -m pip install instaloader
cls
echo python DOWNLOADER.py >> start.bat
start start.bat
start /b "" cmd /c del "%~f0"&exit /b