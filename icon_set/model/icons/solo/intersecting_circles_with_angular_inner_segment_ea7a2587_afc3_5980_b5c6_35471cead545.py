"""Two symmetric overlapping circular outlines with shared intersections. Four smooth branches replace angular inner kink.
Keyshape HRECT_L. No useful subject-specific Lucide match; supplied original determines the silhouette.
Omissions: Removed accidental angular kink from previous revision; preserve original two-loop topology."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ea7a2587-afc3-5980-b5c6-35471cead545'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/boolean and_ea7a2587-afc3-5980-b5c6-35471cead545.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'intersecting-circles-with-angular-inner-segment'
    keyshape = Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="diagrams"
    aliases=()
    keywords=('intersecting', 'circles', 'with', 'angular', 'inner', 'segment')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Mirrored equal elliptical loops share exact upper and lower intersection nodes.
        for side in (-1,1):
         def p(x,y):return (24+side*x,y)
         path(f'outer-{side}',p(0,12),[('A',p(8,8),8,4,side>0),('A',p(20,24),12,16,side>0),('A',p(8,40),12,16,side>0),('A',p(0,36),8,4,side>0)])
         path(f'inner-{side}',p(0,12),[('A',p(8,24),8,12,side>0),('A',p(0,36),8,12,side>0)])
        for a in ['outer--1','outer-1','inner--1','inner-1']:
         for b in ['outer--1','outer-1','inner--1','inner-1']:
          if a<b:join(a,b)

