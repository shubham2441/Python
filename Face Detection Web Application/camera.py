import cv2

class VideoCamera(object):
    def __init__(self):
        
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        dataset = cv2.CascadeClassifier('data.xml')
        
        capture = cv2.VideoCapture(0)
        facedata = []
        while True:
            ret,img = capture.read()
            # print(ret)
            if ret:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = dataset.detectMultiScale(gray)
                for x,y,w,h in faces:
                    cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),4)
        
                    #face = gray[y:y+h, x:x+w]
            #        face = cv2.resize(face, (64,64))
                    #if len(facedata) < 2:
                    #    facedata.append(face)
        #                print(len(facedata))
        
                    ret, jpeg = cv2.imencode('.jpg', img) 
                    return jpeg.tobytes()
            else:
                print("Camera not working")
                 