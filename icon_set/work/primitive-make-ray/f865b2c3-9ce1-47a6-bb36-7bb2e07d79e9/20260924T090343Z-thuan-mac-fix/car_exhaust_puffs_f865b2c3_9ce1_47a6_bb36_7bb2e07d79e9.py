"""Front-facing car with a cloud-shaped exhaust puff above a smaller circular puff. Restored cloud lobes and windshield; bounds (4,8)-(44,40).
Keyshape HRECT_L; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide car-front: separate windshield and paired wheel stems; source exhaust cloud uses round lobes.
Omissions: Tiny headlight marks omitted for interior spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f865b2c3-9ce1-47a6-bb36-7bb2e07d79e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-exhaust-puffs/20260924T090148Z-thuan-mac/reference/low emission zone_f865b2c3-9ce1-47a6-bb36-7bb2e07d79e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-exhaust-puffs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('low', 'emission', 'zone')

    def build(self):
        self.path('cloud',(10,12),('A',(20,12),5,4,True),('A',(16,20),4,8,True),('L',(8,20)),('A',(4,16),4,4,True),('A',(10,12),6,4,True),closed=True)
        self.circle('small-puff',7,32,3)
        self.add_polyline('car',(20,30),(26,22),(38,22),(44,30),(44,38),(40,38),(24,38),(20,38),closed=True)
        self.add_line('windshield',(20,30),(44,30))
        for x in (24,40):self.add_line('wheel-'+str(x),(x,38),(x,40))
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
