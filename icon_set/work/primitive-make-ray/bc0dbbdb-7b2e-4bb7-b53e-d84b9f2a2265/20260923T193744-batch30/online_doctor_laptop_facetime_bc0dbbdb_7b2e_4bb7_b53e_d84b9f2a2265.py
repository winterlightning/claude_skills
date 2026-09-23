"""A doctor portrait with a medical cross behind a laptop.

Symbol plan: Circular head with exact detached gap, smooth shoulder silhouette, cross and left-front laptop. SQUARE ink extremes (4,4)-(44,44).
Construction: laptop: screen and flared base; shared human reference owns doctor bust.
Human construction: icon_set/references/human_ref/user.svg: head center(32,12), radius6, lower head18, shoulder top26; exact 8-unit centerline /4-unit ink gap. Circular head and broad smooth shoulders retained; scene crowding checked separately.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265'
SOURCE_PATH = 'icon_set/work/todo-references/online doctor laptop facetime_bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'online-doctor-laptop-facetime'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('online', 'doctor', 'laptop', 'facetime')

    def build(self):
        self.circle('head',32,12,6)
        self.add_bezier('shoulders',(20,34),((20,29),(26,26),(32,26)),((38,26),(42,30),(42,36)))
        self.add_polyline('laptop-screen',(6,34),(6,26),(14,26))
        self.add_polyline('laptop-base',(6,34),(20,34),(26,34),(30,42),(6,42),closed=True)
        self.relate('connect','shoulders','laptop-base')
        self.relate('connect','laptop-screen','laptop-base')
        for n,a,b in [('cross-up',(32,28),(32,32)),('cross-down',(32,32),(32,36)),('cross-left',(28,32),(32,32)),('cross-right',(32,32),(36,32))]:
            self.add_line(n,a,b)
        parts=['cross-up','cross-down','cross-left','cross-right']
        for i,a in enumerate(parts):
            for b in parts[:i]: self.relate('connect',a,b)

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

