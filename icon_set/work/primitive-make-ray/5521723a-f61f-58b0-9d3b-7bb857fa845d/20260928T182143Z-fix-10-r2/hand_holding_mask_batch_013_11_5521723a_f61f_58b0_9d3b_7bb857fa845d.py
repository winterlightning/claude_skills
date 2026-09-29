"""Restored the theatrical mask oval eye openings and lower-edge grip while preserving this icon’s ID.
Before: The rejected duplicate mask also uses hook eyes and an abstract lower-left pointer instead of a grip.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5521723a-f61f-58b0-9d3b-7bb857fa845d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-mask-batch-013-11/20260928T182143Z-thuan-mac/reference/cosplay_5521723a-f61f-58b0-9d3b-7bb857fa845d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-mask-batch-013-11'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'cosplay')

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

        # Mask contour has a shallow brow and rounded chin; hand occludes lower left.
        self.path('mask',(14,28),(14,9),(17,6,3,3,True),(27,8),(39,6),(42,9,3,3,True),(42,26),(35,35,10,10,True),(29,36))
        for side,x in enumerate((22,34)):
            self.path(f'eye-{side}',(x-4,19),(x+4,19,4,3,True),(x-4,19,4,3,True),closed=True)
        self.path('hand',(6,42),(8,30),(13,27),(28,27),(29,33,3,3,True),(20,35))
        self.path('lower-fingers',(27,34),(28,39,3,3,True),(21,42),(14,42))

