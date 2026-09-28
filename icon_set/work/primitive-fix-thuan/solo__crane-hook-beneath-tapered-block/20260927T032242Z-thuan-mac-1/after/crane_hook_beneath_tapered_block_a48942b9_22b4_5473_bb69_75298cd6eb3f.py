"""A broad lifting hook hangs below a tapered rectangular mounting block. Its thick curved body bends right before curling upward-left to a pointed tip, leaving a large open throat.
Symbol plan: Tapered mounting block above a broad open J hook. Consecutive quarter arcs turn the shank smoothly into the lower bowl. Simplify the double-edged hook body to one stroke.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: no useful hook match. Lucide original and atomic-debug renders inspected where named.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a48942b9-22b4-5473-bb69-75298cd6eb3f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crane-hook-beneath-tapered-block/20260927T032242Z-thuan-mac-1/reference/hook_a48942b9-22b4-5473-bb69-75298cd6eb3f.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'crane-hook-beneath-tapered-block'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    categories = ('construction', 'primitives')
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

        self.add_polyline('block',(12,4),(36,4),(30,16),(24,16),(18,16),closed=True)
        self.add_line('shank',(24,16),(24,20))
        self.add_bezier('neck',(24,20),((24,22),(26,24),(28,24)))
        self.add_arc('hook-right',(28,24),(40,36),radius_x=12)
        self.add_arc('hook-bottom',(40,36),(8,36),radius_x=16,radius_y=8)
        self.add_line('tip',(8,36),(8,30))
        self.add_contour('hook','shank','neck','hook-right','hook-bottom','tip');self.relate('connect','hook','block')
