"""Hexagonal chemical structure with five ring atoms, an upper-right terminal atom and lower side chain. Equal radius2 nodes and explicit bond endpoints; bounds (6,6)-(42,42).
Keyshape SQUARE; fresh revision for feedback: Bad stroke drawn.
Construction reference: No useful exact Lucide molecule match; repeated circular atoms and shared cardinal bond nodes.
Omissions: The terminal atom rightward short branch omitted; upper and lower side chains restored. Radius2 atom circles use the existing small-circle exception and read as solid nodes at native size.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e1fa397a-aca0-4f59-875f-b0f6abeb1a51'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chemical-molecule-linked-atoms/20260924T090148Z-thuan-mac/reference/chemical hexagon_e1fa397a-aca0-4f59-875f-b0f6abeb1a51.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chemical-molecule-linked-atoms'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('chemical', 'hexagon')

    def build(self):
        for n,x,y in [('top',20,8),('upper-left',8,18),('lower-left',8,30),('bottom',20,36),('upper-right',28,20),('terminal',40,14)]:self.circle(n,x,y,2)
        self.add_line('bond-top-left',(10,18),(18,8))
        self.add_line('bond-top-right',(22,8),(28,18))
        self.add_line('bond-left',(8,20),(8,28))
        self.add_line('bond-bottom-left',(10,30),(18,36))
        self.add_polyline('bond-right',(28,22),(28,30),(22,36))
        self.add_line('side-chain',(30,20),(38,14))
        self.add_line('terminal-bond',(40,12),(40,6))
        self.add_polyline('lower-chain',(20,38),(20,42),(14,42))
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
