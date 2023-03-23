try:
    file = open("color_sensor_yellow.csv", "r")
    counter = 0
    normalizedR = []
    normG = []
    normB = []
    for line in file:
        rgb = line.split(',')
        rgb[0] = int(rgb[0])
        rgb[1] = int(rgb[1])
        rgb[2] = rgb[2].replace('\n', '')
        rgb[2] = int(rgb[2])
        sum = rgb[0] + rgb[1] + rgb[2]
        normalizedR.append(rgb[0] / sum)
        normG.append(rgb[1] / sum)
        normB.append(rgb[2] / sum)
        counter += 1
        print(rgb)
    sumR = 0
    sumG = 0
    sumB = 0
    for r in normalizedR:
        sumR += r
    for g in normG:
        sumG += g
    for b in normB:
        sumB += b
    print("normR mean: " + str(sumR/len(normalizedR)))
    print("normG: " + str(sumG/len(normG)))
    print("normB: " + str(sumB/len(normB)))
except:
    print("oops")