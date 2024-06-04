try:
    from ursina import *
    from ursina.prefabs.first_person_controller import FirstPersonController
except:
    if input("Sorry, but it looks like ursina is not installed. Proceed to install? (y/n)").lower == "y":
        from pip import main as pip_main
        pip_main(["install", "ursina"])
    else:
        print("Terminating program.")
    from ursina import *
    from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
app = Ursina()
window.fullscreen = True
Sky()

boxes = []
selected = Entity(color=color.white, model="cube", position=(0.5,-0.25,1), scale=0.5, rotaion=(15,15,15), texture="Grass texture.png", parent=camera, origin_y=0.5)

for x in range(-15, 15):
    for z in range(-15, 15):
        box = Entity(color=color.white, model="cube", position=(x,-6,z), texture="Bedrock texture.png", parent=scene, origin_y=0.5, collider="box")
        boxes.append(box)
        box = Entity(color=color.white, model="cube", position=(x,-5,z), texture="Grass texture.png", parent=scene, origin_y=0.5, collider="box")
        boxes.append(box)
        
def input(key):
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            new = Entity(color=color.white, model="cube", position=hit_info.entity.position + mouse.normal, texture=selected.texture, parent=scene, origin_y=0.5, collider="box")
            boxes.append(new)
    elif key == "right mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if (hit_info.hit) and (str(hit_info.entity.texture) != "Bedrock texture.png"):
            destroy(hit_info.entity)
            boxes.remove(hit_info.entity)
    
    if key == "1":
        selected.texture = "Grass texture.png"
    elif key == "2":
        selected.texture = "Dirt texture.png"
    elif key == "3":
        selected.texture = "Stone texture.png"
    elif key == "4":
        selected.texture = "Stone brick texture.png"

player = FirstPersonController(position=(0,50,0))
app.run()

