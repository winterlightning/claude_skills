"""Hand Holding Paper Airplane.

Plan: Triangular plane above a rounded gripping hand. Fold meets the thumb; reduce individual fingers. Bounds (6,6)-(42,42). Human reference: user.svg and full_body_ref.png; Lucide hand-grab informs the grip.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3f6c409-ce6d-47c9-92ed-52d3c36236bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/origami_b3f6c409-ce6d-47c9-92ed-52d3c36236bc.svg'
AUTHOR = 'gpt-6'

class HandHoldingPaperAirplane(Solo48):
    icon_id = 'hand-holding-paper-airplane'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hobbies"
    aliases = ()
    keywords = ('hand', 'holding', 'paper', 'airplane')

    def build(self):
        self.add_polyline('plane',(6,6),(42,6),(34,24),(24,24),(20,24),closed=True)
        self.add_polyline('fold',(42,6),(24,16),(24,24));self.relate('connect','plane','fold')
        self.add_line('thumb',(24,24),(24,34));self.relate('connect','plane','thumb')
        self.add_line('hand-right',(34,24),(38,42));self.relate('connect','plane','hand-right')
        self.add_polyline('wrist',(14,42),(6,34),(6,32))
        self.add_arc('fingers',(6,32),(14,24),radius_x=8)
        self.add_line('finger-top',(14,24),(20,24))
        self.add_contour('hand','wrist-1','wrist-2','fingers','finger-top')
        self.contours=[c for c in self.contours if c.contour_id!='wrist']
        self.relate('connect','hand','plane')
