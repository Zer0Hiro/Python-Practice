# use the following strings:

# "Enter v(0-100) m/s and a (0-90 as):"
# "Time: %.1f.....S=%5.2f H=%5.2f" ......"
# "Fallen!"
# "Finish"
import math

def height(a,v,t):
    g = 9.81
    v_y = math.sin(deg2rad(a))*v
    h = v_y*t-(g*(t**2))/2
    return h
    
def horizontal(a,v,t):
    v_x = math.cos(deg2rad(a))*v
    s = v_x*t
    return s
   
def deg2rad(a):
    rad = a*(math.pi/180)
    return rad

def main():
   a = 0
   v = 0
   while a != -1 and v != -1:
       t = 0.1
       h = 0
       v,a = eval(input("Enter v(0-100) m/s and a (0-90 degrees):"))
       if 0 <= a <= 90 and 0 <= v <= 100: 
           while h >= 0:
               #deg = deg2rad(a)
               h = height(a, v, t)
               dist = horizontal(a, v, t)
               print("Time: %.1f.....S=%5.2f H=%5.2f......"%(t,dist,h))
               t += 0.1
           print("Fallen!")
           print()
       else:
           a = -1 
           v = -1
   print("Finish")
main()