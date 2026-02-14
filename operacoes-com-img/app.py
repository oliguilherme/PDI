import cv2

img1 = cv2.imread('naruto.jpg')
img2 = cv2.imread('sasuke.jpg')

#result = cv2.add(img1, img2)

if img1 is not None and img2 is not None:
    h, w = img1.shape[:2]
    img2 = cv2.resize(img2, (w, h))

    sum = cv2.add(img1, img2)
    sub = cv2.subtract(img1, img2)
    mult = cv2.multiply(img1, img2)
    div = cv2.divide(img1, img2, scale=255)

    cv2.imshow('Soma', sum)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('Subtracao', sub)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imshow('Multiplicacao', mult)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('Divisao', div)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Erro ao carregar arquivos.")


