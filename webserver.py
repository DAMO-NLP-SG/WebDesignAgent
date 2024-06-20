import yaml
from selenium import webdriver
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

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    print(cfg)

class Webserver:
    def __init__(self, save_file="saves/"):
        if os.path.isabs(save_file):
            download_dir = save_file
        else:
            download_dir = os.path.join(os.getcwd(), save_file)
        
        web_type = cfg["web_type"]

        if web_type == "chrome":
            options = ChromeOptions()
            options.add_argument("start-maximized")  
            options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,  
                "directory_upgrade": True,
                "safebrowsing.enabled": True,
            })
            driver_path = ChromeDriverManager().install()
            service = ChromeService(driver_path)
            self.driver = webdriver.Chrome(service=service, options=options)
        elif web_type == "firefox":
            options = FirefoxOptions()
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.manager.showWhenStarting", False)
            options.set_preference("browser.download.dir", download_dir)  
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver_path = GeckoDriverManager().install()
            service = FirefoxService(driver_path)
            self.driver = webdriver.Firefox(service=service, options=options)
        elif web_type == "edge":
            options = EdgeOptions()
            options.add_argument("start-maximized") 
            options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,  
                "directory_upgrade": True,
                "safebrowsing.enabled": True,
            })
            driver_path = EdgeChromiumDriverManager().install()
            service = EdgeService(driver_path)
            self.driver = webdriver.Edge(service=service, options=options)
        else:
            raise ValueError(f"Unsupported web browser type: {web_type}")

        self.save_file = save_file
        print("Successfully initialized WebDriver")

    def get_screenshot(self, local_html_path , save_path = None):
        if save_path is None:
            save_path = os.path.join(self.save_file, "screenshot.png")
        try:
            if os.path.isabs(local_html_path):
                html_path = local_html_path
            else:
                html_path = os.path.join(os.getcwd() ,local_html_path)
            # 使用file协议打开本地HTML文件
            print(f"Opening local HTML file {html_path}")
            self.driver.get("file:///" + html_path.replace("\\", "/"))
            # 等待页面加载完成，根据实际情况调整等待时间
            time.sleep(15)
            # 截图并保存
            scroll_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            window_height = self.driver.execute_script("return window.innerHeight")
            window_width = self.driver.execute_script("return window.innerWidth")
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
            if img.size[1] > 10000:
                stitched_image = stitched_image.resize((img.size[0] // 2, img.size[1] // 2))
            stitched_image.save(save_path)
            print(f"Screenshot of local HTML saved as {save_path}")
        finally:
            pass
    
    def open_website(self, local_html_path):
        if os.path.isabs(local_html_path):
            html_path = local_html_path
        else:
            html_path = os.path.join(os.getcwd(), local_html_path)
        self.driver.get("file:///" + html_path.replace("\\", "/"))


    def stop(self):
        self.driver.quit()
        print("WebDriver stopped")
