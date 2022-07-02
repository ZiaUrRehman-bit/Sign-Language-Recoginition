import cv2
import mediapipe as mp
import time


# capture Video from webcam (cam is object of VideoCapture function)
cam = cv2.VideoCapture(0)   # 0 for laptop webam 1 for webcam2 and so on


# so first thing is that we have to create an object from over class hands (this class is from mediapipe lib)
HandsSol = mp.solutions.hands

# Takes the parameters like how many hands you want to detect, how much accurate etc.
# The first parameter is static mode which is false because i want to detect hands if
# confidence level is suitable, if put ture it will always do the detection

hands = HandsSol.Hands(static_image_mode=False, max_num_hands=2, model_complexity=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

# in loop we have to send RGB image to object hands, so it makes detection

# to draw the line between the landmarks mediapipe also provide solution for that
drawLine = mp.solutions.drawing_utils


# for frame rate
previousTime = 0
currentTime = 0

# we need while loop which runs forever to display frames
while True:

    readOrNot, videoFrame = cam.read()           # read video frames using cam object
    # read function return two things, 1. boolen value (True if frame is successfully capture, False if not)
    #                                  2. video frame

    # now check if frame is successfully readed or not
    if readOrNot == True:

        # videoFrame is in BGR we need to convert it to RGB as object hands required
        rgbImage = cv2.cvtColor(videoFrame, cv2.COLOR_BGR2RGB)

        # now we process the rgb image using the function of hands
        outCome = hands.process(rgbImage)

        # if print the outcome we obtain a string which shows that there is solutions
        # print(outCome)

        # print(outCome.multi_hand_landmarks)  # this will give us hands

        # now we are going to extract information from outCome
        # we have to extract hands information like landmarks number and value
        # we need for loop


        if outCome.multi_hand_landmarks:   # if there is any hand
            for landMarks in outCome.multi_hand_landmarks:
                # print(landMarks)

                # so still we don't still know how we use these values
                # if i want to track the landmark position to perform certain task then what?

                # so now we are going to extract the id and landmark value from landMarks

                for lmId, lm in enumerate(landMarks.landmark):

                    # print lanmarkid and x y z values
                    # print(lmId, lm)

                    # each id has a corresponding landmark
                    # and landmark has x, y and z , and we are using x and y to find the location of landmark on the hand
                    # but the valuse are in float and pixels valuse are in decimal
                    # so we get the pixel value by multiplying width and height with these valuses

                    h, w, c = videoFrame.shape # gives height width and channels of over image
                    # now we can find the position
                    # we have to convert it to integer
                    px, py = int(lm.x*w), int(lm.y*h)
                    print(lmId, px, py)

                    # this will draw circle on landmark 4
                    if lmId == 4:
                        cv2.circle(videoFrame, (px, py), 15, (255, 0, 255), cv2.FILLED)

                # this will draw only 21 landmarks point
                # drawLine.draw_landmarks(videoFrame, landMarks)

                # draw the points with connected each other with line
                drawLine.draw_landmarks(videoFrame, landMarks, HandsSol.HAND_CONNECTIONS)


        currentTime = time.time()
        framePerSecond = 1/(currentTime - previousTime)
        previousTime = currentTime

        # now put on screen
        cv2.putText(videoFrame, f"FPS: {int(framePerSecond)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 255), 2)

        # now display the frame
        cv2.imshow("webcam", videoFrame) # two parameters first name of window and second is frame

        k = cv2.waitKey(1)  # wait for 1 ms to display current frame
        if k == ord('q'):  # if press q then quit
            break

# Release object cam
cam.release()
cv2.destroyAllWindows()  # release memory

print("Basic Code Done!")