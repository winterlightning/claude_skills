"""Magic Hat with Rabbit Ears.
Symbol plan: Rabbit ears emerge from top hat. VRECT_L (8,4)-(40,44), upright ears and crown. No useful exact Lucide match. Mirrored ears, smooth broad brim; omit inner ear strokes and hatband to keep openings legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ba78189-ea92-5ef8-9b2e-7139d60dc41e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/show rabbit hat_9ba78189-ea92-5ef8-9b2e-7139d60dc41e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-rabbit-ears-emerging-from-top-hat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('magic', 'hat', 'with', 'rabbit', 'ears')

    def build(self):
        self.add_bezier('left-ear',(14,22),((8,10),(8,4),(12,4)),((18,4),(20,14),(20,22)))
        self.add_bezier('right-ear',(28,22),((28,14),(30,4),(36,4)),((40,4),(40,10),(34,22)))
        self.add_polyline('brim-top',(8,22),(14,22),(20,22),(28,22),(34,22),(40,22))
        self.add_bezier('brim-right',(40,22),((40,26),(38,30),(36,30)))
        self.add_line('brim-bottom',(36,30),(12,30))
        self.add_bezier('brim-left',(12,30),((10,30),(8,26),(8,22)))
        self.contours=[c for c in self.contours if c.contour_id!='brim-top']
        self.add_contour('brim',*[f'brim-top-{i}' for i in range(1,6)],'brim-right','brim-bottom','brim-left',closed=True)
        self.relate('connect','left-ear','brim');self.relate('connect','right-ear','brim')
        self.add_bezier('crown',(12,30),((12,35),(10,44),(24,44)),((38,44),(36,35),(36,30)))
        self.relate('connect','crown','brim')

    def rounded(self, name, l, t, r, b, radius, nodes=()):
        # One radius owns all tangent corners; split straight walls at real joins.
        pts=[(l+radius,t),(r-radius,t),(r,t+radius),(r,b-radius),
             (r-radius,b),(l+radius,b),(l,b-radius),(l,t+radius)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; part=f"{name}-{i}"
            if i%2:
                self.add_arc(part,a,z,radius_x=radius)
                members.append(part)
            else:
                on=[p for p in nodes if p!=a and p!=z and
                    (z[0]-a[0])*(p[1]-a[1])==(z[1]-a[1])*(p[0]-a[0]) and
                    min(a[0],z[0])<=p[0]<=max(a[0],z[0]) and min(a[1],z[1])<=p[1]<=max(a[1],z[1])]
                on.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                path=[a,*on,z]
                for j,(v,w) in enumerate(zip(path,path[1:])):
                    if v==w: continue
                    member=f"{part}-{j}";self.add_line(member,v,w);members.append(member)
        self.add_contour(name,*members,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
