################Reprojection Error##############
mean_error = 0
print(len(imgpoints))
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], cameraMatrix, dist)
    print("imgpoints2:")
    print(imgpoints2)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2SQR) / len(
        imgpoints2)  
    mean_error += error

print("total error: {}".format(
    mean_error / len(objpoints)))  