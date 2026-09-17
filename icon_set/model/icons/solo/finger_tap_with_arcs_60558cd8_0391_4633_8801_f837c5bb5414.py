"""Finger Tap with Arcs.
Plan: An open-ended upright fingertip sits below two concentric touch arcs with nine-unit radial spacing. Ink (6,2)-(42,46). Human reference: rounded minimal anatomy, no head/body pairing.
Reference construction: pointer; human_ref/user.svg and human_ref/full_body_ref.png.
Reduction: Omit the short crease inside the finger to preserve its narrow opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '60558cd8-0391-4633-8801-f837c5bb5414'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/gesture tap two fingers 1_60558cd8-0391-4633-8801-f837c5bb5414.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'finger-tap-with-arcs'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('finger', 'tap', 'with', 'arcs')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('outer-touch',(8,20),(40,20),radius_x=16)
        self.add_arc('inner-touch',(17,20),(31,20),radius_x=7)
        self.add_line('finger-left',(18,44),(18,35))
        self.add_arc('finger-tip',(18,35),(30,35),radius_x=6)
        self.add_line('finger-right',(30,35),(30,44))
        self.add_contour('finger','finger-left','finger-tip','finger-right')
