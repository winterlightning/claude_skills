"""Three Row Gantt Chart — batch 51."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '89dfc62c-1d1f-448c-800b-5042956a5d9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/workflow gantt chart_89dfc62c-1d1f-448c-800b-5042956a5d9e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-row-gantt-chart'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('three', 'row', 'gantt', 'chart')

    def build(self):
        # Plan: three task rectangles across three vertical timeline guides.
        # VRECT_L extremes8,4,40,44. Lucide table informs regular shared grid junctions.
        for i,(x,y,w) in enumerate(((8,4,24),(24,20,16),(24,36,16))):
            self.box(f'bar-{i}',x,y,w,8,attachments=((24,y),(24,y+8)))
        guides=[('left',(8,12),(8,44)),('middle-0',(24,4),(24,12)),('middle-1',(24,12),(24,20)),('middle-2',(24,28),(24,36)),('right-0',(40,4),(40,20)),('right-1',(40,28),(40,36))]
        for n,a,z in guides:self.add_line(n,a,z)
        # Only paths with actual shared endpoint nodes receive scoped connections.
        from icon_set.renderers.svg import build_paths
        paths=build_paths(self.draw())
        for i,a in enumerate(paths):
            ap={(p.start.x,p.start.y) for p in a['primitives']}|{(p.end.x,p.end.y) for p in a['primitives']}
            for z in paths[i+1:]:
                zp={(p.start.x,p.start.y) for p in z['primitives']}|{(p.end.x,p.end.y) for p in z['primitives']}
                if ap & zp:self.relate('connect',a['id'],z['id'])


    def circle(self,n,x,y,r,attachments=()):
        from math import atan2
        pts=list(dict.fromkeys([(x+r,y),(x,y+r),(x-r,y),(x,y-r)]+list(attachments)))
        pts.sort(key=lambda p:atan2(p[1]-y,p[0]-x))
        for j in range(len(pts)):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%len(pts)],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(len(pts))],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)

