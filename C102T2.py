import cv2, random, time, dropbox
statTime=time.time()
def take_picture():
    videocaptureobj = cv2.VideoCapture(0)
    reslt = True
    while(reslt):
        myPicNum = random.randint(0, 100000000000)
        ret, frame=videocaptureobj.read()
        imgName = 'myPic' + str(myPicNum) + '.PNG'
        cv2.imwrite(imgName, frame)
        statTime=time.time()
        reslt = False
    return imgName
    print('sanp Done')
    videocaptureobj.release()
    cv2.destroyAllWindows()
'''take_picture()
print(statTime)'''
def upload(imgName):
    access_token = 'sl.A-AzZSbLmCsMzrqDOELNHl_dI7VCKDP3XHB2iK-0Rici5J-i9DvH3anQlu-subKYezm1egQM3E4jF9_xdgAPtCLlcCz8wegLO2-axnxDTnJDSre7014hnKvSIDERXDcTzGChGInlDyr2'
    file=imgName
    file_from = file
    file_2 = '/test/' + (imgName)
    db = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        db.files_upload(f.read(), file_2, mode=dropbox.files.WriteMode.overwrite)
def main():
    while(True):
        if((time.time()-statTime)>=5):
            name=take_picture()
            upload(name)
main()