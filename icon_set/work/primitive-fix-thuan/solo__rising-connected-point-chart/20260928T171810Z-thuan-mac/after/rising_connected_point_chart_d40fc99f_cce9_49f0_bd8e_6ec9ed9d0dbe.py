'The chart had tiny node openings and heavy connectors that formed a bent solid bar. Enlarged all three node openings and rebuilt the origin-to-node and node-to-node links with exposed exact boundary joins.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: Lucide chart-network.\nKeyshape SQUARE; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d40fc99f-cce9-49f0-bd8e-6ec9ed9d0dbe'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rising-connected-point-chart/20260928T171810Z-thuan-mac/reference/chart network_d40fc99f-cce9-49f0-bd8e-6ec9ed9d0dbe.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__rising-connected-point-chart/20260928T171810Z-thuan-mac/before/rising_connected_point_chart_d40fc99f_cce9_49f0_bd8e_6ec9ed9d0dbe.py'
class Drawing(Solo48):
    icon_id='rising-connected-point-chart'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('chart', 'network')

    def path(self,n,p,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';q=c[1]
            if c[0]=='L':self.add_line(k,p,q)
            elif c[0]=='A':self.add_arc(k,p,q,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,p,(c[2],c[3],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4,split=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        commands=[]
        for i in range(8):
            q=pts[(i+1)%8]
            if i%2:commands.append(('A',q,rad,rad,True))
            else:
                for p in (split or {}).get(i,[]):commands.append(('L',p))
                commands.append(('L',q))
        self.path(n,pts[0],commands,True)

    def node(self,n,x,y,r,extra=()):
        import math
        offsets=set([(-r,0),(0,-r),(r,0),(0,r),*extra])
        offsets=sorted(offsets,key=lambda p:math.atan2(p[1],p[0]))
        pts=[(x+dx,y+dy) for dx,dy in offsets]
        self.path(n,pts[0],[('A',q,r,r,True) for q in pts[1:]+pts[:1]],True)

    def build(self):
        # Outlined data nodes expose exact 3-4-5 attachment points for the connecting lines.
        self.add_polyline('axes',(4,4),(4,44),(44,44))
        self.node('point-a',14,18,5,[(-3,4),(4,3)])
        self.node('point-b',28,30,5,[(-4,-3),(3,-4)])
        self.node('point-c',39,9,5,[(-3,4)])
        for name,a,b,parts in [
            ('origin-link',(4,44),(11,22),('axes','point-a')),
            ('middle-link',(18,21),(24,27),('point-a','point-b')),
            ('upper-link',(31,26),(36,13),('point-b','point-c'))]:
            self.add_line(name,a,b)
            for part in parts:self.relate('connect',part,name)

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The larger node openings need an expanded chart envelope; connected strokes near the origin create intentional converging spaces. All three node interiors remain open.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'd22ef1ad7a347dc490ca3d6b92ef7689bce4e26062ca22abe5691cc56f379b35'}
