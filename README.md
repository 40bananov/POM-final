Автоматизация тестирования.  
Требования:  
python 3.8.0  
pytest 5.3.5  
selenium 3.141.0  
Ключи запуска:  
python3 -m pytest -v -s --tb=line test_main_page.py  
python3 -m pytest -v -s --tb=line test_product_page.py  
python3 -m pytest -v --tb=line --language=en -m need_review  
  
python3 -m pytest --alluredir=/tmp/my_allure_results test_dog_api.py  
sh allure serve /tmp/my_allure_results  
