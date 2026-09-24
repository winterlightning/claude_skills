"""Apple on a weighing platform beside a round scale dial. Clearer paired apple lobes, angled dial pointer and shared base; bounds (6,6)-(42,42).
Keyshape SQUARE; fresh revision for feedback: Bad stroke drawn.
Construction reference: Lucide scale: shared structural posts; original reference controls the separate apple and dial.
Omissions: Minor apple cleft reduced to a simple lobed outline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'deb50b30-8dc9-43c7-9d32-ad3dac6a9642'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__apple-on-weighing-scale-batch-009-14/20260924T090148Z-thuan-mac/reference/scale apple_deb50b30-8dc9-43c7-9d32-ad3dac6a9642.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apple-on-weighing-scale-batch-009-14'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('scale', 'apple')

    def build(self):
        self.circle('dial',36,12,6)
        self.add_line('pointer',(36,6),(38,12))
        self.add_line('dial-post',(36,18),(36,34))
        self.add_polyline('base',(6,34),(14,34),(36,34),(42,34),(38,42),(10,42),closed=True)
        self.path('apple',(14,16),('A',(6,18),5,4,False),('A',(14,25),8,7,False),('A',(22,18),8,7,False),('A',(14,16),5,4,False),closed=True)
        self.add_line('stem',(14,16),(16,8))
        self.add_polyline('platform',(6,25),(14,25),(22,25))
        self.add_line('platform-post',(14,25),(14,34))
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
