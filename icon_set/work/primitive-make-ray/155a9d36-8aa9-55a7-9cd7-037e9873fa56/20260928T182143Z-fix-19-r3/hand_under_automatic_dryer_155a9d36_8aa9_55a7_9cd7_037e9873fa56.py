"""Restored the wall-dryer housing, two curved airflow streams, and an open cupped hand.
Before: The rejected dryer removes every airflow stroke, so the upper object reads as a lid over an abstract hand.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '155a9d36-8aa9-55a7-9cd7-037e9873fa56'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-under-automatic-dryer/20260928T182143Z-thuan-mac/reference/automatic hand dryer_155a9d36-8aa9-55a7-9cd7-037e9873fa56.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-under-automatic-dryer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'automatic hand dryer')

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

        # Dryer with two repeated curved airflow strokes, above a cupped hand.
        self.path('dryer',(8,14),(8,12),(14,6,6,6,True),(34,6),(40,12,6,6,True),(40,14),(8,14),closed=True)
        for i,x in enumerate((19,29)):
            self.path(f'air-{i}',(x,20),(x-1,23,3,3,False),(x,26,3,3,True))
        self.path('thumb',(6,36),(13,32),(24,32),(24,38,3,3,True),(18,38))
        self.path('palm',(6,44),(14,42),(25,44),(31,42,10,10,False),(41,34),(37,30,3,3,False),(27,37))

