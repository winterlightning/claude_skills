"""Rebuilt the distinct striking face and swept claw, diagonal shaft and wrapping fingers with a thumb.
Before: The rejected claw hammer has a blocky diamond head and abstract zigzag grip.
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape VRECT_L; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9c2e6a00-c352-4f4c-97df-5e296d00637d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-holding-hammer/20260928T182143Z-thuan-mac/reference/tools hammer hold_9c2e6a00-c352-4f4c-97df-5e296d00637d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-holding-hammer'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', 'tools hammer hold')

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

        # Diagonal shaft and fist, transverse striking face with a hooked claw.
        self.path('face',(26,6),(34,14),(28,20),(20,12),(26,6),closed=True)
        self.path('claw',(34,14),(40,21),(42,30,12,12,True),(36,34),(36,27,12,12,False),(28,20))
        self.path('shaft',(25,23),(20,28))
        self.path('shaft-end',(13,35),(6,42),(11,44),(18,37))
        self.path('fist',(12,36),(7,31),(7,27,3,3,True),(15,19),(19,19,3,3,True),(28,28))
        self.path('thumb',(22,24),(29,29),(31,34,7,7,True),(29,39),(31,44))
        for i,(x,y) in enumerate(((10,25),(15,21))):
            self.add_line(f'finger-{i}',(x,y),(x+7,y+7))

