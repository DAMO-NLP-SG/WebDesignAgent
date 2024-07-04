import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from PIL import Image
import time
import os
import io

with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

class Webserver:
    def __init__(self, save_file="saves/"):
        if os.path.isabs(save_file):
            download_dir = save_file
        else:
            download_dir = os.path.join(os.getcwd(), save_file)
        
        web_type = cfg.get("web_type", "chrome")
        self.web_type = web_type
        if web_type == "chrome":
            options = ChromeOptions()
            options.add_argument("start-maximized")  
            options.add_argument("--headless")  
            options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,  
                "directory_upgrade": True,
                "safebrowsing.enabled": True,
            })
            print("begin install the chrome manager")
            driver_path = ChromeDriverManager().install()
            print("successfully install the chrome manager")
            service = ChromeService(driver_path)
            self.driver = webdriver.Chrome(service=service, options=options)

            preview_options = ChromeOptions()
            preview_options.add_argument("start-maximized")
            self.preview_driver = webdriver.Chrome(service=service, options=preview_options)

        elif web_type == "firefox":
            options = FirefoxOptions()
            options.add_argument("headless")
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.dir", download_dir)  
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            print("begin install the firefox manager")
            driver_path = GeckoDriverManager().install()
            print("successfully install the firefox manager")
            service = FirefoxService(driver_path)
            self.driver = webdriver.Firefox(service=service, options=options)

            preview_options = FirefoxOptions()
            preview_options.add_argument("start-maximized")
            self.preview_driver = webdriver.Firefox(service=service, options=preview_options)

        elif web_type == "edge":
            options = EdgeOptions()
            options.add_argument("headless")
            options.add_argument("start-maximized") 
            options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,  
                "directory_upgrade": True,
                "safebrowsing.enabled": True,
            })
            print("begin install the edge manager")
            driver_path = EdgeChromiumDriverManager().install()
            print("successfully install the edge manager")
            service = EdgeService(driver_path)
            self.driver = webdriver.Edge(service=service, options=options)

            preview_options = EdgeOptions()
            preview_options.add_argument("start-maximized")
            self.preview_driver = webdriver.Edge(service=service, options=preview_options)
        else:
            raise ValueError(f"Unsupported web browser type: {web_type}")

        self.save_file = save_file
        print("Successfully initialized WebDriver")

    def get_screenshot(self, local_html_path , save_path = None , is_local = True):
        if save_path is None:
            save_path = os.path.join(self.save_file, "screenshot.png")
        try:
            if is_local:
                if os.path.isabs(local_html_path):
                    html_path = local_html_path
                else:
                    html_path = os.path.join(os.getcwd() ,local_html_path)
                # 使用file协议打开本地HTML文件
                print(f"Opening local HTML file {html_path}")
                self.driver.get("file:///" + html_path.replace("\\", "/"))
                time.sleep(5)
            else:
                print(f"Opening website {local_html_path}")
                self.driver.get(local_html_path)
                time.sleep(15)
            # 截图并保存
            if self.web_type in ["chrome","firefox","edge"]:
                try:
                    alert = self.driver.switch_to.alert
                    alert.accept()
                except Exception as e:
                    pass
                screen_width = self.driver.execute_script("return window.screen.width")
                scroll_height = self.driver.execute_script("return document.documentElement.scrollHeight")
                # scroll_width = self.driver.execute_script("return document.documentElement.scrollWidth")
                self.driver.set_window_size(screen_width, scroll_height)
                self.driver.save_screenshot(save_path)
            else:
                self.driver.fullscreen_window()
                window_height = self.driver.get_window_size()["height"]
                window_width = self.driver.get_window_size()["width"]
                scroll_height = self.driver.execute_script("return document.body.scrollHeight")        
                stitched_image = Image.new('RGB', (window_width, scroll_height))
                for y in range(0, scroll_height, window_height):
                    self.driver.execute_script(f"window.scrollTo(0, {y});")
                    time.sleep(0.5)
                    img = Image.open(io.BytesIO(self.driver.get_screenshot_as_png())).resize((window_width, window_height))
                    if y + window_height > scroll_height:
                        img = img.crop((0, window_height - scroll_height + y, window_width, scroll_height))
                        stitched_image.paste(img, (0, y))
                        break
                    stitched_image.paste(img, (0, y))
                    stitched_image.save(save_path)
            img = Image.open(save_path)
            if img.size[1] > 10000:
                img = img.resize((img.size[0] // 2, img.size[1] // 2))
            img.save(save_path)
            print(f"Screenshot of local HTML saved as {save_path}")
        finally:
            pass
    
    def open_website(self, local_html_path):
        if os.path.isabs(local_html_path):
            html_path = local_html_path
        else:
            html_path = os.path.join(os.getcwd(), local_html_path)
        self.preview_driver.get("file:///" + html_path.replace("\\", "/"))


    def stop(self):
        self.driver.quit()
        print("WebDriver stopped")

if __name__ == "__main__":
    webserver = Webserver()
    webserver.get_screenshot("https://tb.alicdn.com/","taobao.png",is_local = False)
    webserver.stop()