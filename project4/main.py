import cv2
import numpy as np

# STEP 1: Files aur Labels setup
proto_file = "MobileNetSSD_deploy.prototxt"
model_file = "MobileNetSSD_deploy.caffemodel"
image_path = "test.jpg"  # Ensure karein ke photo ka naam yahi ho

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# STEP 2: Model ko load karna
print("[INFO] Model load ho raha hai...")
net = cv2.dnn.readNetFromCaffe(proto_file, model_file)
print("[INFO] Model successfully load ho gaya!")

# STEP 3: Image ko read aur prepare karna
image = cv2.imread(image_path)

if image is None:
    print(f"[Error] '{image_path}' nahi mili! Folder check karein.")
else:
    (h, w) = image.shape[:2]
    # Image ko AI ke samajhne ke liye 'blob' mein badalna
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

    # STEP 4: Detection shuru karna
    print("[INFO] Objects detect ho rahe hain...")
    net.setInput(blob)
    detections = net.forward()

    # STEP 5: Results ko screen par dikhana
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Sirf wo cheezein dikhana jo 50% se zyada confirm hon
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = f"{CLASSES[idx]}: {confidence * 100:.2f}%"
            
            # Box ki calculation
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Green box aur text banana
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # FINAL STEP: Window show karna
    cv2.imshow("Object Detection Result", image)
    print("[INFO] Success! Window band karne ke liye keyboard se koi key dabayein.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
