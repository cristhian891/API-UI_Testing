@ECHO OFF
setlocal
set Path=C:\Users\crist\AppData\Local\Programs\Python\Python37
python 
endlocal
cd api_tests
cd Tests
python -m pytest
