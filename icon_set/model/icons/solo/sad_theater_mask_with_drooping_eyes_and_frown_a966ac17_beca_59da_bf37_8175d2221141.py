"""Sad Tragedy Theater Mask.
Symbol plan: Sad theater mask with downcast eyes and frown. SQUARE (6,6)-(42,42) fits the broad face. Lucide drama informs curved mask silhouette and spare facial strokes. Mirror outline and eyes; mouth is a circular frown and upper rim gently dips.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a966ac17-beca-59da-bf37-8175d2221141'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/show theater mask sad_a966ac17-beca-59da-bf37-8175d2221141.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sad-theater-mask-with-drooping-eyes-and-frown'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('sad', 'tragedy', 'theater', 'mask')

    def build(self):
        self.add_bezier('rim',(6,6),((16,9),(32,9),(42,6)))
        self.add_line('right',(42,6),(42,22))
        self.add_bezier('chin-right',(42,22),((42,32),(32,42),(24,42)))
        self.add_bezier('chin-left',(24,42),((16,42),(6,32),(6,22)))
        self.add_line('left',(6,22),(6,6));self.add_contour('mask','rim','right','chin-right','chin-left','left',closed=True)
        self.add_line('eye-left',(16,20),(19,18));self.add_line('eye-right',(29,18),(32,20))
        self.add_arc('frown',(20,32),(28,32),radius_x=4)

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
