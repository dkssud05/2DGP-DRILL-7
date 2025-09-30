from pico2d import *
import random

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400, 30)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global running
    running = True

    global world
    world = []
    grass = Grass()
    world.append(grass)

    global team
    team = [Boy() for _ in range(11)]
    world += team

def update_world():
    for game_object in world:
        game_object.update()

def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()