import pygame as pg
FPS = 30

frames = ["frame 0","frame 1","frame 2","frame 3","frame 4","frame 5"]

clock = pg.time.Clock()


current_frame = 0
last_update = 0

def animate():
    global last_update
    global current_frame
    now = pg.time.get_ticks()
    if now - last_update > 350:
        current_frame = (current_frame + 1) % len(frames)
        print(frames[current_frame])
        # print(now)
        last_update = now
  

while True:
    clock.tick(FPS)
    animate()
    