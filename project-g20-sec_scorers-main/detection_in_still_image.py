import cv2 as cv
import numpy as np

#load the class labels our YOLO model was trained on
LABELS = open('related_files/obj.names').read().strip().split("\n")

#load weights and cfg
weights = 'related_files/crop_weed_detection.weights'
config = 'related_files/crop_weed.cfg'

#Random generator for color selection for drawing boxes
np.random.seed(2)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),dtype="uint8")


yolo = cv.dnn.readNetFromDarknet(config, weights)

#load our input image and grab its spatial dimensions
img = cv.imread('images/crop_1.jpeg')
(H, W) = img.shape[:2]

#parameters
confi = 0.5
thresh = 0.5

#determine only the *output* layer names that we need from YOLO
ln = yolo.getLayerNames()
ln = [ln[i - 1] for i in yolo.getUnconnectedOutLayers()]

#construct a blob from the input img and then perform a forward
#pass of the YOLO object detector, giving us our bounding boxes and
#associated probabilities
blob = cv.dnn.blobFromImage(img, 1 / 255.0, (512, 512),swapRB=True, crop=False)
yolo.setInput(blob)
# start = time.time()
layerOutputs = yolo.forward(ln)
# end = time.time()

#show timing information on YOLO
# print("[INFO] YOLO took {:.6f} seconds".format(end - start))

#initialize our lists of detected bounding boxes, confidences, and
#class IDs, respectively
boxes = []
confidences = []
classIDs = []

#loop over each of the layer outputs
for output in layerOutputs:
	#loop over each of the detections
	for detection in output:
		#extract the class ID and confidence (i.e., probability) of
		#the current object detection
		scores = detection[5:]
		classID = np.argmax(scores)
		confidence = scores[classID]

		#filter out weak predictions by ensuring the detected
		#probability is greater than the minimum probability
		if confidence > confi:
			#scale the bounding box coordinates back relative to the
			#size of the img, keeping in mind that YOLO actually
			#returns the center (x, y)-coordinates of the bounding
			#box followed by the boxes' width and height
			box = detection[0:4] * np.array([W, H, W, H])
			(centerX, centerY, width, height) = box.astype("int")

			#use the center (x, y)-coordinates to derive the top and
			#and left corner of the bounding box
			x = int(centerX - (width / 2))
			y = int(centerY - (height / 2))

			#update our list of bounding box coordinates, confidences,
			#and class IDs
			boxes.append([x, y, int(width), int(height)])
			confidences.append(float(confidence))
			classIDs.append(classID)

#apply non-maxima suppression to suppress weak, overlapping bounding
#boxes
idxs = cv.dnn.NMSBoxes(boxes, confidences, confi, thresh)

#ensure at least one detection exists
if len(idxs) > 0:
	#loop over the indexes we are keeping
	for i in idxs.flatten():
		#extract the bounding box coordinates
		(x, y) = (boxes[i][0], boxes[i][1])
		(w, h) = (boxes[i][2], boxes[i][3])

		#draw a bounding box rectangle and label on the img
		color = [int(c) for c in COLORS[classIDs[i]]]
		cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
		text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
		cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX,0.5, color, 2)

cv.imshow("Detected Images", img)
cv.waitKey(0)

# det = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# plt.figure(figsize=(12,8))
# plt.imshow(det)

# #save detected img 
# path = 'detection11.jpeg'#change if you want
# det = cv.cvtColor(det,cv.COLOR_RGB2BGR)
# cv.imwrite(path,det)