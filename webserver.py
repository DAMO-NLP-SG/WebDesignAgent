from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from PIL import Image
import time
import os
import io

class Webserver:
    def __init__(self, save_file = "saves/"):
        # 判断save_file是否为绝对路径
        if os.path.isabs(save_file):
            download_dir = save_file
        else:
            # 构建完整的保存路径，确保跨平台兼容性
            download_dir = os.path.join(os.getcwd(), save_file)
        options = Options()
        options.add_argument("start-maximized")  # 可选：最大化浏览器窗口
        options.add_experimental_option("prefs", {
            "download.default_directory": f"{download_dir}",  # 示例：设置默认下载目录，根据需要修改
            "directory_upgrade": True,
            "safebrowsing.enabled": True,
        })
        
        # 使用webdriver_manager来管理ChromeDriver的路径
        print("Initializing WebDriver")
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        print("Successfully installed ChromeDriver")

        # 初始化WebDriver，配置为可以打开本地文件
        self.driver = webdriver.Chrome(service=service, options=options)    
        self.save_file = save_file
        print("suceessfully initialized WebDriver")   


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
