"""Long-neck brontosaurus with a pointed sweeping tail, two broad legs and an upright neck. Extremes (4,8)-(44,40); intentional side-view asymmetry.
Keyshape HRECT_L; fresh revision for feedback: Bad stroke drawn.
Construction reference: No useful local Lucide subject match; supplied original defines the silhouette.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2b7b6c5f-c04e-5ce2-a62b-3da414005113'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur brontosaurus_2b7b6c5f-c04e-5ce2-a62b-3da414005113.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'brontosaurus'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('dinosaur', 'brontosaurus')

    def build(self):
        self.path('dinosaur',(4,12),('A',(8,8),4,4,True),('L',(12,8)),('A',(16,12),4,4,True),('L',(18,24)),('A',(30,26),12,8,True),('A',(44,32),20,12,False),('A',(32,34),12,8,True),('L',(32,40)),('L',(24,40)),('L',(24,32)),('L',(16,30)),('L',(16,40)),('L',(8,40)),('L',(6,16)),('A',(4,12),2,4,True),closed=True)
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
