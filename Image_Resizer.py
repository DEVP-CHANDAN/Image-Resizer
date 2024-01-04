import cv2
image_name = input("Enter the image path want to resize")
image = cv2.imread(image_name)
cv2.imshow('background' , image)


scale_percent = int(input("Enter the scaling percentage you want"))

width = int(image.shape[1]*scale_percent/100)
height = int(image.shape[0]*scale_percent/100)

dsize = (width , height)

output = cv2.resize(image , dsize=dsize)

new_image_name = input("Enter the new generated image")
cv2.imwrite(new_image_name,output)