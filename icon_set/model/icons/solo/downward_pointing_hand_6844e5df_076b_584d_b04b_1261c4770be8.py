"""Downward Pointing Hand.
Plan: Open wrist expands to a thumb and two folded knuckles; the long index finger descends to a round tip. Ink (6,2)-(42,46). Human references use simple rounded anatomy; no detached head.
Reference construction: pointer; hand; human_ref/user.svg and human_ref/full_body_ref.png.
Reduction: Merge three folded fingertips into two broad knuckles and omit short creases so the pointing index stays clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6844e5df-076b-584d-b04b-1261c4770be8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/hand pointer down_6844e5df-076b-584d-b04b-1261c4770be8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'downward-pointing-hand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('downward', 'pointing', 'hand')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_bezier('wrist-left',(16,4),((16,10),(8,12),(8,18)))
        self.add_line('thumb-left',(8,18),(8,26))
        self.add_arc('thumb',(8,26),(16,26),radius_x=4,sweep=False)
        self.add_line('index-left',(16,26),(16,40))
        self.add_arc('index-tip',(16,40),(24,40),radius_x=4,sweep=False)
        self.add_line('index-right',(24,40),(24,26))
        self.add_arc('knuckle-1',(24,26),(32,26),radius_x=4,sweep=False)
        self.add_arc('knuckle-2',(32,26),(40,26),radius_x=4,sweep=False)
        self.add_line('palm-right',(40,26),(40,18))
        self.add_bezier('wrist-right',(40,18),((40,10),(32,10),(32,4)))
        self.add_contour('hand','wrist-left','thumb-left','thumb','index-left','index-tip','index-right','knuckle-1','knuckle-2','palm-right','wrist-right')
