"""Restored three tilted rounded bells, each with three diagonal tentacles, in the original staggered group.
Before: The rejected jellyfish are flat mushrooms with two vertical stems, missing their tilt and three trailing tentacles.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c9bdc48d-a72f-41ce-9b7a-6a465d1111ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jellyfish-group-solo/20260929T031604Z-recovered-thuan-mac/reference/jellyfish group_c9bdc48d-a72f-41ce-9b7a-6a465d1111ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'jellyfish-group-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'jellyfish group')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)

    def build(self):

        # Three diagonally tilted bells; each owns a regular series of three tentacles.
        for i,(sx,sy,ex,ey,r) in enumerate(((9,8,23,16,8),(4,32,18,40,8),(28,25,44,33,9))):
            self.path(f'bell-{i}',(sx,sy),(ex,ey,r,r,True),(sx,sy),closed=True)
            for j in range(3):
                x=sx+2+5*j;y=sy+1+3*j
                self.add_line(f'tentacle-{i}-{j}',(x,y),(x-3,y+6))

