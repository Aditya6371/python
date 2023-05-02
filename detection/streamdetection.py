import dlib
import cv2
from deepface import DeepFace

# cap= cv2.VideoCapture(0)
# imgpath=[r"C:\Users\HP\Desktop\studies\coding\python\detection\database\abhi.jpg",r"C:\Users\HP\Desktop\studies\coding\python\detection\database\adisahoo.jpg",r"C:\Users\HP\Desktop\studies\coding\python\detection\database\img11.jpg",r"C:\Users\HP\Desktop\studies\coding\python\detection\database\img2.jpg",r"C:\Users\HP\Desktop\studies\coding\python\detection\database\millan.jpg",r"C:\Users\HP\Desktop\studies\coding\python\detection\database\satya.jpg",r"C:\Users\HP\Desktop\studies\coding\python\detection\database\yash.jpg"]

# verify the two faces 


# def takepic():
#     ret, pic=cap.read()
#     cv2.imwrite('test.jpg',pic)
#     cap.release()
# takepic()
# pic1='test.jpg'
# for i in range(0,6):
#     verify=DeepFace.verify(img1_path=imgpath[i],img2_path="test.jpg",detector_backend="OpenFace")
# print(verify['verified'])
# if  verify['verified']:
#     print('Face matched....')
# else:
#     print('Face doesn\'t match....')



#  Analyze the image for data

# for i in range(0,3):
#     ana = DeepFace.analyze(img_path=imgpath[i],actions=("age","gender","emotion"))
#     print(ana)



# Live Analyze the Image 
DeepFace.stream(db_path=r"C:\Users\HP\Desktop\studies\coding\python\detection\database")
# detector= dlib.get_frontal_face_detector()
# cap= cv2.VideoCapture(0)
# def analysis():
#     data=DeepFace.analyze(img_path=pic1,actions=['gender'])
#     return data
# while True:
#     _, frame = cap.read()
#     cv2.imshow('frame',frame)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = detector(gray)
#         # detected face in faces array
#     for face in faces:
#         x1 = face.left()
#         y1 = face.top()
#         x2 = face.right()
#         y2 = face.bottom()
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
#         cv2.imshow('frame',frame)
#     cv2.putText(frame,"hiii",(100,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2,3)
#     key = cv2.waitKey(1)



# face recognition 

# dfs = DeepFace.find(img_path = "img1.jpg",db_path = r"C:\Users\HP\Desktop\studies\coding\python\detection\database")
# print(dfs)


# cap.release()


