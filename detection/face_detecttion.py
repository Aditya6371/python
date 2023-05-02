import cv2
from deepface import DeepFace

def takepic():
    print('SCANNING FACE....')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('captured.jpg',frame)
    cv2.destroyAllWindows()
    cap.release()
    print('Face Scan Complete....')

takepic()
img1 ='captured.jpg'
img2 = 'img1.jpg'

model_name=["VGG face",'Facenet','Facenet512','OpenFace','DeepFace','DeepID','ARCFace','Dlib','SFace']

verify=DeepFace.verify(img1_path=img1,img2_path=img2,model_name=model_name[1])
print(verify['facial_areas'])
print(verify['verified'])
# authentication= DeepFace.analyze(img_path=img1,actions=['emotion','age','gender','race'])
# print(" \n",authentication," ")
# if verify['verified']:
    # print('Access Granted...')
# else:
    # print('Access Denied.. Shutting Down System....')



