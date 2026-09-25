"""Circus Tent with Flag.
Symbol plan: Flagged circus tent, mirrored roof and arched entrance. VRECT_L (8,4)-(40,44) gives the flag vertical room. Lucide tent informs structural symmetry. Omit horizontal roof seam to open doorway space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0c79a19-860e-53f0-8e36-6f3d654ca652'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/circus tent_f0c79a19-860e-53f0-8e36-6f3d654ca652.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circus-tent-with-triangular-peak-flag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('circus', 'tent', 'with', 'flag')

    def build(self):
        self.add_polyline('flag',(24,4),(40,12),(24,20),closed=True)
        self.add_line('mast',(24,20),(24,24));self.relate('connect','flag','mast')
        self.add_bezier('roof-left',(8,32),((14,31),(20,27),(24,24)))
        self.add_bezier('roof-right',(24,24),((28,27),(34,31),(40,32)))
        self.add_polyline('right-wall',(40,32),(40,44),(30,44),(30,42))
        self.add_arc('door-right',(30,42),(24,36),radius_x=6,sweep=False)
        self.add_arc('door-left',(24,36),(18,42),radius_x=6,sweep=False)
        self.add_polyline('left-wall',(18,42),(18,44),(8,44),(8,32))
        self.contours=[c for c in self.contours if c.contour_id=='flag']
        self.add_contour('tent','roof-left','roof-right',*[f'right-wall-{i}' for i in range(1,4)],'door-right','door-left',*[f'left-wall-{i}' for i in range(1,4)],closed=True)
        self.relate('connect','mast','tent')

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
