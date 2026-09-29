"""Restored a broad curved brim, dipped crown, circular jaw and long curved hair on both sides.
Before: The rejected cowboy avatar uses a polygonal hat and squared hair, losing the curved brim, rounded face and flowing hair.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8e5f188b-2874-56f0-8538-ccc3b48f76fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hat-lady-cowboy-avatar/20260929T031604Z-recovered-thuan-mac/reference/hat lady cowboy_8e5f188b-2874-56f0-8538-ccc3b48f76fc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hat-lady-cowboy-avatar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'hat lady cowboy')

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

        self.path('brim',(6,16),(42,16,18,4,False),(42,22,3,3,True),(6,22,18,6,True),(6,16,3,3,True),closed=True)
        self.path('crown',(13,17),(16,7),(20,5,4,4,True),(24,7),(28,5),(32,7,4,4,True),(35,17))
        self.path('jaw',(14,27),(14,29),(34,29,10,10,False),(34,27))
        self.path('hair-left',(12,27),(8,37),(12,44,6,6,False))
        self.path('hair-right',(36,27),(40,37),(36,44,6,6,True))

