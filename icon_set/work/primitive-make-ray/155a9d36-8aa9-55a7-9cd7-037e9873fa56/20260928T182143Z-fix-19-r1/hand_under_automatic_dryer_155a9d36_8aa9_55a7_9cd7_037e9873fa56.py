"""Restored a wall dryer housing, two downward airflow marks, and a recognizable cupped hand.
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

        # Rounded upper dryer, repeated airflow series, open supporting palm.
        self.path('dryer',(8,17),(8,14),(16,6,8,8,True),(32,6),(40,14,8,8,True),(40,17),(8,17),closed=True)
        for i,x in enumerate((19,29)):
            self.add_line(f'air-{i}',(x,23),(x,26))

        self.path('thumb',(6,34),(13,30),(24,30),(24,36,3,3,True),(18,36))
        self.path('palm',(6,42),(14,40),(25,42),(31,40,10,10,False),(41,32),(37,28,3,3,False),(27,35))

