"""Broad light bulb with circular crown, tapered shoulders and wider screw base. Shared vertical axis x=24; extremes (8,4)-(40,44).
Keyshape VRECT_L; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide lightbulb: circular crown and narrowing lower shoulders; source retains closed base.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6af73469-938c-4006-9537-bc65e0be96b4'
SOURCE_PATH = 'pictographic-primitives/work/bulb 1_6af73469-938c-4006-9537-bc65e0be96b4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('bulb', '1')

    def build(self):
        self.path('bulb',(8,20),('A',(40,20),16,16,True),('A',(32,32),8,12,True),('A',(30,36),2,4,False),('L',(30,42)),('A',(28,44),2,2,True),('L',(20,44)),('A',(18,42),2,2,True),('L',(18,36)),('A',(16,32),2,4,False),('A',(8,20),8,12,True),closed=True)
        self.add_line('base-seam',(18,36),(30,36))
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
