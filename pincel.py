#biblioteca Py5 necessária
def setup():
    
    #tela
    size(800, 800)
    #pincel no centro do mouse
    rect_mode(CENTER)
    background(0, 255, 0)
    
def draw():
    
    #quadrado sem preenchimento
    no_fill()
    #cores aleatórias
    stroke(random(256), random(256), random(256))
    if is_mouse_pressed:
        rect(mouse_x, mouse_y, 50, 50)

#apagar tela pressionando 'e'
def key_pressed():
    if key == 'e':
        background(0, 255, 0)