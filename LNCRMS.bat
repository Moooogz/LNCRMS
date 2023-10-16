@ECHO OFF
start cmd.exe /C "cd .. && virt\Scripts\activate && cd lncrms && python manage.py runserver"
start C:\"Program Files"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/"
