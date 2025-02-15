from imutils import perspective
from skimage.filters import threshold_local
import cv2
import imutils

# 边缘扫描
image = cv2.imread("12345.bmp")
cv2.imshow('1',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
ratio = image.shape[0] / 500.0# 比例
orig = image.copy()
image = imutils.resize(image, height=500)

# 灰度转换及边缘查找
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)# 边缘检测

# 只保留轮廓
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # 通过边缘图像找到轮廓
cnts = cnts[0]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]  # 保留最大轮廓

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)# 轮廓点
    if len(approx) == 4: # 表明找到四个轮廓点
        screenCnt = approx
    break

# 转为鸟瞰图
warped = perspective.four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY) # 灰度转换
T = threshold_local(warped, 11, offset=10, method="gaussian")
warped = (warped > T).astype("uint8") * 255

cv2.imshow("Original", imutils.resize(orig, height=650))
cv2.imshow("Scanned", imutils.resize(warped, height=650))
cv2.waitKey(0)
