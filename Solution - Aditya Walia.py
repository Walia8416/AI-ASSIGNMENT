#SOLUTION BY ADITYA WALIA
#EMAIL - adi.walia16@gmail.com


import cv2
import os 
import xml.etree.ElementTree as ET


def extract_Coor(fullname):

	
		
	print(fullname)
	tree = ET.parse(fullname)
	root = tree.getroot()
	boxs=0;
	coordinates = []
	light = []
	for coor in root.findall("object/bndbox/"):
		coordinates.append(float(coor.text))
		boxs+=1;
	boxs = boxs/4
	
	for child in root.iter("filename"):
		head, tail = os.path.split(child.text)

	for child in root.findall("object/name"):
		light.append(str(child.text))
	

	return coordinates, str(tail), int(boxs), light


		



if __name__ == "__main__":
	
	

	for filename in os.listdir('.'):
		if not filename.endswith('.xml'): 
			continue
		
		coors, imgname, nbox, lights = extract_Coor(filename)
		image = cv2.imread(imgname)
		a=0
		b=4

		for i in range(nbox):
			x1,y1,x2,y2 = coors[a:b]	
			start_point = (int(x1), int(y1))
			end_point = (int(x2),int(y2))
			texpt = (int(x1), int(y2)-20)
			color = (255, 0, 0)
			thickness = 2
			image = cv2.rectangle(image, start_point, end_point, color, thickness)
			cv2.putText(image,lights[i],texpt,cv2.FONT_HERSHEY_SIMPLEX, 0.3, (36,255,12),1)
			a+=4
			b+=4
		
		cv2.imshow("result", image)
		cv2.imwrite(imgname, image)
		


