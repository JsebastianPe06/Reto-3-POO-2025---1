import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0

class Line(Point):
    def __init__(self, point_start:Point, point_end:Point):
        self.point_start = point_start
        self.point_end = point_end
        self.length = math.sqrt((point_end.x-point_start.x)**2+(point_end.y-point_start.y)**2)
        if((point_start.x-point_end.x)==0):
            self.slope = None
            self.cut_point = None
        elif((point_start.y-point_end.y)==0):
            self.slope = 0
            self.cut_point = point_start.y
        else:
            self.slope = (point_start.y-point_end.y)/(point_start.x-point_end.x)
            self.cut_point = -(point_start.y/self.slope)+point_start.x
    
    def evaluate_value_function(self, x:float, reverse:bool)->float:
        if(reverse==False):
            return (self.slope*x)+self.cut_point if(self.slope!=None) else self.point_start.x
        else:
            if(self.cut_point==None or self.slope==0):
                return None
            return (x-self.cut_point)/self.slope
    
    def compute_length(self)->bool:
        return self.length
    
    def compute_slope(self):
        return math.atan(self.slope)*180/math.pi if(self.slope!=None) else 90
    
    def compute_horizontal_cross(self)->Point:
        if(self.slope!=0):
            if(self.slope==None):
                return Point(self.point_end.x, 0)
            else:
                return Point(self.evaluate_value_function(0, 1), 0)
        else:
            return None
    
    def compute_vertical_cross(self)->Point:
        if(self.slope!=None):
            if(self.slope==0):
                return Point(0, self.point_end.y)
            else:
                return Point(0, self.evaluate_value_function(0, 0))
        else:
            return None

class Rectangle:
    def __init__(self, line1:Line, line2:Line, line3:Line, line4:Line):
        lis = [line1, line2, line3, line4]
        horizontal = []
        vertical = []
        for i in range(len(lis)):
            horizontal.append(lis[i]) if(lis[i].slope==0) else None
            vertical.append(lis[i]) if(lis[i].slope==None) else None
        val1 = horizontal[0].length==horizontal[1].length
        val2 = vertical[0].length==vertical[1].length
        if(val1 and val2):    
            self.width = horizontal[0].length
            self.height = vertical[0].length
            self.b_left = Point(min([line.point_start.x for line in lis]),
                                min([line.point_start.y for line in lis]))
            self.t_right = Point(max([line.point_start.x for line in lis]),
                                max([line.point_start.y for line in lis]))
            self.center = Point(self.b_left.x+self.width/2,
                                self.b_left.y+self.height/2)

    def compute_area(self)-> float:
        return self.width*self.height

    def compute_perimeter(self)-> float:
        return (self.width*2)+(self.height*2)
    
    def compute_interference_point(self,point:Point)->bool:
        val_x:bool = point.x>=self.b_left.x and point.x<=self.b_left.x+self.width
        val_y:bool = point.y>=self.b_left.y and point.y<=self.b_left.y+self.height
        return val_y and val_x
    
    def compute_interference_line(self,line:Line)->bool:
        a:bool = self.b_left.y<=line.evaluate_value_function(self.b_left.x,0)<=self.t_right.y
        c:bool = self.b_left.y<=line.evaluate_value_function(self.t_right.x,0)<=self.t_right.y
        if(line.evaluate_value_function(self.t_right.y,1)!=None):
            b:bool = self.b_left.x<=line.evaluate_value_function(self.b_left.y,1)<=self.t_right.x
            d:bool = self.b_left.x<=line.evaluate_value_function(self.t_right.y,1)<=self.t_right.x
            return a or b or c or d
        return a or c

class Square(Rectangle):
    def __init__(self, side:float, bottom_left:Point):
        super().__init__(side, side, side, side)

punto1 = Point(3, 4)
punto2 = Point(1, 4)
punto4 = Point(3, 6)
punto5 = Point(1, 6)
linea1 = Line(punto1,punto4)
linea2 = Line(punto4,punto5)
linea3 = Line(punto5,punto2)
linea4 = Line(punto2,punto1)
rec = Rectangle(linea1,linea2,linea3,linea4)

punto3 = Point(6, 6)
linea = Line(punto2, punto3)

print(rec.compute_area())
print(rec.compute_interference_point(punto2))
print(rec.compute_interference_line(linea))
