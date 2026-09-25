"""Lucide user-round and printer principles: capped circular head, curved shoulders and left terminal. Counter scene is intrinsic, not a modifier. Tiny display and apron detail omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c04a8c07-594d-4376-a9db-0a306f9604ae'
SOURCE_PATH = 'pictographic-primitives/shopping/shop barista_c04a8c07-594d-4376-a9db-0a306f9604ae.svg'
AUTHOR = 'gpt-6'

class BaristaAtCashRegister(Solo48):
    icon_id = 'barista-at-cash-register'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    aliases = ()
    keywords = ('barista', 'register', 'counter', 'cap', 'apron', 'cafe', 'worker')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Worker on the right, terminal left.
        self.add_arc('cap',(25,13),(39,13),radius_x=7)
        self.add_arc('chin',(39,13),(25,13),radius_x=7)
        self.add_contour('head','cap','chin',closed=True)
        self.add_line('brim',(21,13),(39,13))
        self.relate('connect','brim','head')
        self.add_polyline('counter',(6,42),(6,38),(8,38),(20,38),(28,38),(40,38),(42,38),(42,42))
        self.add_polyline('register',(8,38),(8,27),(20,27),(20,38))
        self.relate('connect','register','counter')
        self.add_arc('worker',(28,38),(40,38),radius_x=6,radius_y=9)
        self.relate('connect','worker','counter')
