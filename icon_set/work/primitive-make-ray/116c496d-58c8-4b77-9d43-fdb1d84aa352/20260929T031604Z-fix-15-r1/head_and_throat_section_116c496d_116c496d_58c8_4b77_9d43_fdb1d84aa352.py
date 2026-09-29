"""Restored the rounded skull and nose profile, horizontal mouth cavity and curved inner throat channels.
Before: The rejected head is a squared pipe shape with three parallel stubs, obscuring the skull, oral opening and throat section.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '116c496d-58c8-4b77-9d43-fdb1d84aa352'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-and-throat-section-116c496d/20260929T031604Z-recovered-thuan-mac/reference/throat problem_116c496d-58c8-4b77-9d43-fdb1d84aa352.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'head-and-throat-section-116c496d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'throat problem')

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

        self.path('head',(36,44),(36,36),(40,25,18,18,False),(40,19),(25,4,15,15,False),(10,17,15,15,False),(10,19),(6,27),(10,28),(10,31),(20,31),(27,38,7,7,True),(27,44))
        self.path('throat',(11,36),(19,36),(22,39,3,3,True),(22,44))
        self.path('jaw-section',(11,36),(11,39),(17,39),(17,44))

