#! /usr/bin/python3

from collections import deque


class Tower(deque):
    height = 0
    index = 0

    def __init__(self, height, index, isFull=False):
        self.height = height
        self.index = index
        super().__init__()
        if isFull:

            super().__init__()
            init = list(range(height))
            init.reverse()
            self.extend(init)

    def get_index(self):
        return self.index

    def get_row(self, row):
        try:
            return self[self.height-1 - row]
        except IndexError:
            return None

    def top_disk_size(self):
        if len(self):
            return self[-1]
        else:
            return self.height+1  # Always legal to move to empty

    def legal_move_to(self, targ_tower):
        return self.top_disk_size() < targ_tower.top_disk_size()


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

    def __init__(self, hanoi_instance):
        self.h = hanoi_instance
        self.size = hanoi_instance.size
        self.print_char = u"\u2587"  # Solid block
        self.tower_width = TerminalDisplay.wid(self.size)
        self.total_print_width = 3*self.tower_width+2
        debug(self.tower_width)

    def wid(row_num):
        return ((row_num*2)-1)

    def get_ring_char_width(ring_num):
        if ring_num is None:
            return 0
        else:
            return TerminalDisplay.wid(ring_num+1)

    def get_tower_string(self, tower, row_number):
        ring_size = tower.get_row(row_number)

        ring_char_width = TerminalDisplay.get_ring_char_width(ring_size)

        res = '{val:^{width}}'.format(
            width=self.tower_width, val=self.print_char*ring_char_width or '|')

        return res

    def show(self):

        rows = list(range(self.size))
        rows.reverse()
        rows.append(-1)
        rows.reverse()
        for i in rows:
            full_row = ''
            for tow in self.h.towers:
                full_row += self.get_tower_string(tow, i)
            print(full_row)


class Move:
    _source = None
    _destination = None

    def __init__(self, src_tower, dst_tower):
        self._source = src_tower
        self._destination = dst_tower

    def execute(self, force_move=False):
        if not force_move:
            if not self._source.legal_move_to(self._destination):
                raise Exception('Invalid Move attempted')
        self._destination.append(self._source.pop())

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '({}->{})'.format(
            self._source.get_index(), self._destination.get_index())


class Hanoi:
    towers = None

    def __init__(self, size):
        self.size = size
        self.reset()
        self.display = None
        self.move_history = []

    def add_display(self, displayer):
        self.displayer = displayer

    def reset(self):
        temp_towers = []
        for idx in range(0, 3):
            temp_towers.append(Tower(self.size, index=idx, isFull=not(idx)))

        self.towers = tuple(temp_towers)

#  def move(self, src, dest):
#       print("Moving from {} -> {}".format(src, dest))
#        self.towers[dest].append(self.towers[src].pop())

    def show(self):
        self.displayer.show()

    def show_raw(self):
        print('TowA: {}'.format(self.towers[0]))
        print('TowB: {}'.format(self.towers[1]))
        print('TowC: {}'.format(self.towers[2]))

    def get_valid_moves(self):
        valid_moves = []
        for src_tower in self.towers:
            debug('tower {}'.format(src_tower.get_index()))
            for dst_tower in self.towers:
                if src_tower.legal_move_to(dst_tower):
                    debug('added')
                    valid_moves.append(Move(src_tower, dst_tower))

        return valid_moves


debug_enabled = True


def debug(*args, **kwargs):
    if debug_enabled:
        print('>> DEBUG: ', end="")
        print(*args, **kwargs)


game = Hanoi(5)
game.add_display(TerminalDisplay(game))
game.show()
print(game.get_valid_moves())

game.get_valid_moves()[0].execute()
game.show()
print(game.get_valid_moves())
game.get_valid_moves()[0].execute()
game.show()
print(game.get_valid_moves())
# game.show_raw()


'''
size = 4
   #       #
  ###     ###
 #####   #####
####### #######
'''
