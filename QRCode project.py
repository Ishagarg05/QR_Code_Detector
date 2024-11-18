import cv2
import numpy as np
from pyzbar.pyzbar import decode



# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height



# Read authorized data from file
with open('mydataFile.txt') as f:
    # spacing removed 
     myDataList = [line.strip() for line in f.read().splitlines()]

while True:
    success, img = cap.read()
    if not success:
        break

    for barcode in decode(img):
        
        
        # Decode the barcode data
        myData = barcode.data.decode('utf-8').strip()
        print(f"Decoded Data: {myData}")

        
        # Check if the decoded data is in the authorized list
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)  # Green for authorized
        else:
            myOutput = 'Un-authorized'
            myColor = (0, 0, 255)  # Red for unauthorized

        
        # Draw a polygon around the barcode
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)

        
        # Put the text on the image
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, myColor, 2)

    
    
    # Show the result
    cv2.imshow('Result', img)

    
    
    # Exit on pressing "Esc" key
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the "Esc" key
        break

#  Release the webcam and close the OpenCV window
# cap.release()``
# cv2.destroyAllWindows()#
