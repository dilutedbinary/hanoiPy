#! /usr/bin/python3    

from collections import deque

class Tower(deque):
    def get_row(self,row):
        try:
            return self[row]
        except IndexError:
            return None


class TerminalDisplay:
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

    def __init__(self,hanoi_instance):
        self.h = hanoi_instance
        self.size = hanoi_instance.size
        self.tower_width = TerminalDisplay.wid(self.size)-2
        self.total_print_width = 2+(3*self.tower_width)

    def wid(count):
        return (((count+1)*2)-1)

    def get_ring_char_width(ring_num):
        if ring_num is None:
            return 0
        else:
            return TerminalDisplay.wid(ring_num)

    def get_tower_string(self,tower, row_number):
        if not isinstance(tower,Tower):
            tower = self.h.towers[tower_index]
        ring_number = tower.get_row(row_number) or None
        ring_char_width = TerminalDisplay.get_ring_char_width(ring_number)
        buff = self.tower_width - ring_char_width
        white = ' '*int((buff/2.0))
        ret = white + ring_char_width*'#'+white
        return ret

    def show(self):
        line = ''
        rows = list(range(self.size))
        rows.reverse()
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
        initial = list(range(self.size))
        initial.reverse()
        self.tower_a.extend(initial)

    def move(self,src,dest):
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
