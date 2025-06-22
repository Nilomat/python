
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()

red = 255
green= 100
blue= 10
boxes = []
block = 1
def add_box4(pos):
   boxes.append( Button(
        parent=scene,
        model="sphere",
        origin=0.5,
        color=color.rgb(255,0,0),
        position= pos,
        texture="brick"
        
    )
    )
def add_box3(pos):
   boxes.append( Button(
        parent=scene,
        model="cube",
        origin=0.5,
        color=color.rgb(211,211,211),
        position= pos,
        texture="brick"
        
    )
    )

def add_box(pos):
   boxes.append( Button(
        parent=scene,
        model="cube",
        origin=0.5,
        color=color.rgb(255,100,10),
        position= pos,
        texture="brick"
    )
    )
def add_box2(pos):
   boxes.append( Button(
        parent=scene,
        model="cube",
        origin=0.5,
        color=color.rgb(10,255,10),
        position= pos,
        texture="grass"
    )
    )
   
   

for x in range(30):
    for y in range(40):
        add_box2((x,0,y))

def input(key):
       global block
       if key == "1": 
            
            block = 1
            print_on_screen("brick",0,0.5,0.1,0.2)
            print(block)
       if key == "2": 
           
            block = 2
            print_on_screen("dirt",0,0.5,0.1,0.2)
            print(block)
       if key == "3": 
           block = 3
           print_on_screen("stone",0,0.5,0.1,0.2)
           print(block)
       if key == "4":
           block = 4
           print_on_screen("sphere?",0,0.5,0.1,0.2)
           print(block)
       
       for box in boxes:
        if box.hovered:
            if key == "right mouse down": 
                print(block)
                if block == 1:
                   
                    add_box(box.position + mouse.normal)
                if block == 2:
                    
                    add_box2(box.position + mouse.normal)
                if block == 3:
                    
                    add_box3(box.position + mouse.normal)
                if block == 4:
                    
                    add_box4(box.position + mouse.normal)
            if key == "f" :
                file = open('read.txt', 'w') 
                file.write(str(boxes)) 
                file.close() 
            if key == "left mouse down":  
                boxes.remove(box)
                destroy(box)
            
app.run()
