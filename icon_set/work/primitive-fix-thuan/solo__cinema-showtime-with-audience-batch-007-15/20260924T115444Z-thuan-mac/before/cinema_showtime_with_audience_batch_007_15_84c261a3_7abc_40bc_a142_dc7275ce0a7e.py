"""Cinema Showtime with Audience.
Plan: Cinema curtain top rail with open curved drapes, central clock and two shallow rear seat silhouettes. Reduce three seats to two and omit curtain ties; open corners avoid miniature enclosed pockets. Clock hands intentionally asymmetric.
Visible-ink envelope: (4, 4, 44, 44); 4-unit stroke on the integer grid.
Construction: Lucide ticket; independently authored SOLO48 geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84c261a3-7abc-40bc-a142-dc7275ce0a7e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/entertainment/movie cinema clock_84c261a3-7abc-40bc-a142-dc7275ce0a7e.svg'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = '/Applications/Workspaces/pictographic/claude_skills/work/brief-exports/20260918-all-todo-batches-15/batches/batch-007/references/movie cinema clock_84c261a3-7abc-40bc-a142-dc7275ce0a7e.svg'

def circle(s,n,x,y,r):
    pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
    for i,(a,b) in enumerate(zip(pts,pts[1:])):
        s.add_arc(n+str(i),a,b,radius_x=r)
    s.add_contour(n,*(n+str(i) for i in range(4)),closed=True)

def box(s,n,l,t,r,b,k=3,nodes=()):
    pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k),(l+k,t)]
    members=[]
    for i,(a,z) in enumerate(zip(pts,pts[1:])):
        if a==z: continue
        if i%2:
            p=f'{n}-{i}';s.add_arc(p,a,z,radius_x=k);members.append(p)
        else:
            dx,dy=z[0]-a[0],z[1]-a[1]
            mid=[p for p in nodes if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            mid.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy)
            q=[a]+mid+[z]
            for j,(v,w) in enumerate(zip(q,q[1:])):
                p=f'{n}-{i}-{j}';s.add_line(p,v,w);members.append(p)
    s.add_contour(n,*members,closed=True)

class Result(Solo48):
    icon_id = 'cinema-showtime-with-audience-batch-007-15'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'entertainment'
    aliases = ()
    keywords = ('cinema', 'showtime', 'with', 'audience')

    def build(self):
        self.add_polyline('stage',(6,6),(12,6),(36,6),(42,6))
        self.add_line('curtain-tail-left',(6,16),(6,27))
        self.add_line('curtain-tail-right',(42,16),(42,27))
        self.relate('connect','curtain-tail-left','curtain-left')
        self.relate('connect','curtain-tail-right','curtain-right')
        self.add_arc('curtain-left',(12,6),(6,16),radius_x=6,radius_y=10)
        self.add_arc('curtain-right',(42,16),(36,6),radius_x=6,radius_y=10)
        self.relate('connect','stage','curtain-left');self.relate('connect','stage','curtain-right')
        circle(self,'clock',24,22,8)
        self.add_polyline('hands',(24,14),(24,22),(27,22));self.relate('connect','clock','hands')
        for i,x in enumerate((13,35)):
            self.add_arc(f'seat-{i}',(x-7,42),(x+7,42),radius_x=7,radius_y=3)
