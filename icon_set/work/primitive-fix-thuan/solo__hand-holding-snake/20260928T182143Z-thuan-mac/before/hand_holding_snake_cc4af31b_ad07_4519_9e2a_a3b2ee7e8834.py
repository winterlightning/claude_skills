"""Hand Holding Snake.

Plan: Open palm under an S-curved snake with rounded head; reduce the dangling tail. Single snake stroke preserves the coil without cramped doubled walls. Bounds (6,6)-(42,42). Human reference user.svg and full_body_ref.png; Lucide hand-helping informs palm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc4af31b-ad07-4519-9e2a-a3b2ee7e8834'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/herping_cc4af31b-ad07-4519-9e2a-a3b2ee7e8834.svg'
AUTHOR = 'gpt-6'

class HandHoldingSnake(Solo48):
    icon_id = 'hand-holding-snake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('hand', 'holding', 'snake')

    def build(self):
        self.add_polyline('palm-top',(6,30),(16,30),(24,34),(36,24))
        self.add_arc('palm-tip',(36,24),(42,30),radius_x=6)
        self.add_polyline('palm-bottom',(42,30),(30,42),(6,42))
        self.add_contour('palm','palm-top-1','palm-top-2','palm-top-3','palm-tip','palm-bottom-1','palm-bottom-2')
        self.contours=[c for c in self.contours if c.contour_id not in ['palm-top','palm-bottom']]
        self.add_arc('snake-head',(32,12),(20,12),radius_x=6,sweep=False)
        self.add_arc('snake-neck',(20,12),(20,22),radius_x=5,sweep=False)
        self.add_arc('snake-body',(20,22),(16,30),radius_x=4,radius_y=8)
        self.add_contour('snake','snake-head','snake-neck','snake-body')
        self.relate('connect','snake','palm')
