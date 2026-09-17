"""Person On Stage.
Symbol plan: Performer between parted curtains. HRECT_L (4,8)-(44,40) leaves the stage center open. human_ref/full_body_ref.png: radius3 head (24,22), torso junction (24,33), exactly8 centerline/4 ink gap. No useful exact Lucide match. Mirror curtains and simplified figure; omit arms, lower flare and garment outline to preserve separation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f498c216-bd74-4c20-ae57-aae3ee60475d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/show person_f498c216-bd74-4c20-ae57-aae3ee60475d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-performer-between-open-stage-curtains'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('person', 'on', 'stage')

    def build(self):
        for name,sgn in [('left',-1),('right',1)]:
         p=lambda x,y:(24+sgn*x,y)
         self.add_line(name+'-top',p(20,8),p(8,8))
         self.add_bezier(name+'-drape',p(8,8),(p(8,14),p(12,18),p(12,24)))
         self.add_line(name+'-inner',p(12,24),p(12,40))
         self.add_polyline(name+'-outer',p(12,40),p(20,40),p(20,24),p(20,8))
         self.add_line(name+'-tie',p(12,24),p(20,24))
         for a,z in [('top','drape'),('drape','inner'),('inner','outer'),('outer','top'),('tie','drape'),('tie','inner'),('tie','outer')]:self.relate('connect',name+'-'+a,name+'-'+z)
        self.circle('head',24,22,3)
        self.add_line('torso',(24,33),(24,35))
        self.add_polyline('legs',(20,40),(24,35),(28,40));self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

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
