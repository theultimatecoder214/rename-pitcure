import cv2


image= cv2.imread("solar-system.jpg")
text="sun"
text2="mercury"
text3="venus"
text4="earth"
text5="mars"
text6="jupiter"
text7="saturn"
text8="uranus"
text9="neptune"
text10="Solar System"
cv2.putText(image,text,(55,70),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=3,color=(255,0,255))
cv2.putText(image,text2,(84,250),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=1,color=(255,0,0))
cv2.putText(image,text3,(180,170),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=1,color=(255,0,255))
cv2.putText(image,text4,(275,250),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=1,color=(255,255,255))
cv2.putText(image,text5,(360,250),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=1,color=(255,255,255))
cv2.putText(image,text6,(440,150),fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(image,text7,(790,250),fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(255,0,0))
cv2.putText(image,text8,(895,150),fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(255,255,255))
cv2.putText(image,text9,(1110,250),fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(image,text10,(490,40),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=1,color=(0,255,255,))
cv2.imshow("Solar-system",image)
print(image)

cv2.waitKey(0)