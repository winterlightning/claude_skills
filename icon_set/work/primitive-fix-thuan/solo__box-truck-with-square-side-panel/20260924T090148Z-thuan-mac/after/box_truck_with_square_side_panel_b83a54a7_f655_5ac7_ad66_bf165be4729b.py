"""Box delivery truck with closed cargo body, square side panel and circular wheels attached to the chassis. Bounds (4,8)-(44,40); shared wheel radius3 and y=37.
Keyshape HRECT_L; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide truck: equal circular wheels and body/chassis attachment nodes; source square panel retained.
Omissions: None
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b83a54a7-f655-5ac7-ad66-bf165be4729b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__box-truck-with-square-side-panel/20260924T090148Z-thuan-mac/reference/delivery truck_b83a54a7-f655-5ac7-ad66-bf165be4729b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'box-truck-with-square-side-panel'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('delivery', 'truck')

    def build(self):
        self.path('cargo',(30,16),('L',(30,10)),('A',(28,8),2,2,False),('L',(6,8)),('A',(4,10),2,2,False),('L',(4,32)),('A',(6,34),2,2,False),('L',(12,34)),('L',(30,34)),('L',(30,16)),closed=True)
        self.add_polyline('cab',(30,16),(36,16),(44,26),(44,34),(36,34),(30,34))
        self.add_polyline('panel',(13,17),(21,17),(21,25),(13,25),closed=True)
        for x in (12,36):self.circle('wheel-'+str(x),x,37,3)
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
