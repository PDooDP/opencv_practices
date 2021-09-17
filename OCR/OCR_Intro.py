import pytesseract
from PIL import Image

# 文字辨識

# 辨識英文
# image = Image.open(r"paragraph.jpg")
# code = pytesseract.image_to_string(image)
# print(code)

# 辨識繁體中文
# 字體越大，辨識度越好
chi = Image.open(r"chinese2_1.png")
chi_code = pytesseract.image_to_string(chi, lang="chi_tra")
print(chi_code)
