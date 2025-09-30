from pico2d import *
import random

class Big_ball:
    def __init__(self):
        self.x = random.randint(41, 759)
        self.y = 599
        self.image = load_image('ball41x41.png')
    def update(self):
        self.y -= random.randint(0, 5)
        if self.y < 70:
            self.y = 70
    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)

class Small_ball:
    def __init__(self):
        self.x = random.randint(21, 779)
        self.y = 599
        self.image = load_image('ball21x21.png')
    def update(self):
        self.y -= random.randint(0, 5)
        if self.y < 55:
            self.y = 55
    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.frame = random.randint(0, 7)
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

    total_balls = 20
    x = random.randint(1, total_balls - 1)
    y = total_balls - x
    global small_balls
    small_balls = [Small_ball() for _ in range(x)]
    world += small_balls

    global big_balls
    big_balls = [Big_ball() for _ in range(y)]
    world += big_balls

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