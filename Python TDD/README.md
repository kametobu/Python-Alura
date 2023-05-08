#Pytest args
pytest -v   --> Verbose
pytest -k   --> filter name function test
pytest -m   --> mark run select filter for decorator
#Coverange
pip install pytest-cov==3.0.0
pytest --cov=folder skip_folder/
#Relatorio
pytest --cov=folder skip_folder/ --cov-report term-missing
pytest --cov=folder skip_folder/ --cov-report html
pytest --junitxml report.xml
pytest --cov-report xml