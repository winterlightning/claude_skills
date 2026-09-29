"""Restored the extended lower-left handle, curved diagonal spine and four equally spaced comb teeth.
Before: The rejected comb has three large teeth attached to a short rounded spine; the long grip and finer tooth row disappear.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dafdca17-4d27-4cd9-935d-01a08f4e53e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handled-comb-on-diagonal/20260929T025914Z-thuan-mac/reference/hair dress comb_dafdca17-4d27-4cd9-935d-01a08f4e53e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handled-comb-on-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'hair dress comb')

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

        # Diagonal comb spine and extended rounded handle; one repeated tooth definition.
        self.path('spine',(44,16),(37,9),(30,9,5,5,False),(6,33),(5,40,5,5,False),(11,42,5,5,False),(16,37),(34,19))
        for i in range(4):
            x,y=34-5*i,19+5*i
            self.add_line(f'tooth-{i}',(x,y),(x+7,y+7))
            self.relate('connect','spine',f'tooth-{i}')

