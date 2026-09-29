"""Restored a pinching hand, a diagonal string, a complete yo-yo with central axle, and two motion arcs.
Before: The rejected yo-yo has a broken second circle and a thick connector, losing the thin string and spinning motion.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '28a605e6-a545-47ed-ae21-f45557bb8374'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-playing-yoyo/20260929T025914Z-thuan-mac/reference/playing yoyo_28a605e6-a545-47ed-ae21-f45557bb8374.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-playing-yoyo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'playing yoyo')

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

        # Pinching hand above a hanging yo-yo; twin arcs indicate swinging/spinning motion.
        self.path('hand-top',(42,6),(31,6),(20,10),(11,10),(6,14,4,4,False),(10,20,4,4,False),(17,15),(25,17))
        self.path('hand-bottom',(18,17),(27,21),(35,18),(42,14))
        self.add_line('string',(16,16),(24,29))
        self.circle('yoyo',32,35,9)
        self.circle('axle',32,35,2)
        self.path('motion-outer',(8,28),(8,43,12,12,False))
        self.path('motion-inner',(14,31),(14,40,8,8,False))

