"""Made a broad split fountain nib, horizontal pen shaft, stepped rounded knuckles and a visible curled thumb.
Before: The rejected nib looks like an arrow; three identical tall loops obscure the fist and omit the thumb.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '83ff3171-53c2-4300-a683-6306ba8fe250'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-fountain-pen/20260928T182143Z-thuan-mac/reference/workflow coaching hand pen_83ff3171-53c2-4300-a683-6306ba8fe250.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-fountain-pen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'workflow coaching hand pen')

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

        # Pen passes behind upright gripping fingers; knuckles share one step/radius scheme.
        self.path('nib',(20,13),(13,10),(6,16),(13,22),(20,19))
        self.add_line('nib-slit',(6,16),(12,16))
        self.relate('connect','nib','nib-slit')
        self.add_line('pen-tail',(38,16),(42,16))
        self.path('fingers',(20,23),(20,12),(26,12,3,3,True),(26,9),(32,9,3,3,True),(32,11),(38,11,3,3,True),(38,30),(34,37,9,9,True),(34,42))
        self.path('thumb',(26,21),(20,21),(17,24,3,3,False),(17,29),(21,35,8,8,False),(23,38),(23,42))
        self.path('thumb-fold',(20,29),(24,27,4,4,False),(26,23,4,4,False),(26,21))
        self.add_line('finger-a',(26,12),(26,18))
        self.add_line('finger-b',(32,11),(32,19))
        self.relate('connect','finger-a','fingers')
        self.relate('connect','finger-b','fingers')

