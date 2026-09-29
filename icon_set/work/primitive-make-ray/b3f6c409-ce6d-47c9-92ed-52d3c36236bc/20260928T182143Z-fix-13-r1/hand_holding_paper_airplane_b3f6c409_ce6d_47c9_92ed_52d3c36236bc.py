"""Restored a long horizontal paper-plane silhouette, diagonal fold, and pinching thumb with curled fingers.
Before: The rejected paper plane loses the long pointed nose and the hand becomes an angular block.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b3f6c409-ce6d-47c9-92ed-52d3c36236bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-paper-airplane/20260928T182143Z-thuan-mac/reference/origami_b3f6c409-ce6d-47c9-92ed-52d3c36236bc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-paper-airplane'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'origami')

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

        # Folded triangle points left; the thumb crosses in front of the lower fold.
        self.path('plane',(6,6),(42,10),(35,19),(6,6),closed=True)
        self.path('fold',(18,12),(35,19),(31,32))
        self.path('rear-fold',(12,12),(12,17,4,4,False),(23,27))
        self.path('thumb',(28,31),(26,23),(20,25,3,3,False),(22,35),(25,42))
        self.path('palm',(31,32),(32,42))
        self.path('fingers',(17,23),(13,23),(11,27,3,3,False),(16,31),(12,29),(10,32,3,3,False),(15,37),(19,42))
        self.relate('connect','plane','fold')

