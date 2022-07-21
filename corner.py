################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################
chessboardSize = (6, 6)  
frameSize = (1920, 1080)  # frame size oder resolution
# # Define the algorithm termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 
30, # Max number of iteration
0.001 # Epsilon)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]].T.reshape(-1, 2)  
# zeroes with coordinate value like 0,0,0  1,0,0  2,0,0 ...0,1,0 ...  5,5,0
size_of_chessboard_squares_mm = 20
objp = objp * size_of_chessboard_squares_mm  # array of 6*6 
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.
path = r"C:\Users\Akshay\Downloads\data\*.png"
images = glob.glob(path) 
for image in images: 
    img = cv.imread(image)  # read the image
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # covert to gray scale
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
    if ret == True:
        print("chessboard found")
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)  
        imgpoints.append(corners2)  
		# Draw and display the corners
        cv.drawChessboardCorners(img, chessboardSize, corners2,ret)  
        cv.imshow('img', img)
        cv.imwrite('res.png', img)
        cv.waitKey(1000)

cv.destroyAllWindows()



