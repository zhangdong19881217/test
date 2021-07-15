cd /d %~dp0
::pyinstaller --hidden-import=queue -w -F main.py
pyinstaller -F -w -i   2.ico main.py 
::pyinstaller -D -w -i   2.ico main.py 
echo  Press any key & pause
exit 