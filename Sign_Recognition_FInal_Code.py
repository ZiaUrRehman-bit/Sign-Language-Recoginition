import cv2
import Track_Hand as ht

# read webcam and sign picture
cap = cv2.VideoCapture(0)
im = cv2.imread("InkedInkedimg.jpg")

# set the frame and resize the picture
cap.set(3, 840)
cap.set(4, 620)
im = cv2.resize(im, (640, 480))

# Making an object of class handTracker
detector = ht.handTracker(detConfidence=0.8)

def findSign(lmList):

    # landmarks id's of thump other finger tips
    tiIds = [4, 8, 12, 16, 20]
    letters = ['?', 'A', 'B', 'C', 'Hi', 'D', 'E',
               'F', 'G', 'L', 'I', 'J', 'M', 'W', 'V']

    fingers = []
    character = letters[0]

    # print('\n', lmList[8], lmList[12], lmList[16], lmList[20], lmList[4], end= ' ') #> 280
    bb = (lmList[8][2] > lmList[7][2]) & (lmList[12][2] > lmList[11][2]) & (lmList[16][2] > lmList[15][2]) & (
            lmList[20][2] > lmList[19][2])
    cc = (lmList[8][2] > lmList[5][2]) & (lmList[12][2] > lmList[9][2]) & (lmList[16][2] > lmList[13][2]) & (
            lmList[20][2] > lmList[17][2])

    fff = (lmList[12][2] < lmList[11][2]) & (lmList[16][2] < lmList[15][2]) & (lmList[20][2] < lmList[19][2])
    ggg = (lmList[12][2] > lmList[9][2]) & (lmList[16][2] > lmList[13][2]) & (lmList[20][2] > lmList[17][2])

    ii = (lmList[20][2] < lmList[19][2])
    iii = (lmList[8][2] > lmList[5][2]) & (lmList[12][2] > lmList[9][2]) & (lmList[16][2] > lmList[13][2])
    i = (lmList[4][2] - lmList[14][2]) < 20
    j = lmList[4][2] > lmList[9][2]

    m = (lmList[6][2] > lmList[5][2]) & (lmList[7][2] > lmList[6][2])
    mm = (lmList[10][2] > lmList[9][2]) & (lmList[11][2] > lmList[10][2])
    mmm = (lmList[14][2] > lmList[13][2]) & (lmList[15][2] > lmList[14][2])

    w = (lmList[8][2] < lmList[7][2]) & (lmList[12][2] < lmList[11][2]) & (lmList[16][2] < lmList[15][2])
    ww = lmList[20][2] > lmList[17][2]

    v = (lmList[16][2] > lmList[13][2]) & (lmList[20][2] > lmList[17][2])
    vv = (lmList[8][2] < lmList[7][2]) & (lmList[12][2] < lmList[11][2])

    # Thumb
    if lmList[tiIds[0]][1] > lmList[tiIds[0] - 1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
    #
    # # 4 Fingers
    for id in range(1, 5):

        if lmList[tiIds[id]][2] < lmList[tiIds[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    # print(fingers)
    totalFingers = fingers.count(1)
    ff = lmList[4][1] > lmList[3][1]

    # if totalFingers == 0:
    #     print("A")
    #     character = letters[1]
    if cc & (lmList[4][2] < lmList[6][2]):
        print("A")
        character = letters[1]
    elif cc & (lmList[4][2] > lmList[6][2]):
        print("E")
        character = letters[6]
    elif totalFingers == 4:
        character = letters[2]
    elif w & ww:
        character = letters[13]
    elif totalFingers == 5:
        character = letters[4]
    elif (lmList[8][2] < lmList[7][2]) & ((lmList[4][1] - lmList[12][1]) < 20):
        print("D")
        character = letters[5]
    elif fff & (lmList[4][1] - lmList[8][1] < 14):
        print("F")
        character = letters[7]
    elif ggg & ((lmList[4][2] - lmList[8][2]) > 70 & (lmList[4][2] - lmList[8][2]) < 105):
        print("G")
        character = letters[8]
    elif (lmList[4][1] - lmList[8][1]) > 50:
        print("L")
        character = letters[9]
    elif i & ii & iii:
        print("I")
        character = letters[10]
    elif i & j:
        print("J")
        character = letters[11]
    elif m & mm & mmm:
        print("M")
        character = letters[12]
    elif v & vv:
        character = letters[14]
    elif lmList[4][1] < lmList[3][1]:
        if bb:
            print("C")
            character = letters[3]
    else:
        print("none2")
        character = letters[0]

    return character



while True:
    Success, img = cap.read()
    img = detector.findAndDrawHands(img)
    lmList = detector.findLandmarks(img)

    if lmList:

        character = findSign(lmList)

        cv2.rectangle(img, (435, 220), (580, 410),
                      (0, 0, 0), cv2.FILLED)
        cv2.rectangle(img, (435, 220), (580, 410),
                      (255, 0, 255), 5)

        cv2.putText(img, str(character), (460, 375), cv2.FONT_HERSHEY_COMPLEX,
                    5, (255, 255, 255), 25)

    cv2.rectangle(img, (615, 40), (470, 10),
                  (0, 0, 0), cv2.FILLED)
    cv2.rectangle(img, (615, 40), (470, 10),
                  (255, 0, 255), 3)
    cv2.putText(img, "Created By Diana", (475, 30), cv2.FONT_ITALIC,
                0.5, (255, 255, 255), 1)
    cv2.imshow("Sign Recognition", img)
    cv2.imshow("Sign Image", im)
    key = cv2.waitKey(1)

    if key == 80 or key == 113:
        break

cap.release()
cv2.destroyAllWindows()

print("Code Completed!")