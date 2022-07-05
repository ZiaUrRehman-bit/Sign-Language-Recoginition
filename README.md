# Sign Language Recoginition

![image](https://user-images.githubusercontent.com/77435711/177387039-cb87dc53-e799-4284-a352-c7dd850b2a2b.png)

## Steps to create code
### 1. I will create class for hand detection with following functions
	
		a. Class name handDetector()
		
		b. First function of class is initialization function, which initialize mediapipe library for how many hands 
    you want to detect and how much accuracy you need or    confidence required to guess it is really a hand.
    
		c. The second function is for hands detection named findHands(), which simple detect hands and display the 
    landmarks on it with connected to each other, just like
		
 ![image](https://user-images.githubusercontent.com/77435711/177390792-2e5a4820-bccb-49eb-9f30-54cee75f25e8.png)
 
    d. The last function is finding hand landmarks named as findHandLm(), which return 21 hand landmarks with x-axis 
    and y-axis value.
![image](https://user-images.githubusercontent.com/77435711/177391109-045af422-e28f-4513-a38f-589a5daf81f7.png)

### 2. The next step is to create main program and recognize signs 

![image](https://user-images.githubusercontent.com/77435711/177391275-013bf9ac-44f3-4e52-8de4-f066b90a738b.png)
		
    A.  In main program first I make an object of handDetector() class 
		
		B. Through the object I find the hand
		
		C. After detection of hand then finds the landmarks 
		
		D. On the basis of landmarks values guess the sign
		
		E. In last display what the sign is on run time video 














