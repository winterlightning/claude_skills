"""Diagonal celery bunch: rounded stalk base with parallel ribs meeting a scalloped leafy crown. Coherent arc lobes replace kinked Bezier loops. Bounds (6,6)-(42,42).
Keyshape SQUARE; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide leafy-green: connected scalloped leaf silhouette and a single clear vein.
Omissions: Three source stalks reduced to two; crown retains multiple leaves.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '59ce0e63-72d1-4919-9043-cd2872b7a013'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/celery_59ce0e63-72d1-4919-9043-cd2872b7a013.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'celery-bunch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('celery',)

    def build(self):
        self.path('outline',(10,38),('A',(6,30),4,8,True),('L',(18,18)),('A',(18,10),4,4,True),('A',(26,10),4,4,True),('A',(34,10),4,4,True),('A',(38,18),4,8,True),('A',(38,26),4,4,True),('A',(30,30),8,4,True),('L',(18,42)),('A',(10,38),8,4,True),closed=True)
        self.add_line('stalk-rib',(10,38),(26,22))
        self.contacts()

    def path(self, name, start, *commands, closed=False):
        members=[]
        here=start
        for j,command in enumerate(commands):
            kind,end,*args=command
            ident=f'{name}-{j}'
            if kind=='L': self.add_line(ident,here,end)
            else:
                rx,ry,sweep=args
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            here=end;members.append(ident)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def contacts(self):
        # Split receiving straight runs at true attachment nodes. Declare only
        # actual endpoint contact; never connect separated shapes.
        from icon_set.model.primitives import Line
        from dataclasses import replace
        endpoints={p.start for p in self.primitives}|{p.end for p in self.primitives}
        replacement={};rebuilt=[]
        for p in self.primitives:
            if isinstance(p,Line) and p.start!=p.end:
                a,b=p.start,p.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in endpoints if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        ident=f'{p.element_id}-join-{j}';rebuilt.append(Line(ident,u,v));ids.append(ident)
                    replacement[p.element_id]=ids
                    continue
            rebuilt.append(p)
        self.primitives[:]=rebuilt
        self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacement.get(m,[m]))) for c in self.contours]
        for j,a in enumerate(self.primitives):
            for b in self.primitives[j+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)
