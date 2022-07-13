# INFORMACOES
# Este código voce pode mapear os locals dos do estacionamento e
# salvar no arquvivo CarParkPos para que o código no arquivo main possa ler
import cv2
import pickle

width, height = 107, 48

try:
    with open('arquivos/CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    
    with open('arquivos/carParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('media/carParkImg.png')

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255,0,255),2)

    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouseClick)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break