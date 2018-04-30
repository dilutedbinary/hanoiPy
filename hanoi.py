#! /usr/bin/python3    

from collections import deque

def make_list(size):
    i = 0
    initial = []
    while i<size:
        initial.append(i)
        i += 1
    return initial

def wid(count):
    return (((count+1)*2)-1)



class Tower(deque):
    def get_row(self,row):
        try:
            return self[row]
        except IndexError:
            return None

 '''
         Tower0
           |     Tower1
           |       |     Tower2
           |       |       |
           v       v       v
     
row3>      X       X       X    <size = 0
row2>     XXX     XXX     XXX   <size = 1
row1>    XXXXX   XXXXX   XXXXX
row0>   XXXXXXX XXXXXXX XXXXXXX   

'''

class TerminalDisplay:
    def __init__(self,hanoi_instance):
        def h = hanoi_instance

    def get_tower_string(self,tower_index, row_number):
        tower = self.h.towers[tower_index]
        ring_size = tower.get_row(row_number)
        buff = self.tower_width - wid(ring_size)
        white = ' '*int((buff/2.0))
        ret = white + wid(count)*'#'+white
        return ret
            


class Hanoi:
    def __init__(self, size, display):
        self.size = size
        self.reset()
        self.display = None
        
    def add_display(display):
        self.display = display

    def reset(self):
        self.tower_a = Tower()
        self.tower_b = Tower()
        self.tower_c = Tower()
        self.towers = (self.tower_a,self.tower_b,self.tower_c)
        initial = list(range(self.size))
        initial.reverse()
        self.tower_a.extend(initial)

    def print(self)
        visual_tower_width = wid(size)-2
        total_print_width = 2+(3*self.tower_width)

    def move(self,src,dest):
        self.towers[dest].append(self.towers[src].pop())

            
    def show(self):
        line = ''
        rows = make_list(self.size)
        rows.reverse()
        for i in rows:
            print(i)
            full_row = ''
            for tow in self.towers:
                full_row+=self.get_tower_string(tow,i)
            print(full_row)

    def show_raw(self):
        print('TowA: {}'.format(self.towers[0]))
        print('TowB: {}'.format(self.towers[1]))
        print('TowC: {}'.format(self.towers[2]))
print('test')
t = Hanoi(4)
t.show()
t.show_raw()
t.move(0,2)
t.move(0,1)
t.show_raw()
t.show()



'''
size = 4
   #       #
  ###     ### 
 #####   #####
####### #######
'''
