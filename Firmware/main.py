import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.rgb import RGB
from kmk.modules.encoder import EncoderHandler
from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.row_pins = (board.D5, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.LCTL(KC.S),       # save stuff
        KC.LCTL(KC.Z),       # undo 
        KC.LCTL(KC.Y),       # redo
        KC.LCTL(KC.P),       # file search
        KC.LCTL(KC.Q),       # quick switch
        KC.LCTL(KC.R),       # switch projects
        KC.LCTL(KC.GRAVE),   # Terminal
        KC.LCTL(KC.LSFT(KC.M)), # problems panel
        KC.LCTL(KC.LSFT(KC.P)), # command palette
        KC.LCTL(KC.J),       # toggle panel
    ]
]

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = ((board.D7, board.D8, board.D9),)
encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)       
]

if __name__ == '__main__':
    keyboard.go()
