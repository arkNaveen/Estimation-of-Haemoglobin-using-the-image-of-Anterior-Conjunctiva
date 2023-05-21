# Estimation-of-Haemoglobin-using-the-image-of-Anterior-Conjunctiva
This projects main objective is to provide a statistical method for estimating Haemoglobin percentage using Digital Image Processing using the OpenCV Python library.
#
All samples and data are obtained from the csv file. A brief look at the samples shows the
haemoglobin values and their respective red, green, blue percentage of pixels which
are further used in the calibration curve in the coding with th availability of both male and female samples.
#
The image is first taken on a smartphone and then feeded into the code by adding relative path.
Segmentation of the required part of the eye is done by applying two masks which mask only the particular RED colour in the HSV colour space.
