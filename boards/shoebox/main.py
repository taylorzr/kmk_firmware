print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP0,board.GP1,board.GP2,board.GP3)

keyboard.col_pins = (
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(ModTap())
keyboard.modules.append(Layers())

keyboard.tap_time = 200

_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    # QWERTY
    [
        KC.EQL,                KC.Q,    KC.W,    KC.E,    KC.R,                  KC.T,                   KC.Y,            KC.U, KC.I,    KC.O,   KC.P,    KC.MINS,\
        KC.MT(KC.TAB,KC.LCTL), KC.A,    KC.S,    KC.D,    KC.F,                  KC.G,                   KC.H,            KC.J, KC.K,    KC.L,   KC.SCLN, KC.QUOT,\
        KC.MT(KC.GRV,KC.LSFT), KC.Z,    KC.X,    KC.C,    KC.V,                  KC.B,                   KC.N,            KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.MT(KC.BSLS,KC.RSFT),\
        XXXXXXX,               XXXXXXX, XXXXXXX, XXXXXXX, KC.MT(KC.ESC,KC.LALT), KC.MT(KC.BSPC,KC.LGUI), KC.LT(1,KC.SPC), KC.LT(2,KC.ENT),
    ],
    # LOWER
    [
        _______, KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   _______, \
        _______, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, _______, \
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, \
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, _______, KC.BSPC, _______, _______,
    ],
    # RAISE
    [
        _______, _______, _______, KC.LCBR, KC.RCBR, _______, KC.MEDIA_PLAY_PAUSE, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.MEDIA_NEXT_TRACK, _______, _______, \
        _______, _______, _______, KC.LBRC, KC.RBRC, _______, KC.LEFT,             KC.DOWN,           KC.UP,           KC.RIGHT,            _______, _______, \
        _______, _______, _______, _______, _______, _______, _______,             _______,           _______,         _______,             _______, _______, \
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, _______, KC.BSPC, _______,             _______,
    ],
]

if __name__ == '__main__':
    keyboard.go()
