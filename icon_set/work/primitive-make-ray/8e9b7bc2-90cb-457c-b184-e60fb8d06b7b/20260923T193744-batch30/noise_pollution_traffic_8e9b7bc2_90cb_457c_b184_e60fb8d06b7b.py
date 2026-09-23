"""Two cars below lightning and noise zigzags.

Symbol plan: Two repeated car silhouettes; central lightning and mirrored side noise marks. HRECT_L ink extremes (2,6)-(46,42).
Construction: car-front: coherent rounded body and paired wheel placement.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8e9b7bc2-90cb-457c-b184-e60fb8d06b7b'
SOURCE_PATH = 'icon_set/work/todo-references/noise pollution traffic_8e9b7bc2-90cb-457c-b184-e60fb8d06b7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'noise-pollution-traffic'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('noise', 'pollution', 'traffic')

    def build(self):
        # Each car is a fresh repeated symbol, with roof and wheel lobes in one contour.
        for k,x in enumerate((4,28)):
            n=f'car-{k}'
            self.add_bezier(n,(x,34),((x,31),(x+2,31),(x+3,30)),((x+4,26),(x+5,26),(x+8,26)),((x+11,26),(x+12,26),(x+13,30)),((x+14,31),(x+16,31),(x+16,34)),((x+16,36),(x+16,37),(x+14,37)),((x+14,41),(x+10,41),(x+10,37)),((x+9,37),(x+7,37),(x+6,37)),((x+6,41),(x+2,41),(x+2,37)),((x,37),(x,36),(x,34)))
            self.add_contour(n+'-outline',n,closed=True)
        self.add_polyline('lightning',(26,8),(18,18),(25,18),(22,24),(31,14),(25,14),closed=True)
        self.add_polyline('noise-left',(4,17),(7,20),(10,16),(13,19))
        self.add_polyline('noise-right',(41,13),(38,16),(41,19),(38,22))

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

