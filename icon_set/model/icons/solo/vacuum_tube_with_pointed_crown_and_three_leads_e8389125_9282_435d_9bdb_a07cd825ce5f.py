"""Electronic Vacuum Tube.
Symbol plan: Vacuum tube, pointed crown, transverse base and three leads. Retain a two-rail internal ladder with one rung. VRECT_M extremes (10,4)-(38,44). Lucide plug informs lead attachments.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8389125-9282-435d-9bdb-a07cd825ce5f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/vacuum tube_e8389125-9282-435d-9bdb-a07cd825ce5f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vacuum-tube-with-pointed-crown-and-three-leads'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/electronics"
    aliases = ()
    keywords = ('electronic', 'vacuum', 'tube')

    def build(self):
        self.add_line('crown-1',(10,20),(10,18))
        self.add_arc('crown-2',(10,18),(18,10),radius_x=8)
        self.add_line('crown-3',(18,10),(20,10))
        self.add_line('crown-4',(20,10),(24,4))
        self.add_line('crown-5',(24,4),(28,10))
        self.add_line('crown-6',(28,10),(30,10))
        self.add_arc('crown-7',(30,10),(38,18),radius_x=8)
        self.add_line('crown-8',(38,18),(38,20))
        self.add_line('right',(38,20),(38,30));self.add_arc('br',(38,30),(32,36),radius_x=6)
        self.add_polyline('base',(32,36),(28,36),(24,36),(20,36),(16,36))
        self.add_arc('bl',(16,36),(10,30),radius_x=6);self.add_line('left',(10,30),(10,20))
        self.contours.clear()  # Combine the two authored runs into the complete glass contour.
        self.add_contour('glass',*[f'crown-{i}' for i in range(1,9)],'right','br',*[f'base-{i}' for i in range(1,5)],'bl','left',closed=True)
        self.add_polyline('division',(10,20),(20,20),(28,20),(38,20));self.relate('connect','division','glass')
        for x in (20,28):
            self.add_polyline(f'electrode-{x}',(x,20),(x,28),(x,36))
            self.relate('connect',f'electrode-{x}','division')
            self.relate('connect',f'electrode-{x}','glass')
        self.add_line('rung',(20,28),(28,28))
        for x in (20,28): self.relate('connect','rung',f'electrode-{x}')
        for x in (16,24,32):
         self.add_line(f'lead-{x}',(x,36),(x,44));self.relate('connect',f'lead-{x}','glass')

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
