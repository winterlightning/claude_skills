"""Restored a hand gripping a broad brush, an even bristle row and a low foam cluster beneath.
Before: The rejected brush has only two thick bristles, a disconnected hand, and a detached cloud instead of cleaning foam.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ae7b2f22-759d-4da2-b10b-25f4390e7bda'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-scrubbing-with-brush/20260929T031604Z-recovered-thuan-mac/reference/hand brush bubble_ae7b2f22-759d-4da2-b10b-25f4390e7bda.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-scrubbing-with-brush'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'hand brush bubble')

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

        self.path('brush',(7,18),(41,18),(41,26,4,4,True),(7,26),(7,18,4,4,True),closed=True)
        self.path('arm-left',(8,4),(16,18))
        self.path('arm-right',(20,4),(26,10),(31,10),(37,16,6,6,True))
        self.path('thumb',(26,15),(31,20),(28,25,3,3,True))
        for i,x in enumerate((9,15,21,27,33,39)):
            self.add_line(f'bristle-{i}',(x,26),(x,31))
            self.relate('connect','brush',f'bristle-{i}')
        self.path('foam',(6,44),(10,40,4,4,True),(20,40),(26,38,4,4,True),(33,37,5,5,True),(40,41,5,5,True),(44,44,4,4,True),(6,44),closed=True)

