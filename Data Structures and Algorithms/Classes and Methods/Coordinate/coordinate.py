

class Coordinate(object):
    ''' takes two integer values on initialization and assigns to the
        coordinate objects data attributes, these will be used to plot
        onto a graph, expecting only integers'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'

    def distance(self, other):
        # Euclidean distance formula
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return float((x_diff_sq + y_diff_sq)**0.5)

try:
    xval = int(input("X Axis Coordinate:"))
    yval = int(input("Y Axis Coordinate:"))
except:
    raise Exception('Invalid Values for Coordinates')

coord = Coordinate(xval,yval)
origin = Coordinate(0,0)

print('X coordinate provided:',coord.x,end='     ')
print('Y coordinate of origin:',origin.x,end='     ')
print(f'Euclidean distance {coord.distance(origin):.2f}')
print(coord)
