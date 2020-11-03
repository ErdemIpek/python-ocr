try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    
    return text
def clear_pic():
    pic = cv2.imread("ads.jpg",0)
    blurredpic=cv2.blur(pic,(5,5))
    cv2.imwrite("C:/ProgramFiles/TesseractOCR/ads1.jpg",blurredpic)

print(ocr_core(clear_pic()))
