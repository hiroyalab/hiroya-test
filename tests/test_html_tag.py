from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from hiroyap.helper import Helper
import time

class TestHtmlTag():
    def test_テキスト(self, helper: Helper):
        helper.write_md('テキストタグのURLゲット\n')
        helper.get('https://web-designer.cman.jp/html_ref/abc_list/input_text/')
        helper.write_md('テキストに値をセット\n')
        helper.set_val(By.XPATH, '//*[@id="tmContMain"]/div[2]/div[2]/input', 'text')
        helper.write_md('テキストに値をセット\n')
        helper.set_val(By.XPATH, '//*[@id="tmContMain"]/div[3]/div[2]/input', 'text')
        # disabledのタグはエラー
        # helper.set_val(By.XPATH, '//*[@id="tmContMain"]/div[4]/div[2]/input', 'text')
        # readonlyのタグはエラー
        # helper.set_val(By.XPATH, '//*[@id="tmContMain"]/div[5]/div[2]/input', 'text')
    
    def test_password(self, helper: Helper):
        helper.get('https://web-designer.cman.jp/html_ref/abc_list/input_password/')
        helper.set_val(By.XPATH, '//*[@id="tmContMain"]/div[2]/div[2]/input', 'password')
    
    def test_ラジオボタン(self, helper: Helper):
        helper.get('https://web-designer.cman.jp/html_ref/abc_list/input_radio/')
        helper.check(By.XPATH, '//*[@id="tmContMain"]/div[2]/div[2]/input[2]')
        helper.check(By.XPATH, '//*[@id="tmContMain"]/div[7]/div/div[2]/label[2]')

    def test_チェックボックス(self, helper: Helper):
        helper.get('https://web-designer.cman.jp/html_ref/abc_list/input_checkbox/')
        helper.check(By.XPATH, '//*[@id="tmContMain"]/div[2]/div[2]/input[2]')
        helper.check(By.XPATH, '//*[@id="tmContMain"]/div[7]/div/div[2]/label[1]')
    
    # def test_hidden(self, helper: Helper):
    #     helper.get('https://web-designer.cman.jp/html_ref/abc_list/input_hidden/')
    #     # helper.set_val('//*[@id="tmContMain"]/div[2]/div[2]/input', 'hidden')
    #     # hiddenも流石に無理
    #     # やるなら要素取って以下みたいにするかな？
    #     elem = helper.driver.find_element(By.XPATH, '//*[@id="tmContMain"]/div[2]/div[2]/input')
    #     helper.driver.execute_script("arguments[0].setAttribute('value', 'hidden')", elem)

    def test_セレクト(self, helper: Helper):
        helper.get('https://web-designer.cman.jp/html_ref/abc_list/select/')
        
        helper.select(By.XPATH, '//*[@id="tmContMain"]/div[3]/div[2]/select', '3')
        helper.select(By.XPATH, '//*[@id="tmContMain"]/div[3]/div[2]/select', '2')
        
        helper.select(By.XPATH, '//*[@id="tmContMain"]/div[4]/div[2]/select', '4')
        helper.select(By.XPATH, '//*[@id="tmContMain"]/div[4]/div[2]/select', '1')

    def test_テキストエリア(self, helper: Helper):
        helper.get('https://web-designer.cman.jp/html_ref/abc_list/textarea/')
        helper.set_val(By.XPATH, '//*[@id="tmContMain"]/div[3]/div/div[2]/textarea', "text \narea")
        
    def test_ファイルアップロード(slef, helper:Helper):
        helper.get('https://web-designer.cman.jp/html_ref/abc_list/input_file/')
        helper.upload(By.XPATH, '//*[@id="tmContMain"]/div[2]/div[2]/input', 'slideshow.png')
    
        