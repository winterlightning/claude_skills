"""Front-facing car below a horizontal key. Mirrored car with visible windshield and rounded lower corners; key teeth share an 8-unit repeat. Bounds (8,4)-(40,44).
Keyshape VRECT_L; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide car-front: tapered windshield, rounded bumper and paired wheel stems.
Omissions: Headlight marks omitted; windshield restored.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/3ca5e341-784c-4a0c-9aa0-c71bcbbafbd2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-key-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('car', 'with', 'key')

    def build(self):
        y=26
        self.path('car',(8,y+8),('L',(14,y)),('L',(34,y)),('L',(40,y+8)),('L',(40,y+14)),('A',(38,y+16),2,2,True),('L',(36,y+16)),('L',(12,y+16)),('L',(10,y+16)),('A',(8,y+14),2,2,True),('L',(8,y+8)),closed=True)
        self.add_line('windshield',(8,y+8),(40,y+8))
        for x in (12,36):self.add_line('wheel-'+str(x),(x,y+16),(x,y+18))

        self.circle('key-bow',34,10,6)
        self.add_line('key-shaft',(8,10),(28,10))
        for x in (12,20):self.add_line('tooth-'+str(x),(x,10),(x,16))
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
