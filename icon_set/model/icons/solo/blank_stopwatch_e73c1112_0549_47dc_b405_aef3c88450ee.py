"""Blank Stopwatch.
Plan: Blank circular face radius15 at (23,29); plunger and right button attach at exact circle points. Ink (6,2)-(42,46).
Reference construction: timer.
Reduction: Omit the secondary button cap. Shift the circular body one unit left to balance the button.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e73c1112-0549-47dc-b405-aef3c88450ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/stopwatch_e73c1112-0549-47dc-b405-aef3c88450ee.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'blank-stopwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    aliases = ()
    keywords = ('blank', 'stopwatch')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        pts=[(23,14),(32,17),(38,29),(23,44),(8,29),(23,14)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'face-{j}',a,b,radius_x=15)
        self.add_contour('face',*(f'face-{j}' for j in range(5)),closed=True)
        self.add_line('plunger',(23,4),(23,14))
        self.add_polyline('cap',(17,4),(23,4),(29,4))
        self.relate('connect','plunger','cap')
        self.relate('connect','plunger','face')
        self.add_line('side-button',(32,17),(40,9))
        self.relate('connect','side-button','face')
