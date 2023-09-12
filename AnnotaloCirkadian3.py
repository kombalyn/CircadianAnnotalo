
# parameterek definialasa
file_name = "/media/nas/PUBLIC/Circadian_PIC_Videos/videos/60AA/NVR_ch2_main_20230818123500_20230818124000.dav"
FPS = 25
sebesseg = 50 # 0-tol 50-ig allithato

if 50<sebesseg:
    sebesseg = 50 
if sebesseg<0:
    sebesseg=0

import cv2 # szukseges package importalasa
import numpy as np # szukseges package importalasa

# Video stream definialasa
cap = cv2.VideoCapture(cv2.samples.findFile(file_name))

# Megszamoljuk hany frame van a videoban
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1
print(f"A videó {frame_count} frame-et tartalmaz.")

# Függvény a gombokhoz tartozó események kezelésére
def button_click(event, x, y, flags, param):
    global selected_option
    if event == cv2.EVENT_LBUTTONDOWN:
        # Ellenőrizzük, melyik gomb lett megnyomva
        if 50 <= x <= 200 and 50 <= y <= 100:
            selected_option = 1
        elif 250 <= x <= 400 and 50 <= y <= 100:
            selected_option = 2
        elif 450 <= x <= 600 and 50 <= y <= 100:
            selected_option = 3
        elif 50 <= x <= 200 and 150 <= y <= 200:
            selected_option = 4
        elif 250 <= x <= 400 and 150 <= y <= 200:
            selected_option = 5
        elif 450 <= x <= 600 and 150 <= y <= 200:
            selected_option = 6

def display_Panel():
    global selected_option
    
    # Inicializáljuk a változót a kiválasztott opció számával
    selected_option = None
    
    # Címkék és koordináták a gombokhoz
    button_labels = ["Csendes-Alvas", "Aktiv-Alas", "Atmeneti", "Csendes-Eber", "Aktiv-Eber", "Siras"]
    button_coordinates = [(50, 100), (250, 100), (450, 100), (50, 200), (250, 200), (450, 200)]
    
    # Kép létrehozása és hozzáadása
    width, height = 700, 300
    image = np.zeros((height, width, 3), dtype=np.uint8)  # Fekete háttér
    cv2.namedWindow('Options')
    cv2.setMouseCallback('Options', button_click)
    
    # Gombok rajzolása
    for label, (x, y) in zip(button_labels, button_coordinates):
        cv2.rectangle(image, (x, y - 50), (x + 150, y), (0, 255, 0), -1)
        cv2.putText(image, label, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        
    while True:
        cv2.imshow('Options', image)
        key = cv2.waitKey(1) & 0xFF
        if selected_option is not None:
            print(f"Kiválasztott opció: {selected_option}")
            break
        if key == 27:  # Esc gomb lenyomása
            break
        
    return selected_option

# Video stream ujrainicializalasa a szamlalas utan
cap = cv2.VideoCapture(cv2.samples.findFile(file_name))

# Futtatas az egesz dav fajlra
counter = 0
for i in range(frame_count):
    ret, frame2 = cap.read()
    frame2 = cv2.resize(frame2, (500,500))
    if not ret:
        print('No frames grabbed!')
        break
    cv2.imshow('frame',frame2)
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(51-sebesseg) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png', frame2)
    prvs = next
    if(i!=0 and (i%1500==0 or i==(frame_count-1))):
        selected = display_Panel()
        row = np.ones(counter)*selected
        with open(file_name.split('.')[0].split('/')[-1] + "_output.txt",'a') as o:
            for j in range(len(row)):
                o.write(str(row[j]))
                o.write("\n")
        cv2.destroyAllWindows()
        counter = 0
    counter = counter + 1
cv2.destroyAllWindows()

