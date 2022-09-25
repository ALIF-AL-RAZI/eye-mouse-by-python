import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
   _, frame = cam.read()
   frame =cv2.flip(frame,1) #flipping camera vertically for 1
   rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   output = face_mesh.process(rgb_frame)
   landmark_points = output.multi_face_landmarks

   frame_h, frame_w, _ = frame.shape

   if landmark_points:
      landmarks = landmark_points[0].landmark
      for id, landmark in enumerate(landmarks[474:478]):    #four points of eyes [474:478]

         x= int(landmark.x * frame_w)
         y= int(landmark.y * frame_h)
         cv2.circle(frame, (x,y), 3, (0,255,0)) #circle drawing of different points in faces
         if id==1:
            screen_x = 1.5*screen_w/frame_w * x   #multiplying 1.5 is increasing mouse sensitivity and others is for pointer covering whole screen
            screen_y = 1.5*screen_h / frame_h * y      #multiplying 1.5 is increasing mouse sensitivity and others is for pointer covering whole screen
            pyautogui.moveTo(screen_x,screen_y) #moving mouse pointer


      left = [landmarks[145], landmarks[159]]
      for landmark in left:
         x = int(landmark.x * frame_w)
         y = int(landmark.y * frame_h)
         cv2.circle(frame, (x, y), 3, (0, 255, 255))

      #print(left[0].y-left[1].y)
      if  (left[0].y-left[1].y)<0.01:
         print("click")
         pyautogui.click()
         pyautogui.sleep(1)





   cv2.imshow('eye mouse', frame)
   cv2.waitKey(1)


