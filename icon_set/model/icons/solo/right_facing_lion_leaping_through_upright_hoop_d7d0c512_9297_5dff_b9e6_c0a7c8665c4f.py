"""Lion Jumping Through Hoop.
Symbol plan: Lion leaps right through an upright hoop. SQUARE (6,6)-(42,42) spans hoop, mane and extended foreleg. No useful exact Lucide lion match. Keep pointed mane, protruding muzzle, hoop and one extended foreleg; omit eye and second parallel foreleg. Reduce mane to two clear points. Shared occlusion endpoints, smooth hoop and rounded paw; directional asymmetry preserves action.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7d0c512-9297-5dff-b9e6-c0a7c8665c4f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/circus lion ring_d7d0c512-9297-5dff-b9e6-c0a7c8665c4f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-facing-lion-leaping-through-upright-hoop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('lion', 'jumping', 'through', 'hoop')

    def build(self):
        self.add_bezier('hoop',(28,6),((14,6),(6,14),(6,24)),((6,34),(10,40),(16,40)),((20,40),(23,36),(24,32)))
        self.add_line('stand',(16,40),(16,42));self.relate('connect','stand','hoop')
        self.add_polyline('mane',(24,32),(14,18),(26,18),(28,6))
        self.add_bezier('forehead',(28,6),((34,10),(36,10),(36,16)))
        self.add_polyline('muzzle',(36,16),(42,20),(40,26),(32,26),(42,30),(42,34))
        self.add_arc('paw',(42,34),(38,38),radius_x=4)
        self.add_bezier('leg',(38,38),((32,38),(28,34),(24,32)))
        self.contours.clear()
        self.add_contour('lion',*[f'mane-{i}' for i in range(1,4)],'forehead',*[f'muzzle-{i}' for i in range(1,6)],'paw','leg',closed=True)
        self.relate('connect','lion','hoop')

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
