############## UNDISTORTION #####################################################

img = cv.imread(r"C:\Users\Akshay\Downloads\video_new\700.png")
h, w = img.shape[:2]  # resolution i.e h = 1080 , w= 1920

newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w, h), 1, (w, h))
# ROI:- Optional output rectangle [x,y,w,h] that outlines all-good-pixels region in the undistorted image
print('ROI = ')
print(roi)
dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)
# crop the image
x, y, w, h = roi
print('New w = ')
print(w)
print('New h = ')
print(h)
dst = dst[y:y + h, x:x + w]
cv.imwrite('caliResult1.png', dst)


