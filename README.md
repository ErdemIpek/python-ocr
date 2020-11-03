# python-ocr
# [GitHub Repo](https://github.com/ErdemIpek/python-ocr)
 
Hi! This is an OCR(Optical Character Recognition) project written in python language. Can be used to detect handwritten or printed texts in any language.

# This project requires Google's OCR technology "Tesseract":

 [Tesseract](https://github.com/tesseract-ocr/)

# To download Tesseract:

 [Download](https://github.com/UB-Mannheim/tesseract/wiki)

Important reminder, to run ocr_coreTaslak.py you should install tesseract to your root project folder or specify location of tesseract in ocr_coreTaslak.py...


 # Usage:
 ```
  python ocr_coreTaslak.py -i <Path To Image> -l <Dataset Name(inside \Tesseract-OCR\tessdata folder)> 
 ```
  
 # Example Image:
 ![example_00.png](https://github.com/ErdemIpek/python-ocr/blob/master/images/example_00.png?raw=true)
 
 # Example Usage:
```cd python-ocr
   python ocr_coreTaslak.py  -i images\example_00.png -l tur_best
```

# Output:
```
Input Fıle --> example_00
Used Data --> tur_best
Ankaraya Hosgeldin

```




