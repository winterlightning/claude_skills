"""Magic Wand and Top Hat.
Symbol plan: Diagonal magic wand enters top hat opening. SQUARE (6,6)-(42,42). No useful exact Lucide match. Preserve asymmetrical wand and two effect rays with symmetric hat; omit hatband.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5332a6af-13c4-402e-b7bc-16e1107c5b0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/show hat magician_5332a6af-13c4-402e-b7bc-16e1107c5b0f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slanted-magic-wand-entering-open-top-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    categories = ("entertainment", "primitives")
    aliases = ()
    keywords = ('magic', 'wand', 'and', 'top', 'hat')

    def build(self):
        self.add_bezier('brim-left',(14,20),((6,20),(6,23),(6,25)),((6,28),(8,30),(12,30)))
        self.add_line('brim-bottom',(12,30),(36,30))
        self.add_bezier('brim-right',(36,30),((40,30),(42,28),(42,25)),((42,23),(42,20),(40,20)))
        self.add_contour('brim','brim-left','brim-bottom','brim-right')
        self.add_line('body-left',(12,30),(12,36))
        self.add_arc('bottom-left',(12,36),(18,42),radius_x=6,sweep=False)
        self.add_line('bottom',(18,42),(30,42))
        self.add_arc('bottom-right',(30,42),(36,36),radius_x=6,sweep=False)
        self.add_line('body-right',(36,36),(36,30))
        self.add_contour('crown','body-left','bottom-left','bottom','bottom-right','body-right')
        self.relate('connect','crown','brim')

        self.add_line('wand',(24,21),(42,6))
        self.add_line('ray-left',(6,10),(10,10));self.add_line('ray-top',(20,6),(20,9))

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
