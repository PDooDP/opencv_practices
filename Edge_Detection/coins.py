import cv2
img_name = input("請輸入圖片名稱 (含副檔名): ")
image = cv2.imread(img_name)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (13, 13), 0)  # 使用高斯模糊去除微小雜訊或圖案

edged = cv2.Canny(gray, 15, 20)
# (低閥值, 高閥值)
# 比第一個參數低, 就不是邊緣
# 比第二個參數高, 就是邊緣

#cv2.imshow(edged)

# 在樹莓派裡執行需要多加 edged
# edged, contours, hierarchy = cv2. findContours(

contours, hierarchy = cv2.findContours(
    edged,
    cv2.RETR_TREE, # 尋找所有可能的邊緣特徵
    # cv2.RETR_EXTERNAL, # 此參數只會得到最外圍的框線
    cv2.CHAIN_APPROX_SIMPLE)

# 用hconcat() 將原本的圖片與現有的畫布合併在一起
out = image.copy()
out.fill(0)

# cv2.drawContours(image, contours, -1, (0, 255, 128), 2) # 直接在原圖檔上畫出輪廓
cv2.drawContours(out, contours, -1, (0, 255, 128), 1)

final_image = cv2.hconcat([image, out])

cv2.imshow("image", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
