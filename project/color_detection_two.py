from math import sqrt

# (R, G, B) average for red from our tests for the DRIVING sensor
rR = 245
gR = 46
bR = 11
normrR = rR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))
normgR = gR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))
normbR = bR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))


# (R, G, B) average for orange from our tests for the DRIVING sensor
rO = 265
gO = 76
bO = 16
normrO = rO / sqrt(pow(rO, 2) + pow(gO, 2) + pow(bO, 2))
normgO = gO / sqrt(pow(rO, 2) + pow(gO, 2) + pow(bO, 2))
normbO = bO / sqrt(pow(rO, 2) + pow(gO, 2) + pow(bO, 2))

# (R, G, B) average for yellow from our tests for the DRIVING sensor
rY = 255
gY = 230
bY = 20
normrY = rY / sqrt(pow(rY, 2) + pow(gY, 2) + pow(bY, 2))
normgY = gY / sqrt(pow(rY, 2) + pow(gY, 2) + pow(bY, 2))
normbY = bY / sqrt(pow(rY, 2) + pow(gY, 2) + pow(bY, 2))


# (R, G, B) average for green from our tests for the DRIVING sensor
rG= 47
gG= 115
bG= 16
normrG = rG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))
normgG = gG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))
normbG = bG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))


# (R, G, B) average for blue from our tests for the DRIVING sensor
rB = 34
gB = 47
bB = 38
normrB = rB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))
normgB = gB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))
normbB = bB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))

# (R, G, B) average for purple from our tests for the DRIVING sensor
rP = 176
gP = 30
bP = 24
normrP = rP / sqrt(pow(rP, 2) + pow(gP, 2) + pow(bP, 2))
normgP = gP / sqrt(pow(rP, 2) + pow(gP, 2) + pow(bP, 2))
normbP = bP / sqrt(pow(rP, 2) + pow(gP, 2) + pow(bP, 2))


# (R, G, B) average for white from our tests
rW = 301
gW = 289
bW = 127
normrW = rW / sqrt(pow(rW, 2) + pow(gW, 2) + pow(bW, 2))
normgW = gW / sqrt(pow(rW, 2) + pow(gW, 2) + pow(bW, 2))
normbW = bW / sqrt(pow(rW, 2) + pow(gW, 2) + pow(bW, 2))

# (R, G, B) average for red from our tests for the DELIVERY sensor
rRDel = 220
gRDel = 37
bRDel = 26
normrRDel = rRDel / sqrt(pow(rRDel, 2) + pow(gRDel, 2) + pow(bRDel, 2))
rrStDev = 0.00362998
normgRDel = gRDel / sqrt(pow(rRDel, 2) + pow(gRDel, 2) + pow(bRDel, 2))
rgStDev =  0.01308116
normbRDel = bRDel / sqrt(pow(rRDel, 2) + pow(gRDel, 2) + pow(bRDel, 2))
rbStDev = 0.01249792


# (R, G, B) average for orange from our tests for the DELIVERY sensor
rODel = 260
gODel = 70
bODel = 30
normrODel = rODel / sqrt(pow(rODel, 2) + pow(gODel, 2) + pow(bODel, 2))
#orStDev = 
normgODel = gODel / sqrt(pow(rODel, 2) + pow(gODel, 2) + pow(bODel, 2))
#ogStDev =
normbODel = bODel / sqrt(pow(rODel, 2) + pow(gODel, 2) + pow(bODel, 2))
#obStDev =


# (R, G, B) average for yellow from our tests for the DELIVERY sensor
rYDel = 166
gYDel = 130
bYDel = 30
normrYDel = rYDel / sqrt(pow(rYDel, 2) + pow(gYDel, 2) + pow(bYDel, 2))
normgYDel = gYDel / sqrt(pow(rYDel, 2) + pow(gYDel, 2) + pow(bYDel, 2))
normbYDel = bYDel / sqrt(pow(rYDel, 2) + pow(gYDel, 2) + pow(bYDel, 2))

# (R, G, B) average for green from our tests for the DELIVERY sensor
rGDel = 50
gGDel= 107
bGDel= 30
normrGDel = rGDel / sqrt(pow(rGDel, 2) + pow(gGDel, 2) + pow(bGDel, 2))
normgGDel = gGDel / sqrt(pow(rGDel, 2) + pow(gGDel, 2) + pow(bGDel, 2))
normbGDel = bGDel / sqrt(pow(rGDel, 2) + pow(gGDel, 2) + pow(bGDel, 2))

# (R, G, B) average for blue from our tests for the DELIVERY sensor
rBDel = 30
gBDel = 50
bBDel = 80.4
normrBDel = rBDel / sqrt(pow(rBDel, 2) + pow(gBDel, 2) + pow(bBDel, 2))
normgBDel = gBDel / sqrt(pow(rBDel, 2) + pow(gBDel, 2) + pow(bBDel, 2))
normbBDel = bBDel / sqrt(pow(rBDel, 2) + pow(gBDel, 2) + pow(bBDel, 2))

# (R, G, B) average for purple from our tests for the DELIVERY sensor
rPDel = 169.76
gPDel = 28.75
bPDel = 46.135
normrPDel = rPDel / sqrt(pow(rPDel, 2) + pow(gPDel, 2) + pow(bPDel, 2))
prStDev = 0.00378445
normgPDel = gPDel / sqrt(pow(rPDel, 2) + pow(gPDel, 2) + pow(bPDel, 2))
pgStDev = 0.0112719
normbPDel = bPDel / sqrt(pow(rPDel, 2) + pow(gPDel, 2) + pow(bPDel, 2))
pbStDev = 0.0090617

# (R, G, B) average for white from our tests for the DELIVERY sensor
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
  rgbRedStDev = [rrStDev, rgStDev, rbStDev]
  rgbOrange = [normrODel,normgODel,normbODel]
  rgbYellow = [normrYDel,normgYDel,normbYDel]
  rgbGreen = [normrGDel,normgGDel,normbGDel]
  rgbBlue = [normrBDel,normgB,normbBDel]
  rgbPurple = [normrPDel,normgPDel,normbPDel]
  rgbPurpleStDev = [prStDev, pgStDev, pgStDev]
  rgbWhite = [normrWDel, normgWDel, normbWDel]


  #calculating distance
  farDistanceFromRed = pow(pow(rgb[0]-rgbRed[0] + (5*rgbRedStDev[0]), 2) + pow(rgb[1]-rgbRed[1] + (5*rgbRedStDev[1]),2) + pow(rgb[2]-rgbRed[2] + (5*rgbRedStDev[2]),2),0.5) 
  distanceFromRed = pow(pow(rgb[0]-rgbRed[0], 2) + pow(rgb[1]-rgbRed[1],2) + pow(rgb[2]-rgbRed[2],2),0.5) 
  smallDistanceFromRed = pow(pow(rgb[0]-rgbRed[0] - (5*rgbRedStDev[0]), 2) + pow(rgb[1]-rgbRed[1] - (5*rgbRedStDev[1]),2) + pow(rgb[2]-rgbRed[2] - (5*rgbRedStDev[2]),2),0.5) 

  distanceFromOrange = pow(pow(rgb[0]-rgbOrange[0], 2) + pow(rgb[1]-rgbOrange[1],2) + pow(rgb[2]-rgbOrange[2],2), 0.5) 

  distanceFromYellow = pow(pow(rgb[0]-rgbYellow[0], 2) + pow(rgb[1]-rgbYellow[1],2) + pow(rgb[2]-rgbYellow[2],2), 0.5) 

  distanceFromGreen = pow(pow(rgb[0]-rgbGreen[0], 2) + pow(rgb[1]-rgbGreen[1],2) + pow(rgb[2]-rgbGreen[2],2), 0.5) 

  distanceFromBlue = pow(pow(rgb[0]-rgbBlue[0], 2) + pow(rgb[1]-rgbBlue[1],2) + pow(rgb[2]-rgbBlue[2],2), 0.5)

  farDistanceFromPurple = pow(pow(rgb[0]-rgbPurple[0] + (5*rgbPurpleStDev[0]), 2) + pow(rgb[1]-rgbPurple[1] - (5*rgbPurpleStDev[1]),2) + pow(rgb[2]-rgbPurple[2] - (5*rgbPurpleStDev[2]),2), 0.5)  
  distanceFromPurple = pow(pow(rgb[0]-rgbPurple[0], 2) + pow(rgb[1]-rgbPurple[1],2) + pow(rgb[2]-rgbPurple[2],2), 0.5) 
  smallDistanceFromPurple = pow(pow(rgb[0]-rgbPurple[0] - (5*rgbPurpleStDev[0]), 2) + pow(rgb[1]-rgbPurple[1] - (5*rgbPurpleStDev[1]),2) + pow(rgb[2]-rgbPurple[2] - (5*rgbPurpleStDev[2]),2), 0.5) 

  distanceFromWhite = pow(pow(rgb[0]-rgbWhite[0], 2) + pow(rgb[1]-rgbWhite[1],2) + pow(rgb[2]-rgbWhite[2],2), 0.5) 

  distances = {
    "white" : distanceFromWhite,
    "redsmall" : smallDistanceFromRed,
    "red": distanceFromRed,
    "redfar" : farDistanceFromRed,
    "orange": distanceFromOrange,
    "yellow": distanceFromYellow,
    "green" : distanceFromGreen,
    "blue" : distanceFromBlue, 
    "purple" : smallDistanceFromPurple,
    "purple" : distanceFromPurple,
    "purple" :farDistanceFromPurple
  }

  # find the closest distance from all the color distances; this is the color that we've detected  
  miniumumDistance = min(distances.values())

  color = [k for k, v in distances.items() if v == miniumumDistance]

  return color[0]
