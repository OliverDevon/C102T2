import cv2, random
def take_picture():
    videocaptureobj = cv2.VideoCapture(0)
    reslt = True
    while(reslt):
        myPicNum = random.randint(0, 100000000000)

        ret, frame=videocaptureobj.read()
        cv2.imwrite('myPic' + str(myPicNum) + '.PNG', frame)
        reslt = False
        videocaptureobj.release()
        cv2.destroyAllWindows()
take_picture()