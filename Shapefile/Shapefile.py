import fiona, os, pandas


# Get coordinates

output = open("output.txt", "a")

for file in os.listdir("./Shapes"):
    if file.endswith(".shp"):
        output.write(file + '\n\n')
        thefile = fiona.open('./Shapes/' + file)
        for shapes in thefile:
            output.write(str((shapes)['geometry']) + '\n\n\n')

output.close()


# Clean the txt file

with open('output.txt', 'r') as file :
  data = file.read()

data = data.replace('shapes\\', '').replace('.shp', '').replace('{\'type\': \'', '').replace('\', \'coordinates\': [[', '(').replace('1,','1').replace('2,','2').replace('3,','3').replace('4,','4').replace('5,','5').replace('6,','6').replace('7,','7').replace('8,','8').replace('9,','9').replace(')', '').replace('(', '').replace('Polygon', 'MultiPolygon (((').replace(']]}', ')))')

with open('output.txt', 'w') as file:
  file.write(data)

