"""Redrew a broad flared axe blade, diagonal handle, rounded fist and thumb with two finger divisions.
Before: The rejected axe head is a small diamond and the hand reads as a zigzag rather than fingers wrapped around a handle.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '47659966-6bcc-4338-8851-46f26e9cca27'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-axe/20260928T182143Z-thuan-mac/reference/tools axe hold_47659966-6bcc-4338-8851-46f26e9cca27.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-axe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'tools axe hold')

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

        # Root: broad flared blade, diagonal handle, enclosing fist; repeated finger separators.
        self.path('blade',(27,6),(31,15,13,13,False),(42,23),(36,29,5,5,True),(28,22),(20,18),(27,6,15,15,True),closed=True)
        self.path('handle-top',(24,22),(20,26))
        self.path('handle-bottom',(13,35),(6,42),(11,44),(18,37))
        self.path('fist',(12,36),(7,31),(7,27,3,3,True),(15,19),(19,19,3,3,True),(28,28))
        self.path('thumb',(22,24),(29,29),(31,34,7,7,True),(29,39),(31,44))
        for i,(x,y) in enumerate(((10,25),(15,21))):
            self.add_line(f'finger-{i}',(x,y),(x+7,y+7))

