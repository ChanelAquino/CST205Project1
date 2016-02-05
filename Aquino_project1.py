#Names: Chanel Aquino and Marcus Dixon
#Date Created: 5 February 2016
#Description: CST205 Project 1 Image manipulation to replace undesireable pixels in a set of otherwise similar images.

#create a list of pictures
pictures = []

#prompt user to pick an image file1
#append the chosen image to the pictures list
file1 = pickAFile()
image1 = makePicture(file1)
pictures.append(image1)

file2 = pickAFile()
image2 = makePicture(file2)
pictures.append(image2)

file3 = pickAFile()
image3 = makePicture(file3)
pictures.append(image3)

file4 = pickAFile()
image4 = makePicture(file4)
pictures.append(image4)

file5 = pickAFile()
image5 = makePicture(file5)
pictures.append(image5)

file6 = pickAFile()
image6 = makePicture(file6)
pictures.append(image6)

file7 = pickAFile()
image7 = makePicture(file7)
pictures.append(image7)

file8 = pickAFile()
image8 = makePicture(file8)
pictures.append(image8)

file9 = pickAFile()
image9 = makePicture(file9)
pictures.append(image9)

#create an empty picture for the final image
finalImage = makeEmptyPicture(495, 557)

#function to obtain median values
def medianOdd(values):
  listLength = len(values)
  sortedValues = sorted(values)
  middleIndex = (listLength/2)
  return sortedValues[middleIndex]

#create lists for red, green, and blue values
redValue = []
greenValue = []
blueValue = []

for w in range(0, 495):
  for y in range(0, 557):
    for p in range(0, 9):
    	#get pixel at pictures[p] pixel, with w as x-coordinate and y as y-coordinate
		imagepixel = getPixel(pictures[p], w, y)
		
		#append red, blue, and green pixel to respective value list
		redValue.append(getRed(imagepixel))
		blueValue.append(getBlue(imagepixel))
		greenValue.append(getGreen(imagepixel))
		
	#set redness, blueness, and greeness of pixel at (finalImage, w, y) with value medianOdd()
    setRed(getPixel(finalImage, w, y), medianOdd(redValue))
    setBlue(getPixel(finalImage, w, y), medianOdd(blueValue))
    setGreen(getPixel(finalImage, w, y), medianOdd(greenValue))
    redValue = []
    blueValue = []
    greenValue = []

#display final image
show(finalImage)
