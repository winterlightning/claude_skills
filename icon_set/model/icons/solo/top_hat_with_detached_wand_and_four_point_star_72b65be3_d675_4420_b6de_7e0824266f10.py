"""Magic Wand and Top Hat.
Symbol plan: Magic-trick scene with hat, four-point sparkle and detached wand. SQUARE (6,6)-(42,42) spans the scene. The user explicitly requests whole-scene generation for this listed draft; interpret the sparkle as a magic effect. No useful exact Lucide match. Preserve four-point star, interrupted brim, rounded tall crown and right-rising wand; omit hatband and shorten wand to maintain spacing. Intentional asymmetry follows the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72b65be3-d675-4420-b6de-7e0824266f10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/show hat magician_72b65be3-d675-4420-b6de-7e0824266f10.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'top-hat-with-detached-wand-and-four-point-star'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('magic', 'wand', 'and', 'top', 'hat')

    def build(self):
        self.add_bezier('brim-left',(6,24),((6,28),(8,30),(12,30)))
        self.add_line('brim-bottom',(12,30),(36,30))
        self.add_bezier('brim-right',(36,30),((40,30),(42,28),(42,25)),((42,24),(42,22),(34,22)))
        self.add_contour('brim','brim-left','brim-bottom','brim-right')
        self.add_line('body-left',(12,30),(12,36))
        self.add_arc('bottom-left',(12,36),(18,42),radius_x=6,sweep=False)
        self.add_line('bottom',(18,42),(30,42))
        self.add_arc('bottom-right',(30,42),(36,36),radius_x=6,sweep=False)
        self.add_line('body-right',(36,36),(36,30))
        self.add_contour('crown','body-left','bottom-left','bottom','bottom-right','body-right')
        self.relate('connect','crown','brim')

        self.add_polyline('sparkle',(16,6),(19,11),(26,14),(19,17),(16,21),(13,17),(6,14),(13,11),closed=True)
        self.add_line('wand',(34,10),(42,6))

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
