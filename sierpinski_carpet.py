import tkinter
root=tkinter.Tk()
canvas= tkinter.Canvas(root,width=500,heigh=500)
canvas.pack()

def sierpinski_triangle(xy,dlzka_strany,breakpoint):
    if breakpoint != 0:
        x=xy[0]
        y=xy[1]
        canvas.create_line(x,y,x+dlzka_strany,y)
        canvas.create_line(x,y,x+(dlzka_strany/2),y-(dlzka_strany**2-(dlzka_strany/2)**2)**0.5)
        canvas.create_line(x+ (dlzka_strany / 2), y - (dlzka_strany ** 2 - (dlzka_strany / 2) ** 2) ** 0.5, x +dlzka_strany, y)

        sierpinski_triangle(xy,dlzka_strany/2,breakpoint-1)
        sierpinski_triangle([x+(dlzka_strany/2),y],dlzka_strany/2,breakpoint-1)
        sierpinski_triangle([x+dlzka_strany/4,y-((dlzka_strany**2-(dlzka_strany/2)**2)**0.5)/2],dlzka_strany/2, breakpoint-1)

#sierpinski_triangle([20,400],300,8)

def sierpinski_carpet(suradnice,dlzka_strany,breakpoint):
    if breakpoint !=0:
        x1=suradnice[0]
        y1=suradnice[1]
        upravena_strana= dlzka_strany/3
        x2=x1+dlzka_strany
        y2=y1+dlzka_strany
        canvas.create_rectangle(x1,y1,x2,y2)

        sierpinski_carpet(suradnice,upravena_strana,breakpoint-1)
        sierpinski_carpet([x1+upravena_strana,y1], upravena_strana, breakpoint - 1)
        sierpinski_carpet([x1 + 2 * upravena_strana, y1], upravena_strana, breakpoint - 1)
        sierpinski_carpet([x1,y1+upravena_strana], upravena_strana, breakpoint - 1)
        sierpinski_carpet([x1, y1 + 2*upravena_strana], upravena_strana, breakpoint - 1)
        sierpinski_carpet([x1+2*upravena_strana, y1 + upravena_strana], upravena_strana, breakpoint - 1)
        sierpinski_carpet([x1 + upravena_strana, y1 +2* upravena_strana], upravena_strana, breakpoint - 1)
        sierpinski_carpet([x1 +2* upravena_strana, y1 + 2 * upravena_strana], upravena_strana, breakpoint - 1)

sierpinski_carpet([50,100],400,6)
root.mainloop()
