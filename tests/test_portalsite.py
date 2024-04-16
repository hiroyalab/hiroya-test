from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from hiroyap.helper import Helper

db_use = False
db_type = 'db2'
username = 'username'
userpwd = 'password'
host = '127.0.0.1'
port = 50000
service_name = 'dbname'

class TestIt01Class():
    def test_01_01_ホーム画面レイアウト確認(self, helper: Helper):
        helper.write_md('#### レイアウト確認')
        helper.get('http://biz.taiken.cmskit.jp/index.html')        
    
    def test_01_02_ホーム画面グローバルナビ遷移(self, helper: Helper):
        helper.write_md('#### サイト表示')
        helper.get('http://biz.taiken.cmskit.jp/index.html')
        helper.write_md('#### 商品紹介クリック')
        helper.click(By.XPATH, '//*[@id="globalnavi-products"]/a/img')
        helper.write_md('#### バイヤー紹介クリック')
        helper.click(By.XPATH, '//*[@id="globalnavi-buyer"]/a/img')
        helper.write_md('#### キャンペーンクリック')
        helper.click(By.XPATH, '//*[@id="globalnavi-campaign"]/a/img')
        helper.write_md('#### ショップリストクリック')
        helper.click(By.XPATH, '//*[@id="globalnavi-shop"]/a/img')
        helper.write_md('#### サイトロゴクリック')
        helper.click(By.XPATH, '//*[@id="header-logo"]/a/img')

    def test_01_03_ヘッダー検索(self, helper: Helper):
        helper.write_md('#### サイト表示')
        helper.get('http://biz.taiken.cmskit.jp/index.html')
        helper.write_md('#### 検索項目にテキスト入力')
        helper.set_val(By.XPATH, '//*[@id="searchform-textarea"]', 'クリスマス')
        helper.write_md('#### 検索ボタン押下')
        helper.click(By.XPATH, '//*[@id="searchform-btn"]')
        helper.write_md('#### 検索結果のリンク押下')
        helper.click(By.XPATH, '//*[@id="content"]/dl/dt[1]/a')
    
    def test_01_04_別タブ遷移確認(self, helper: Helper):
        helper.write_md('#### サイト表示')
        helper.get('http://biz.taiken.cmskit.jp/index.html')
        helper.write_md('#### キャンペーンページのリンク画像クリック')     
        helper.click(By.XPATH, '//*[@id="home-campaign-inner"]/p[1]/a/img')
        helper.write_md('#### 開いたタブを閉じて、元のタブに戻る')
        helper.close_window()


class TestIt02Class():
    def test_02_01_商品紹介画面レイアウト確認(self, helper: Helper):
        helper.write_md('#### レイアウト確認')
        helper.get('http://biz.taiken.cmskit.jp/product/index.html')
    
    def test_02_02_サイドメニュー押下(self, helper: Helper):
        helper.write_md('#### レイアウト確認')
        helper.get('http://biz.taiken.cmskit.jp/product/index.html')
        helper.write_md('#### サイドメニューのキャンドルホルダー押下')
        helper.click(By.XPATH, '//*[@id="sidenavi"]/li/ul/li[2]/a')
        helper.write_md('#### サイドメニューの商品紹介押下')
        helper.click(By.XPATH, '//*[@id="sidenavi"]/li/a')
        