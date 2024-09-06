
import cv2

cont = 0
while True:
    # Inicializar a câmera (0 geralmente representa a câmera padrão)
    cap = cv2.VideoCapture(0)

    # Verificar se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Não foi possível abrir a câmera")
        exit()

    # Capturar um frame
    ret, frame = cap.read()

    # Verificar se o frame foi capturado com sucesso
    if not ret:
        print("Não foi possível capturar o frame")
        exit()

    # Mostrar o frame
    cv2.imshow('Frame', frame)

    # Salvar a imagem
    for i in range(0, 7):
        cv2.imwrite('imagem_capturada' + str(i) + '.jpg', frame)       
        
# Liberar a câmera e fechar a janela    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()    
    cont += 1
    if cont == 5:
        break