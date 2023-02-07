import pytesseract
import cv2
#declare tesseract.exe path
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

#declare sample image path
image = cv2.imread("image\sampleimg.png")
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Returns string containing box boundaries, confidences, and other information
print(pytesseract.image_to_data(img_RGB))
results = pytesseract.image_to_data(img_RGB)

for id, line in enumerate(results.splitlines()):
    if id !=0:
#split the result line by line
        line = line.split()
        print(line)
#detect word only
        if len(line) == 12:
#initialize the string containing box boundaries, confidences
            x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
#Put rectangular box and recognised text above the sample text
            cv2.rectangle(image,(x,y),(w+x,h+y), (0,255,0),2)
            cv2.putText(image,line[11],(x,y), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)

cv2.imshow("Input", image)
cv2.waitKey(0)