import cv2

img1 = cv2.imread('kakashi.jpg')
img2 = cv2.imread('jiraya.jpg')

if img1 is None or img2 is None:
    print("Erro ao carregar as imagens!")
else:
    h, w = img1.shape[:2]
    img2 = cv2.resize(img2, (w, h))

    res_and = cv2.bitwise_and(img1, img2)

    res_or = cv2.bitwise_or(img1, img2)

    res_xor = cv2.bitwise_xor(img1, img2)

    res_not = cv2.bitwise_not(img1)

    cv2.imshow('1 - Bitwise AND', res_and)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('2 - Bitwise OR', res_or)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('3 - Bitwise XOR', res_xor)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('4 - Bitwise NOT (Kakashi)', res_not)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    