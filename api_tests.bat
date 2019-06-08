@ECHO OFF
setlocal
set PYTHONPATH="C:\Users\crist\AppData\Local\Programs\Python\Python37"
endlocal
cd api_tests
cd Tests
python -m pytest
