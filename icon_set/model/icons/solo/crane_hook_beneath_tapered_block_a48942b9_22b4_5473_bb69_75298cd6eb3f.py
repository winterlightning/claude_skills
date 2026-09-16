"""A broad lifting hook hangs below a tapered rectangular mounting block. Its thick curved body bends right before curling upward-left to a pointed tip, leaving a large open throat.
Symbol plan: Tapered mounting block above a broad open J hook. Consecutive quarter arcs turn the shank smoothly into the lower bowl. Simplify the double-edged hook body to one stroke.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: no useful hook match. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a48942b9-22b4-5473-bb69-75298cd6eb3f'
SOURCE_PATH = 'pictographic-primitives/construction/hook_a48942b9-22b4-5473-bb69-75298cd6eb3f.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'crane-hook-beneath-tapered-block'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('crane', 'hook', 'beneath', 'tapered', 'block')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_polyline('block',(8,4),(40,4),(34,16),(24,16),(14,16),closed=True)
        self.add_line('shank',(24,16),(24,20))
        self.add_arc('neck',(24,20),(28,24),radius_x=4,sweep=False)
        self.add_arc('hook-right',(28,24),(40,36),radius_x=12)
        self.add_arc('hook-bottom',(40,36),(8,36),radius_x=16,radius_y=8)
        self.add_line('tip',(8,36),(8,30))
        self.add_contour('hook','shank','neck','hook-right','hook-bottom','tip');self.relate('connect','hook','block')
