import cv2
import numpy as np
import os

yol = os.path.realpath(__file__)
k, dosyaAd = os.path.split(yol)
resim = k + "\\" + 'odev3.png'
imgResim = cv2.imread(resim)
if imgResim is None:
    print(f"Dosya bulunamadı: {resim}")
    exit()
griResim = cv2.cvtColor(imgResim, cv2.COLOR_BGR2GRAY)
_, esiklenmisResim = cv2.threshold(griResim, 120, 255, cv2.THRESH_BINARY)
kernel = np.ones((1, 1), np.uint8)
morfolojikResim = cv2.morphologyEx(esiklenmisResim, cv2.MORPH_CLOSE, kernel)
kntr, _ = cv2.findContours(morfolojikResim, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
pirincSay = 0
for kontur in kntr:
    alan = cv2.contourArea(kontur)
    if alan > 80:
        pirincSay += 1
        cv2.drawContours(imgResim, [kontur], -1, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(kontur)
        cv2.rectangle(imgResim, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.namedWindow('bulunmamıs', cv2.WINDOW_NORMAL)
cv2.resizeWindow('bulunmamıs', 700, 500)
cv2.imshow('bulunmamıs', imgResim)
cv2.namedWindow('bulunmus', cv2.WINDOW_NORMAL)
cv2.resizeWindow('bulunmus', 700, 500)
cv2.imshow('bulunmus', morfolojikResim)
print(f"PirinçSayısı -->: {pirincSay}")
cv2.waitKey(0)
cv2.destroyAllWindows()
