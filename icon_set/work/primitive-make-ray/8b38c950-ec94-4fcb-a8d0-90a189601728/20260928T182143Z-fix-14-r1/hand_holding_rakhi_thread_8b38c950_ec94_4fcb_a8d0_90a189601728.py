"""Restored the diagonal bracelet thread through a round medallion and a closed hand with rounded fingers.
Before: The rejected rakhi loses its diagonal thread and the hand reads as a bent arrow.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8b38c950-ec94-4fcb-a8d0-90a189601728'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-rakhi-thread/20260928T182143Z-thuan-mac/reference/raksha bandhan 1_8b38c950-ec94-4fcb-a8d0-90a189601728.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-rakhi-thread'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'raksha bandhan 1')

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

        # Circular rakhi on a diagonal thread; closed hand grasps the lower strand.
        self.circle('rakhi',34,14,6)
        self.add_line('thread-upper',(38,10),(42,6))
        self.add_line('thread-middle',(30,18),(24,24))
        self.add_line('thread-lower',(12,36),(6,42))
        self.path('hand',(13,37),(7,31),(7,25,5,5,True),(17,15),(22,20,4,4,True),(17,25),(21,22),(25,26,3,3,True),(22,29),(25,27),(29,31,3,3,True),(27,34),(29,32),(33,36,3,3,True),(26,42),(19,42),(13,37),closed=True)
        self.relate('connect','rakhi','thread-upper')
        self.relate('connect','rakhi','thread-middle')

