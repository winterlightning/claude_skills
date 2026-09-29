"""Restored a diagonal open-jaw wrench with a broad head and a rounded fist around its shaft.
Before: The rejected wrench is a small incomplete ring on a line, and the hand is an abstract zigzag.
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '80b7765d-72c2-4b01-b0bf-6a084aa9bc97'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wrench/20260929T025914Z-thuan-mac/reference/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-wrench'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'tools wrench hold')

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

        # Broad open jaw above a diagonal shaft and two-finger grip.
        self.path('wrench',(25,21),(25,14),(31,6,9,9,True),(40,4),(34,10),(38,14),(44,8),(44,17),(38,25,9,9,True),(31,25))
        self.add_line('shaft-top',(27,23),(21,29))
        self.add_line('shaft-bottom',(14,36),(6,44))
        self.path('fist',(15,39),(7,31),(7,27,3,3,True),(14,22),(18,22,3,3,True),(27,31))
        self.path('thumb',(24,28),(29,33),(29,39,6,6,True),(31,44))
        self.add_line('finger-seam',(10,26),(17,33))

