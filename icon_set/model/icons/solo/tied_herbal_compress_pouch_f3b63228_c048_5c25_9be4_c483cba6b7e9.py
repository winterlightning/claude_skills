"""A round fabric pouch bulges beneath a narrow tied collar and a flared upright handle. Two short diagonal folds descend from the tie into the otherwise blank compress body.
Symbol plan: Mirrored fabric pouch with a flared handle, one tie line and two folds. Elliptical shoulders flow into a broad rounded bottom; remove the duplicate collar outline.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: droplet; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3b63228-c048-5c25-9be4-c483cba6b7e9'
SOURCE_PATH = 'pictographic-primitives/beauty/herbal compress_f3b63228-c048-5c25-9be4-c483cba6b7e9.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'tied-herbal-compress-pouch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('tied', 'herbal', 'compress', 'pouch')

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

        segments('handle',(18,16),(14,4),(34,4),(30,16))
        self.add_arc('shoulder-right',(30,16),(40,32),radius_x=10,radius_y=16)
        self.add_arc('bottom',(40,32),(8,32),radius_x=16,radius_y=12)
        self.add_arc('shoulder-left',(8,32),(18,16),radius_x=10,radius_y=16)
        self.add_contour('pouch','handle-1','handle-2','handle-3','shoulder-right','bottom','shoulder-left',closed=True)
        self.add_line('tie',(18,16),(30,16));self.relate('connect','tie','pouch')
        for n,a,b in [('left',(18,16),(20,24)),('right',(30,16),(28,24))]:
         self.add_line(n+'-fold',a,b);self.relate('connect',n+'-fold','pouch');self.relate('connect',n+'-fold','tie')
