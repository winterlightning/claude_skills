"""Restored a clean side-profile head and separate fingers descending from a wrist onto the scalp.
Before: The rejected hand blends into a large hook at the side of the head and obscures the scalp massage gesture.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-scalp-17e8bc26/20260929T025914Z-thuan-mac/reference/massage head_17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-massaging-scalp-17e8bc26'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'massage head')

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

        # Side-profile head on left; hand descends from upper right onto the crown and temple.
        self.path('head',(18,44),(18,38),(14,38),(10,34,4,4,True),(10,30),(6,30),(10,22),(10,20),(21,12,12,12,True),(25,12))
        self.add_line('neck',(32,35),(32,44))
        self.path('hand',(25,4),(22,11),(29,12),(25,23),(30,26,3,3,False),(34,17))
        self.path('finger-two',(34,17),(31,27),(36,29,3,3,False),(39,20))
        self.path('hand-outside',(42,4),(39,13),(42,22),(39,30),(36,29))

