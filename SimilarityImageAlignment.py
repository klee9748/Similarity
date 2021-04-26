import cv2
import glob
import numpy as np
from PIL import Image, ImageChops
X_data = []
Y_data = []
files = glob.glob ("/Users/klee22/Desktop/save/New_Vid/*.png")
files2 = glob.glob ("/users/klee22/Desktop/save/old_vid/*.png")


for myFile in files:    
    #image = cv2.imread (myFile, cv2.IMREAD_COLOR) #enumerated constants
    image = Image.open(myFile)
    X_data.append (image)

for myFile2 in files2:
   #print(myFile2)
   #image2 = cv2.imread (myFile2, cv2.IMREAD_COLOR)
   image2 = Image.open(myFile2)
   Y_data.append (image2)

print('X_data shape:', np.array(X_data).shape)
#print('Y_data shape:', np.array(X_data[0]).shape); # create multi-dim array by providing shape

numpic_x = 97
numpic_y = 97
comparison_data = np.zeros(shape=(97, 97)) #create an empty grid that has space for the data from the for loop

x = 0
for ref_image in X_data:

    y = 0
    for new_image in Y_data:
        diff = ImageChops.difference(ref_image, new_image)
        Image.show(diff)
        print(diff.getbox())
        #comparison_score = cv2.SIFT_create(ref_image, new_image)
        
        #comparison_data[x][y] = comparison_score #comparison_data[x][y] -> location
        y += 1
    x += 1


#|x| SSE ->max similarity minimum diff = offset alignment (find out)

#sampling (every 5th image -> )

#comparison_score (greatest similarity)
#(Image alignment)
#which is the diagonal with the best scores 
#find the offset



#r compare in comparison_data:
##    pairs = zip(X_data.getdata(), Y_data.getdata())
  #  if len(X_data.getbands()) == 1:
 #      dif = sum(abs(p1-p2) for p1,p2 in pairs)
  #  else:
 #      dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 #  ncomponents = X_data.size[0] * X_data.size[1] * 3
 #  print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)
  #  difPercent = (dif / 255.0 * 100) / ncomponents
    
#For I in 0..X_data.count
#Refimage= X_data[i]#
#For j in 0…Y_data.count
#compImage= y_data[j]
#Score = compare(refimage,compimage)
#compa_array[i][j]=score

#what is should print out: array of similarityscores 
#Part 2
#X0 = y45
#x1=y46
#x2=y27 (table)


