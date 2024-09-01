import pgzrun
import random
#start
FONT_option=(255,255,255)
WIDTH=800
HEIGHT=600
TITLE="RECYCLE"
#pos
CENTER_x=WIDTH/2
CENTER_y=HEIGHT/2
CENTER=(CENTER_x,CENTER_y)
#variable
FINAL_LEVEL=10
start_speed=10
ITEMS=["bag","battery","bottle","chips"]
game_over=False
game_completed=False
current_level=1
items=[]
animations=[]

def draw():
    global items, current_level, game_completed, game_over
    screen.clear()
    screen.blit("bground",(0,0))
    if game_over:
        display_message("GAME OVER", "TRY AGAIN")
    elif game_completed:
        display_message("YOU WIN", "GOOD JOB")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

def get_option_to_create(number_of_extra_items):
    items_to_create=["paper"]
    for i in range(0, number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option+"img")
        new_items.append(item)  
    return new_items

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def layout_items(item_to_layout):
    number_of_gaps=len(item_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(item_to_layout)
    for index, item in enumerate(item_to_layout):
        new_xpos=(index+1)*gap_size
        item.x=new_xpos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration=start_speed-current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration, on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper"in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level, items, animations, game_completed
    stop_animations(animations)
    if current_level==FINAL_LEVEL:
        game_completed=True
    else:
        current_level=current_level+1
        items=[]
        animations=[]

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, subheading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color="WHITE")
    screen.draw.text(subheading_text, fontsize=30, center=(CENTER_x,CENTER_y+20), color="white")
pgzrun.go()
