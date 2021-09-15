import cv2
ESC = 27

# 哈爾特徵正臉分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# CSRT追蹤演算法
tracker = cv2.TrackerCSRT_create()
cap = cv2.VideoCapture(0)
initTracker = None

while True:
    # 如果取得影像 ret = true, frame則是儲存取得的影像資料 
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 300))
    # 鏡像
    frame = cv2.flip(frame, 1)
    
    if initTracker is None:
        # 將取得的影像轉成灰階, 方便黑白色的區域的像素轉換成特徵值
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 尋找影像內的人臉
        faces = face_cascade.detectMultiScale(gray, 1.05, 3)
        
        # 用迴圈找出從臉部左上角座標(x,y)和長寬範圍(w, h)繪出一個矩形
        for (x, y, w, h) in faces:
            try:
                initTracker = (x, y, w, h)
                tracker.init(frame, initTracker)
            except:
                continue
                
    else:
        # 追蹤演算法的update函數計算新區域的座標
        success, rect = tracker.update(frame)
        if success:
            # opencv的畫矩形函數
            (x, y, w, h) = [int(i) for i in rect]
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break
    

