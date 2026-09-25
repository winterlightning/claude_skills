"""Four Part Direction Pad.
Plan: Four identical inward-pointing pentagonal buttons rotate around an empty center. Ink (4,4)-(44,44).
Reference construction: gamepad-2.
Reduction: Shorten the four buttons equally to preserve the empty central cross.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fb707dc9-b478-5801-9493-b7c9d5a127a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/direction button_fb707dc9-b478-5801-9493-b7c9d5a127a5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'four-part-direction-pad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('four', 'part', 'direction', 'pad')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        base=[(-6,-18),(6,-18),(6,-12),(0,-8),(-6,-12)]
        for j in range(4):
         pts=[]
         for x,y in base:
          for _ in range(j):x,y=-y,x
          pts.append((24+x,24+y))
         self.add_polyline(f'button-{j}',*pts,closed=True)
