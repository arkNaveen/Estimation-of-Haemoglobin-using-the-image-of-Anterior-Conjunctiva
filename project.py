import cv2 as cv
import numpy as np
gend=input("Enter m if Male or f for Female - ")
image = cv.imread('ENter your path here')
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Original",image)
nonoise = cv.GaussianBlur(gray, (7, 7), 0)  #reduces noise
level, bw = cv.threshold(nonoise, 0, 255, cv.THRESH_OTSU+cv.THRESH_BINARY)  
#can be done with THRESH TRIANLE global method also
# cv.imshow("Thresholded Image",bw)

#OTSU method is used for images having two peak intensity values in the 
#histogram of intensity values and the number of pixels having that intensity value
contours, hierarchy = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area (assumed to be the eye)
largest_contour = {}
max_area_contour = 0
for i in range(len(contours)):
    area=cv.contourArea(contours[i])
    if area>max_area_contour:
        max_area_contour=area
        largest_contour=contours[i]
mask=np.zeros_like(image)
#drawing a black mask over the image
cv.drawContours(mask,[largest_contour],0,(255, 255, 255), -1)

masked_eye=cv.bitwise_and(image, mask)
cv.imshow('Image Processed Eye', masked_eye)

def rgb():
    arr_list=image.tolist()
    r=g=b=0
    for row in arr_list:
        for item in row: 
            r=r+item[2]
            g=g+item[1]
            b=b+item[0]  
    total=r+g+b
    red=r/total*100
    green=g/total*100
    blue=b/total*100
    a=[red,green,blue]
    return a

#a is collective rgb array 
matrix=rgb()  
print(matrix)
red=matrix[0]
green=matrix[1]
blue=matrix[2]

#Conditions
lb=ub=0
if gend=='m':
    if red>37 and red<40.7:
        lb=10.2
        ub=12.37
    if red>=40.7 and red<44.4:
        lb=8.99
        ub=14.27
    if red>=44.4 and red<48.1:
        lb=11.82
        ub=15.36
    if red>=48.1 and red<=51.8:
        lb=13.0
        ub=15.18
    if red>51.8 and red<60:
        lb=15
        ub=17
    
elif gend=='f':
    if red>37 and red<40.7:
        lb=7.83
        ub=9.17
    if red>=40.7 and red<44.4:
        lb=9.37
        ub=12.36
    if red>=44.4 and red<48.1:
        lb=9.24
        ub=13.9
    if red>=48.1 and red<=51.8:
        lb=10.63
        ub=12.73
    if red>51.8 and red<60:
        lb=10
        ub=12
else:
    print("Enter valid data")
if gend=='m':
    if green>24.2 and green<26.4:
        lb1=14.32
        ub1=15.55
    if green>=26.4 and green<28.6:
            lb1=12.49
            ub1=15.23
    if green>=28.6 and green<30.8:
            lb1=10.28
            ub1=14.78
    if green>30.8 and green<33:
            lb1=4.61
            ub1=11.27
elif gend=='f':
    if green>24.2 and green<26.4:
        lb1=10.22
        ub1=12.78
    if green>=26.4 and green<28.6:
        lb1=10.24
        ub1=13.52
    if green>=28.6 and green<30.8:
        lb1=9.16
        ub1=13.26
    if green>30.8 and green<33:
        lb1=8.38
        ub1=11.04

lb2=ub2=0
if gend=='m':
    if blue>=18 and blue<20:
        lb2=14.5
        ub2=15.2
    if blue>20 and blue<22:
        lb2=12.9
        ub2=15.76
    if blue>=22 and blue<24:
        lb2=9.75
        ub2=14.31
    if blue>=24 and blue<26:
        lb2=11.05
        ub2=15.61
    if blue>=26 and blue<28:
        lb2=9.75
        ub2=15.67
    if blue>28 and blue<30:
        lb2=10.9
        ub2=13.4
elif gend=='f':
    if blue>20 and blue<22:
        lb2=10.45
        ub2=12.59
    if blue>=22 and blue<24:
        lb2=9.24
        ub2=12.56
    if blue>=24 and blue<26:
        lb2=8.36
        ub2=13.04
    if blue>=26 and blue<28:
        lb2=9.66
        ub2=13.22
    if blue>28 and blue<30:
        lb2=8.5
        ub2=12.7
else:
    print("Enter valid data")
lower_mean=(lb+lb1+lb2)/3
upper_mean=(ub+ub1+ub2)/3
print("Hb between " +str(lower_mean)+" "+str(upper_mean))
print(" Haemoglobin Level - "+str((lower_mean+upper_mean)/2)+"g/dl")
print("Hematocrit level",red,"%")
cv.waitKey(0)
cv.destroyAllWindows()
