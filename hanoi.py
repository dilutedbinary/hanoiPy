#! /usr/bin/python3    

from collections import deque

class Tower(deque):
    height =0;
    def set_height(self, height):
        self.height = height
    def get_row(self,row):
        try:
            return self[self.height-1 -row]
        except IndexError:
            return None


class TerminalDisplay:
    '''
             Tower0
               |     Tower1
               |       |     Tower2
               |       |       |
               v       v       v
     
    row0>      X       X       X    <size = 0
    row1>     XXX     XXX     XXX   <size = 1
    row2>    XXXXX   XXXXX   XXXXX  <size = 2
    row3>   XXXXXXX XXXXXXX XXXXXXX <size = 3
    '''

    def __init__(self,hanoi_instance):
        self.h = hanoi_instance
        self.size = hanoi_instance.size
        self.tower_width = TerminalDisplay.wid(self.size)
        self.total_print_width = 3*self.tower_width+2
        print(self.tower_width)
    def wid(row_num):
        return ((row_num*2)-1)

    def get_ring_char_width(ring_num):
        if ring_num is None:
            return 0
        else:
            return TerminalDisplay.wid(ring_num+1)

    def get_tower_string(self,tower, row_number):
        ring_size = tower.get_row(row_number)

        ring_char_width = TerminalDisplay.get_ring_char_width(ring_size)
        res = '{val:^{width}}'.format(width=self.tower_width,val="#"*ring_char_width)

        return res

    def show(self):
        line = ''
        rows = list(range(self.size))
        for i in rows:
            full_row = ''
            for tow in self.h.towers:
                full_row+=self.get_tower_string(tow,i)
            print(full_row)
         


class Hanoi:
    def __init__(self, size):
        self.size = size
        self.reset()
        self.display = None
        
    def add_display(self, displayer):
        self.displayer = displayer

    def reset(self):
        self.tower_a = Tower()
        self.tower_b = Tower()
        self.tower_c = Tower()
        
        self.towers = (self.tower_a,self.tower_b,self.tower_c)
        for t in self.towers:
            t.set_height(self.size)
        initial = list(range(self.size))
        initial.reverse()
        self.tower_a.extend(initial)

    def move(self,src,dest):
        print("Moving from {} -> {}".format(src,dest))
        self.towers[dest].append(self.towers[src].pop())

    def show(self):
        self.displayer.show()

    def show_raw(self):
        print('TowA: {}'.format(self.towers[0]))
        print('TowB: {}'.format(self.towers[1]))
        print('TowC: {}'.format(self.towers[2]))


print('test')
t = Hanoi(4)
t.add_display(TerminalDisplay(t))
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
