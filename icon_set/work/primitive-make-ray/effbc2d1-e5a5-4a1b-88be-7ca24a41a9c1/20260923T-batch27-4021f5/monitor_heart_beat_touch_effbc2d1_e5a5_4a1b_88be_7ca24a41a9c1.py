"""monitor heart beat touch, complete SOLO48 composition.
Symbol plan in build(); visible keyshape extremes (6, 2, 42, 46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1'
SOURCE_PATH = 'icon_set/work/todo-references/monitor heart beat touch_effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-heart-beat-touch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('monitor heart beat touch',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)

    def rounded(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def monitor(self):
        # Symmetric rounded screen, split bottom edge at actual stand attachment.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        self.add_line('bottom-right',(38,34),(24,34))
        self.add_line('bottom-left',(24,34),(10,34))
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('screen','top','tr','right','br','bottom-right','bottom-left','bl','left','tl',closed=True)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','foot')

    def banknote(self):
        self.add_polyline('note',(4,8),(44,8),(44,40),(4,40),closed=True)
        # Paired eight-unit corner quadrants meet the note edges.
        arcs=[((12,8),(4,16)),((44,16),(36,8)),((4,32),(12,40)),((36,40),(44,32))]
        for i,(a,b) in enumerate(arcs):
            self.add_arc('corner-'+str(i),a,b,radius_x=8)
            self.relate('connect','note','corner-'+str(i))

    def build(self):
        # Shared human guidance: hand only, no detached head/body construction.
        # Sensor outline is interrupted where the touching finger occludes its bottom.
        self.add_line('sensor-left',(10,25),(10,14))
        self.add_arc('sensor-top',(10,14),(30,14),radius_x=10)
        self.add_line('sensor-right',(30,14),(30,25))
        self.add_arc('sensor-br',(30,25),(25,30),radius_x=5)
        self.add_line('sensor-bottom-right',(25,30),(24,30))
        self.add_arc('sensor-bl',(15,30),(10,25),radius_x=5)
        self.add_line('sensor-bottom-left',(18,30),(15,30))
        self.add_contour('sensor','sensor-bottom-left','sensor-bl','sensor-left','sensor-top','sensor-right','sensor-br','sensor-bottom-right')
        self.add_polyline('pulse',(10,17),(15,17),(18,12),(22,22),(25,17),(30,17))
        self.relate('connect','sensor','pulse')
        self.add_line('thumb-1',(16, 44),(8, 36))
        self.add_line('thumb-2',(8, 36),(8, 34))
        self.add_line('thumb-3',(8, 34),(11, 33))
        self.add_line('thumb-4',(11, 33),(18, 40))
        self.add_line('thumb-5',(18, 40),(18, 30))
        self.add_line('thumb-6',(18, 30),(18, 25))
        self.add_arc('finger-tip',(18,25),(24,25),radius_x=3)
        self.add_line('finger',(24,25),(24,34))
        self.add_line('hand-top',(24,34),(34,34))
        self.add_arc('hand-corner',(34,34),(40,40),radius_x=6)
        self.add_line('hand-right',(40,40),(40,44))
        self.add_contour('hand','thumb-1','thumb-2','thumb-3','thumb-4','thumb-5','thumb-6','finger-tip','finger','hand-top','hand-corner','hand-right')
        self.relate('connect','sensor','hand')
