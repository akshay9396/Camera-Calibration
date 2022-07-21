############## CALIBRATION #######################################################

ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)

print("CameraMatrix = ")
print(cameraMatrix)
print('----------------------------------------------------------')
print(dist)
print('----------------------------------------------------------')
print(rvecs)
print('----------------------------------------------------------')
print(tvecs)

