Create a virtual environment and install behave and selenium to execute.

pip install behave
pip install selenium

Finally, Execute this with following command:

$  behave -f allure_behave.formatter:AllureFormatter -o reporTest\ ./features

$ allure serve \reporTest

report will be generated to C:\Users\shail\AppData\Local\Temp\3609749911560213999\allure-report
