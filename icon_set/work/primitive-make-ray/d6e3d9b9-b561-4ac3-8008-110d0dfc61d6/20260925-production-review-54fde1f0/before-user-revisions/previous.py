"""A clipboard containing a dollar sign.

Symbol plan: Centered clip capsule attached to one rounded board contour. VRECT_L ink extremes (6,2)-(42,46).
Construction: clipboard-list: open board contour around the clip; dollar-sign: geometric S with an open diagonal waist.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e3d9b9-b561-4ac3-8008-110d0dfc61d6'
SOURCE_PATH = 'pictographic-primitives/other/note dollar sign_d6e3d9b9-b561-4ac3-8008-110d0dfc61d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'note-dollar-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('note', 'dollar', 'sign')

    def build(self):
        self.clipboard()
        self.add_polyline('dollar-top-bar',(28,22),(24,22),(22,22))
        self.add_arc('dollar-upper',(22,22),(20,24),radius_x=2,sweep=False)
        self.add_line('dollar-waist',(20,24),(28,32))
        self.add_arc('dollar-lower',(28,32),(26,34),radius_x=2)
        self.add_polyline('dollar-bottom-bar',(26,34),(24,34),(20,34))
        for a,b in [('dollar-top-bar','dollar-upper'),('dollar-upper','dollar-waist'),('dollar-waist','dollar-lower'),('dollar-lower','dollar-bottom-bar')]:self.relate('connect',a,b)
        self.add_line('dollar-top',(24,21),(24,22));self.relate('connect','dollar-top','dollar-top-bar')
        self.add_line('dollar-bottom',(24,34),(24,35));self.relate('connect','dollar-bottom','dollar-bottom-bar')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-upper', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-lower', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-upper', name+'-lower', closed=True)

    def box(self, name, x, y, right, bottom, r=4):
        # A single radius owns all four tangent corners.
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),
             (right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            n=f'{name}-{i}'; a=pts[i]; b=pts[(i+1)%8]
            if a == b:
                continue
            if i%2:
                self.add_arc(n,a,b,radius_x=r)
            else:
                self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def clipboard(self):
        # Clip capsule and open board share the two lateral attachment nodes.
        self.box('clip',16,4,32,12,4)
        self.add_line('board-top-right',(32,8),(36,8))
        self.add_arc('board-tr',(36,8),(40,12),radius_x=4)
        self.add_line('board-right',(40,12),(40,40))
        self.add_arc('board-br',(40,40),(36,44),radius_x=4)
        self.add_line('board-bottom',(36,44),(12,44))
        self.add_arc('board-bl',(12,44),(8,40),radius_x=4)
        self.add_line('board-left',(8,40),(8,12))
        self.add_arc('board-tl',(8,12),(12,8),radius_x=4)
        self.add_line('board-top-left',(12,8),(16,8))
        self.add_contour('board','board-top-right','board-tr','board-right','board-br','board-bottom','board-bl','board-left','board-tl','board-top-left')
        self.relate('connect','board','clip')

