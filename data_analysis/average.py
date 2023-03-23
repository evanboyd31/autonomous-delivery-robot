try:
    file = open("color_sensor_white.csv", "r")
    counter = 0
    sumR = 0
    sumG = 0
    sumB = 0
    for line in file:
        rgb = line.split(',')
        rgb[0] = int(rgb[0])
        rgb[1] = int(rgb[1])
        rgb[2] = rgb[2].replace('\n', '')
        rgb[2] = int(rgb[2])
        sumR += rgb[0]
        sumG += rgb[1]
        sumB += rgb[2]
        counter += 1
        print(rgb)
    
    print("R: " + str(sumR/counter))
    print("G: " + str(sumG/counter))
    print("B: " + str(sumB/counter))
except:
    print("oops")