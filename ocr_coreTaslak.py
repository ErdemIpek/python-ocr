try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r".\Tesseract-OCR\tesseract.exe"
import cv2
import sys, getopt


def ocr_core(file, lang):
    text = pytesseract.image_to_string(file, lang = lang)
    return text

def main(argv):
    inputfile = ''
    language = 'tur'
    try:
        opts, args = getopt.getopt(argv, "hi:l:", ["ifile=", "help=", "lang="])
    except getopt.GetoptError as ex:
        print('ocr_core.py -i <inputFilePath> -l <TesseractTrainDataLanguage>', ex)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('ocr_core.py -i <inputFilePath> -l <TesseractTrainDataLanguage>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-l", "--lang"):
            language = arg

    photo = cv2.imread(inputfile)
    ret,thresh1 = cv2.threshold(photo,127,255,cv2.THRESH_BINARY)
    denoise = cv2.fastNlMeansDenoisingColored(thresh1,None,10,10,7,21)
    blur = cv2.GaussianBlur(denoise,(5,5),0)
    print('Input Fıle --> ', inputfile)
    print('Used Data -->', language)

    print("Result :\n\n"+ocr_core(blur, language))


if __name__ == "__main__":
   main(sys.argv[1:])

