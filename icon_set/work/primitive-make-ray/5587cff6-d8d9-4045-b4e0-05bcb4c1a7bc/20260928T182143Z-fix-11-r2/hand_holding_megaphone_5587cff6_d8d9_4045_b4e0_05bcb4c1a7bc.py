"""Restored a tapered megaphone, distinct handle, thumb across the handle and curved lower palm.
Before: The rejected megaphone is a horn above a letter-D loop; the hand is not recognizable and the handle is lost.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape SQUARE; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5587cff6-d8d9-4045-b4e0-05bcb4c1a7bc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-megaphone/20260928T182143Z-thuan-mac/reference/labor megaphone_5587cff6-d8d9-4045-b4e0-05bcb4c1a7bc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-megaphone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'labor megaphone')

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

        # Horn flares right; separate handle and enclosing hand below its body.
        self.path('horn',(17,12),(28,11),(42,6),(42,28),(28,23),(17,22),(17,12),closed=True)
        self.path('rear',(17,12),(11,12),(6,17,5,5,False),(11,22,5,5,False),(17,22))
        self.path('handle-left',(17,22),(19,29))
        self.path('handle-right',(24,23),(26,29))
        self.path('thumb',(7,31),(15,29),(28,29),(28,35,3,3,True),(22,35))
        self.path('palm',(7,42),(14,41),(22,42),(27,38,5,5,False),(28,35))
        self.relate('connect','rear','horn')
        self.relate('connect','horn','handle-left')
        self.relate('connect','thumb','palm')

