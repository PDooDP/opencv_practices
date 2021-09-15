import cv2

cap = cv2.VideoCapture('vtest.avi')

# CSRT 物體追蹤演算法
tracker = cv2.TrackerCSRT_create()
roi = None
while True:
    # 如果成功取得到影像, 則ret為True, frame儲存取得的影像資料
    ret, frame = cap.read()
 
    # roi, region of interest
    if roi is None:
        # selectROI允許使用者畫出一個矩形的區域
        roi = cv2.selectROI('frame', frame)
        if roi != (0, 0, 0, 0):
            tracker.init(frame, roi)
            
    # update函數計算新區域的座標
    success, rect = tracker.update(frame)
    if success: 
        # 將座標傳給opencv畫矩形的函數
        (x, y, w, h) = [int(i) for i in rect]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(66) == 27:   # 27 = ESC
        cv2.destroyAllWindows()
        break
