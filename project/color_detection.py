# (R, G, B) average for red from our tests for the DRIVING sensor
from math import sqrt


rR = 245
gR = 46
bR = 11
normrR = rR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))
normgR = gR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))
normbR = bR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))

# (R, G, B) average for red from our tests for the DELIVERY sensor
rRDel = 200
gRDel = 30
bRDel = 30
normrRDel = rRDel / sqrt(pow(rRDel, 2) + pow(gRDel, 2) + pow(bRDel, 2))
normgRDel = gRDel / sqrt(pow(rRDel, 2) + pow(gRDel, 2) + pow(bRDel, 2))
normbRDel = bRDel / sqrt(pow(rRDel, 2) + pow(gRDel, 2) + pow(bRDel, 2))

# (R, G, B) average for orange from our tests for the DRIVING sensor
rO = 265
gO = 76
bO = 16
normrO = rO / sqrt(pow(rO, 2) + pow(gO, 2) + pow(bO, 2))
normgO = gO / sqrt(pow(rO, 2) + pow(gO, 2) + pow(bO, 2))
normbO = bO / sqrt(pow(rO, 2) + pow(gO, 2) + pow(bO, 2))


# (R, G, B) average for orange from our tests for the DELIVERY sensor
rODel = 200
gODel = 70
bODel = 20
normrODel = rODel / sqrt(pow(rODel, 2) + pow(gODel, 2) + pow(bODel, 2))
normgODel = gODel / sqrt(pow(rODel, 2) + pow(gODel, 2) + pow(bODel, 2))
normbODel = bODel / sqrt(pow(rODel, 2) + pow(gODel, 2) + pow(bODel, 2))

# (R, G, B) average for yellow from our tests for the DRIVING sensor
rY = 255
gY = 230
bY = 20
normrY = rY / sqrt(pow(rY, 2) + pow(gY, 2) + pow(bY, 2))
normgY = gY / sqrt(pow(rY, 2) + pow(gY, 2) + pow(bY, 2))
normbY = bY / sqrt(pow(rY, 2) + pow(gY, 2) + pow(bY, 2))

# (R, G, B) average for yellow from our tests for the DELIVERY sensor
rYDel = 166
gYDel = 130
bYDel = 30
normrYDel = rYDel / sqrt(pow(rYDel, 2) + pow(gYDel, 2) + pow(bYDel, 2))
normgYDel = gYDel / sqrt(pow(rYDel, 2) + pow(gYDel, 2) + pow(bYDel, 2))
normbYDel = bYDel / sqrt(pow(rYDel, 2) + pow(gYDel, 2) + pow(bYDel, 2))

# (R, G, B) average for green from our tests for the DRIVING sensor
rG= 47
gG= 115
bG= 16
normrG = rG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))
normgG = gG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))
normbG = bG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))

# (R, G, B) average for green from our tests for the DELIVERY sensor
rGDel = 50
gGDel= 107
bGDel= 30
normrGDel = rGDel / sqrt(pow(rGDel, 2) + pow(gGDel, 2) + pow(bGDel, 2))
normgGDel = gGDel / sqrt(pow(rGDel, 2) + pow(gGDel, 2) + pow(bGDel, 2))
normbGDel = bGDel / sqrt(pow(rGDel, 2) + pow(gGDel, 2) + pow(bGDel, 2))

# (R, G, B) average for blue from our tests for the DRIVING sensor
rB = 34
gB = 47
bB = 38
normrB = rB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))
normgB = gB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))
normbB = bB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))

# (R, G, B) average for blue from our tests for the DELIVERY sensor
rBDel = 30
gBDel = 50
bBDel = 80.4
normrBDel = rBDel / sqrt(pow(rBDel, 2) + pow(gBDel, 2) + pow(bBDel, 2))
normgBDel = gBDel / sqrt(pow(rBDel, 2) + pow(gBDel, 2) + pow(bBDel, 2))
normbBDel = bBDel / sqrt(pow(rBDel, 2) + pow(gBDel, 2) + pow(bBDel, 2))

# (R, G, B) average for purple from our tests for the DRIVING sensor
rP = 176
gP = 30
bP = 24
normrP = rP / sqrt(pow(rP, 2) + pow(gP, 2) + pow(bP, 2))
normgP = gP / sqrt(pow(rP, 2) + pow(gP, 2) + pow(bP, 2))
normbP = bP / sqrt(pow(rP, 2) + pow(gP, 2) + pow(bP, 2))


rPDel = 140
gPDel = 50.6
bPDel = 40.6
normrPDel = rPDel / sqrt(pow(rPDel, 2) + pow(gPDel, 2) + pow(bPDel, 2))
normgPDel = gPDel / sqrt(pow(rPDel, 2) + pow(gPDel, 2) + pow(bPDel, 2))
normbPDel = bPDel / sqrt(pow(rPDel, 2) + pow(gPDel, 2) + pow(bPDel, 2))

# (R, G, B) average for white from our tests
rW = 301
gW = 289
bW = 127
normrW = rW / sqrt(pow(rW, 2) + pow(gW, 2) + pow(bW, 2))
normgW = gW / sqrt(pow(rW, 2) + pow(gW, 2) + pow(bW, 2))
normbW = bW / sqrt(pow(rW, 2) + pow(gW, 2) + pow(bW, 2))

rWDel = 301
gWDel = 289
bWDel = 200
normrWDel = rWDel / sqrt(pow(rWDel, 2) + pow(gWDel, 2) + pow(bWDel, 2))
normgWDel = gWDel / sqrt(pow(rWDel, 2) + pow(gWDel, 2) + pow(bWDel, 2))
normbWDel = bWDel / sqrt(pow(rWDel, 2) + pow(gWDel, 2) + pow(bWDel, 2))

def color_detection_drive(rgb):
  """
  Color detection function for the driving color sensor.
  Used to control which way our robot turns.
  """
  #normalized vector from hardcoded data for colors
  if pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5) == 0:
      return ""
  rgb = (rgb[0] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5), rgb[1] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5), 
         rgb[2] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5))
  
  rgbRed = [normrR, normgR, normbR]
  rgbOrange = [normrO,normgO,normbO]
  rgbYellow = [normrY,normgY,normbY]
  rgbGreen = [normrG,normgG,normbG]
  rgbBlue = [normrB,normgB,normbB]
  rgbPurple = [normrP,normgP,normbP]
  rgbWhite = [normrW, normgW, normbW]


  #calculating distance
  distanceFromRed = pow(pow(rgb[0]-rgbRed[0], 2) + pow(rgb[1]-rgbRed[1],2) + pow(rgb[2]-rgbRed[2],2),0.5) 
  distanceFromOrange = pow(pow(rgb[0]-rgbOrange[0], 2) + pow(rgb[1]-rgbOrange[1],2) + pow(rgb[2]-rgbOrange[2],2), 0.5) 
  distanceFromYellow = pow(pow(rgb[0]-rgbYellow[0], 2) + pow(rgb[1]-rgbYellow[1],2) + pow(rgb[2]-rgbYellow[2],2), 0.5) 
  distanceFromGreen = pow(pow(rgb[0]-rgbGreen[0], 2) + pow(rgb[1]-rgbGreen[1],2) + pow(rgb[2]-rgbGreen[2],2), 0.5) 
  distanceFromBlue = pow(pow(rgb[0]-rgbBlue[0], 2) + pow(rgb[1]-rgbBlue[1],2) + pow(rgb[2]-rgbBlue[2],2), 0.5) 
  distanceFromPurple = pow(pow(rgb[0]-rgbPurple[0], 2) + pow(rgb[1]-rgbPurple[1],2) + pow(rgb[2]-rgbPurple[2],2), 0.5) 
  distanceFromWhite = pow(pow(rgb[0]-rgbWhite[0], 2) + pow(rgb[1]-rgbWhite[1],2) + pow(rgb[2]-rgbWhite[2],2), 0.5) 

  distances = {
    "white" : distanceFromWhite,
    "red": distanceFromRed,
    "orange": distanceFromOrange,
    "yellow": distanceFromYellow,
    "green" : distanceFromGreen,
    "blue" : distanceFromBlue, 
    "purple" : distanceFromPurple 
  }

  miniumumDistance = min(distances.values())

  color = [k for k, v in distances.items() if v == miniumumDistance]

  return color[0]

def color_detection_delivery(rgb):
  """
  The color detection algorithm that is used for our delivery zone color sensor.
  """
  if pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5) == 0:
      return ""
  rgb = (rgb[0] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5), rgb[1] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5), 
         rgb[2] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5))
  
  rgbRed = [normrRDel, normgRDel, normbRDel]
  rgbOrange = [normrODel,normgODel,normbODel]
  rgbYellow = [normrYDel,normgYDel,normbYDel]
  rgbGreen = [normrGDel,normgGDel,normbGDel]
  rgbBlue = [normrBDel,normgB,normbBDel]
  rgbPurple = [normrPDel,normgPDel,normbPDel]
  rgbWhite = [normrWDel, normgWDel, normbWDel]


  #calculating distance
  distanceFromRed = pow(pow(rgb[0]-rgbRed[0], 2) + pow(rgb[1]-rgbRed[1],2) + pow(rgb[2]-rgbRed[2],2),0.5) 
  distanceFromOrange = pow(pow(rgb[0]-rgbOrange[0], 2) + pow(rgb[1]-rgbOrange[1],2) + pow(rgb[2]-rgbOrange[2],2), 0.5) 
  distanceFromYellow = pow(pow(rgb[0]-rgbYellow[0], 2) + pow(rgb[1]-rgbYellow[1],2) + pow(rgb[2]-rgbYellow[2],2), 0.5) 
  distanceFromGreen = pow(pow(rgb[0]-rgbGreen[0], 2) + pow(rgb[1]-rgbGreen[1],2) + pow(rgb[2]-rgbGreen[2],2), 0.5) 
  distanceFromBlue = pow(pow(rgb[0]-rgbBlue[0], 2) + pow(rgb[1]-rgbBlue[1],2) + pow(rgb[2]-rgbBlue[2],2), 0.5) 
  distanceFromPurple = pow(pow(rgb[0]-rgbPurple[0], 2) + pow(rgb[1]-rgbPurple[1],2) + pow(rgb[2]-rgbPurple[2],2), 0.5) 
  distanceFromWhite = pow(pow(rgb[0]-rgbWhite[0], 2) + pow(rgb[1]-rgbWhite[1],2) + pow(rgb[2]-rgbWhite[2],2), 0.5) 

  distances = {
    "white" : distanceFromWhite,
    "red": distanceFromRed,
    "orange": distanceFromOrange,
    "yellow": distanceFromYellow,
    "green" : distanceFromGreen,
    "blue" : distanceFromBlue, 
    "purple" : distanceFromPurple 
  }

  # find the closest distance from all the color distances; this is the color that we've detected  
  miniumumDistance = min(distances.values())

  color = [k for k, v in distances.items() if v == miniumumDistance]

  return color[0]

def find_avg_color(color_list):
    """
    finds the most probable color from a list
    """
    # 0: red
    # 1: orange
    # 2: yellow
    # 3: green
    # 4: blue
    # 5: purple
    # 6: white

    color_counter = [0,0,0,0,0,0,0,0]
    for color in color_list:
        if color == "red":
            color_counter[0] = color_counter[0] + 1
        elif color == "orange":
            color_counter[1] = color_counter[1] + 1
        elif color == "yellow":
            color_counter[2] = color_counter[2] + 1
        elif color == "green":
            color_counter[3] = color_counter[3] + 1
        elif color_counter == "blue":
            color_counter[4] = color_counter[4] + 1
        elif color_counter == "purple":
            color_counter[5] = color_counter[5] + 1
        elif color_counter == "white":
            color_counter[6] = color_counter[6] + 1
    
    max = color_counter.index(max(color_counter))
    if max == 0:
        return "red"
    elif max == 1:
        return "orange"
    elif max == 2:
        return "yellow"
    elif max == 3:
        return "green"
    elif max == 4:
        return "blue"
    elif max == 5:
        return "purple"
    else:
        return "white"
    
def find_avg_color_jean(lst):
    color_counter =[lst.count("red"),lst.count("orange"), lst.count("yellow"), lst.count("green"), lst.count("blue"), lst.count("purple")]
    maximum = color_counter.index(max(color_counter))
    if maximum == 0:
        return "red"
    elif maximum == 1:
        return "orange"
    elif maximum == 2:
        return "yellow"
    elif maximum == 3:
        return "green"
    elif maximum == 4:
        return "blue"
    elif maximum == 5:
        return "purple"
    else:
        return "white"