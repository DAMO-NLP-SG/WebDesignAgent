process_img_en = """
Your task is to give a brief description of the above picture. Please keep it as short as possible and do not output other content, please output both Chinese and English descriptions, the output format is as follows:
<Chinese>{Your Chinese description of the picture}</Chinese>
<English>{Your English description of the picture}</English>
"""

process_img_zh = """
您的任务是对上图进行简要描述。请尽量简短，不要输出其他内容,请输出中文跟英文两种描述，输出格式如下：
<Chinese>{你对图片的中文描述}</Chinese>
<English>{你对图片的英文描述}</English>
"""

def get_process_img_prompt(language="en"):
    if language == "en":
        return process_img_en
    else:
        return process_img_zh