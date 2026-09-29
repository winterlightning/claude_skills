"""Restored the mountain peak, connected scalloped snowline and irregular dripping ink silhouette.
Before: The rejected logo replaces the mountain snowline with a detached caret and reduces the ink splash to one flat pedestal.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '284bd116-a688-437f-8349-e9b0799bf5bb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__inkscape-logo/20260929T031604Z-recovered-thuan-mac/reference/inkscape logo_284bd116-a688-437f-8349-e9b0799bf5bb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'inkscape-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'inkscape logo')

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

        self.path('outline',(6,24),(21,6),(27,6,4,4,True),(42,23),(41,27,3,3,True),(32,30),(32,34,3,3,False),(35,35),(34,39,3,3,True),(28,41),(28,44,2,2,True),(20,44),(19,40,3,3,True),(11,37),(11,33,3,3,True),(15,32),(15,28,3,3,False),(7,26),(6,24,2,2,True),closed=True)
        self.path('snow',(12,17),(20,18,5,5,False),(24,14),(28,18),(33,18,4,4,False),(36,19,3,3,False),(39,17))

