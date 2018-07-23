#! /usr/bin/python3

from collections import deque

# import curses


class Tower(deque):
    height = 0
    index = 0

    def __init__(self, height, index, isFull=False):
        self.height = height
        self.index = index
        super().__init__()
        if isFull:
            print('full one! {} '.format(height))
            super().__init__()
            init = list(range(height))
            init.reverse()
            self.extend(init)
            print(self)

    def is_full(self):
        return len(self) == self.height

    def get_index(self):
        return self.index

    def get_row(self, row):
        try:
            return self[self.height-1 - row]
        except IndeExrror:
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

        self.h = hanoi_instance.game_state
        self.size = hanoi_instance.size
        self.print_char = u"\u2587"  # Solid block
        self.tower_width = TerminalDisplay.wid(self.size)
        self.total_print_width = 3*self.tower_width+2
        debug(self.tower_width)
        self.printer = print

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


class CursesTerminalDisplay(TerminalDisplay):

    def __init__(self, hanoi_instance):
        super().__init__(hanoi_instance)
        # self.stdscr = curses.initscr()
        # curses.noecho()
        # curses.cbreak()
        # self.printer = self.stdscr.addstr


class Move:
    _source = None
    _destination = None
    _state = None

    def __init__(self, game_state, src_tower, dst_tower):
        self._state = game_state
        self._source = src_tower
        self._destination = dst_tower

    # Return new game state with move processed
    def execute(self, force_move=False):
        new_state = copy.deepcopy
        if not force_move:
            if not self._source.legal_move_to(self._destination):
                raise Exception('Invalid Move attempted')

        self._destination.append(self._source.pop())

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '({}->{})'.format(
            self._source.get_index(), self._destination.get_index())


def get_int_with_criteria(criteria_fn, prompt):
    while True:
        try:
            raw = input(prompt)
            val = int(raw)
            assert(criteria_fn(val))
            return val
        except Exception as e:
            print(e)
            print("Invalid Entry!")


class Player:

    def select_move(self, move_options, tower_states):
        pass


class HumanPlayer(Player):

    def select_move(self, move_options, tower_states):
        print('Chose a move option: ')
        for idx, move in enumerate(move_options):
            print('   {}) {}'.format(idx+1, move))

        move = get_int_with_criteria(
            lambda x: len(move_options) >= x and x > 0,
            'type a number and hit "Enter": ')
        return move_options[move-1]


class DFSPlayer(Player):
    def search_for_win(self, current_state, move_list):
        for move in current_state.get_valid_moves():
            move.execute()
            if current_state.check_for_win():
                move_list.append(move)
                return True

    def get_horizon(self, state, current_move_list):
        res = []
        for move in state.get_valid_moves():
            res.append(copy(current_move_list.append(move, ),
    def select_move(self, move_options, tower_states):
        move_list=[]
        search_state=copy.deepcopy(tower_states)
        self.search_for_win(tower_states, move_list)


class HanoiGameState:
    size=0
    towers=None

    def __init__(self, size):
        self.size=size
        self.reset()

    def reset(self):
        temp_towers=[]
        for idx in range(0, 3):
            temp_towers.append(Tower(self.size, index=idx, isFull=not(idx)))

        self.towers=tuple(temp_towers)
        print(self.towers)

    def get_valid_moves(self):
        valid_moves=[]
        for src_tower in self.towers:
            debug('tower {}'.format(src_tower.get_index()))
            for dst_tower in self.towers:
                if src_tower.legal_move_to(dst_tower):
                    debug('added')
                    valid_moves.append(Move(src_tower, dst_tower))
        return valid_moves

    def check_for_win(self):
        for tower in self.towers:
            if tower.is_full() and tower != self._initial_tower:
                return True
        return False


class Hanoi:

    game_state=None

    def __init__(self, size):
        self.size=size
        self.display=None
        self.move_history=[]
        self.player=None
        self._running=False
        self._turn_number=0
        self._initial_tower=None
        self.game_state=HanoiGameState(size)

    def execute_game_turn(self):
        self.show()
        moves=self.game_state.get_valid_moves()
        selected_move=self.player.select_move(moves, self.game_state)
        self.move_history.append(selected_move)
        selected_move.execute()
        if self.game_state.check_for_win():
            self.show()
            print('you won!')
            exit(0)

    def start(self):
        self._running=True
        while self._running:
            self.execute_game_turn()

    def add_player(self, player):
        self.player=player

    def add_display(self, displayer):
        self.displayer=displayer


#  def move(self, src, dest):
#       print("Moving from {} -> {}".format(src, dest))
#        self.towers[dest].append(self.towers[src].pop())

    def show(self):
        self.displayer.show()

    def show_raw(self):
        print('TowA: {}'.format(self.game_state.towers[0]))
        print('TowB: {}'.format(self.game_state.towers[1]))
        print('TowC: {}'.format(self.game_state.towers[2]))

    def reset(self):
        self.game_state.reset()


debug_enabled=False


def debug(*args, **kwargs):
    if debug_enabled:
        print('>> DEBUG: ', end="")
        print(*args, **kwargs, end="\n")


game=Hanoi(3)
game.add_display(TerminalDisplay(game))
game.add_player(HumanPlayer())
game.start()
# game.show_raw()


'''
size = 4
   #       #
  ###     ###
 #####   #####
####### #######
'''
