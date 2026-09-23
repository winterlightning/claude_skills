"""Immersive virtual-reality goggles with side straps and a central cross.
SOLO48 HRECT_M; geometry authored independently from the rendered reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a58cb8f2-5a25-594d-a031-72828d14122f'
SOURCE_PATH = 'icon_set/work/todo-references/game immersive vr_a58cb8f2-5a25-594d-a031-72828d14122f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'game-immersive-vr'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/gaming'
    aliases = ()
    keywords = ('game', 'immersive', 'vr')

    def line(self, n, a, b):
        self.add_line(n,a,b)

    def arc(self,n,a,b,rx,ry=None,sweep=True):
        self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)

    def rect(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.arc(f"{n}-{i}",a,b,r)
            else:self.line(f"{n}-{i}",a,b)
        self.add_contour(n,*(f"{n}-{i}" for i in range(8)),closed=True)

    def build(self):
        # Plan: symmetric visor, nose recess, equal side straps and centered cross.
        self.line('top',(18,10),(30,10))
        self.arc('tr',(30,10),(36,16),6)
        self.line('right',(36,16),(36,32))
        self.arc('br',(36,32),(30,38),6)
        nose=[(30,38),(27,38),(24,34),(21,38),(18,38)]
        for i in range(4):self.line(f'nose-{i+1}',nose[i],nose[i+1])
        self.arc('bl',(18,38),(12,32),6)
        self.line('left',(12,32),(12,16))
        self.arc('tl',(12,16),(18,10),6)
        self.add_contour('visor','top','tr','right','br',*[f'nose-{i}' for i in range(1,5)],'bl','left','tl',closed=True)
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            self.add_polyline('strap'+str(side),p(12,18),p(20,18),p(20,30),p(12,30))
            self.relate('connect','strap'+str(side),'visor')
        self.line('cross-a',(21,22),(27,26))
        self.line('cross-b',(21,26),(27,22))
        self.relate('connect','cross-a','cross-b')
