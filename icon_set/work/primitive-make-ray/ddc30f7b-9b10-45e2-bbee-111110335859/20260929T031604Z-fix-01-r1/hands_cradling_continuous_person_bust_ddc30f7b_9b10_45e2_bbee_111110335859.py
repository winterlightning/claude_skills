"""Restored the continuous head, neck and shoulders, and two cupped hands with separate thumbs and open wrists.
Before: The rejected bust is reduced to an omega-shaped head and the hands become closed loops; the reference has a continuous neck/shoulders and open wrists.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ddc30f7b-9b10-45e2-bbee-111110335859'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hands-cradling-continuous-person-bust/20260929T031604Z-recovered-thuan-mac/reference/donation charity care person male_ddc30f7b-9b10-45e2-bbee-111110335859.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-cradling-continuous-person-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'donation charity care person male')

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

        self.path('person',(14,26),(14,25),(20,22),(20,18),(18,12,9,9,True),(30,12,6,6,True),(28,18,9,9,True),(28,22),(34,25),(34,26))

        # Mirrored cupped hands with open wrists and a shared thumb attachment on each side.
        for side in (-1,1):
            x=lambda v:24+side*(24-v)
            self.path(f'hand-outer-{side}',(x(12),44),(x(12),40),(x(6),33),(x(6),24),(x(12),24,3,3,side==-1),(x(12),30),(x(17),35))
            self.path(f'hand-inner-{side}',(x(12),30),(x(16),29),(x(20),34,6,6,side==-1),(x(20),44))
            self.relate('connect',f'hand-outer-{side}',f'hand-inner-{side}')

