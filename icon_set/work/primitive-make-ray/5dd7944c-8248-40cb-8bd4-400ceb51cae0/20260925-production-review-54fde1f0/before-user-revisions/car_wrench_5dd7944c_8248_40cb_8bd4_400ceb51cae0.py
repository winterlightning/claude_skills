"""Car Repair and Maintenance. Smooth mirrored car silhouette with round wheel arches and an open double-ended wrench.
Keyshape HRECT_L: extremes authored from its SOLO48 centerline box.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5dd7944c-8248-40cb-8bd4-400ceb51cae0'
SOURCE_PATH = 'pictographic-primitives/other/car wrench_5dd7944c-8248-40cb-8bd4-400ceb51cae0.svg'
AUTHOR = 'gpt-6'
PLAN = 'Smooth mirrored car silhouette with round wheel arches and an open double-ended wrench.'
OMISSIONS = 'None.'
CONSTRUCTION_REFERENCES = ['car-front']
PARENT_MODULE = 'icon_set/model/icons/solo/car_wrench_5dd7944c_8248_40cb_8bd4_400ceb51cae0.py'

class Drawing(Solo48):
    icon_id = 'car-wrench'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('car', 'wrench')

    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{n}-{i}'; kind,end,*args=c
            if kind=='L' and here==end: continue
            if kind=='L': self.add_line(eid,here,end)
            elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self):
        self.box('phone',8,4,40,44,4)
        self.add_line('phone-band',(8,36),(40,36))
    def calendar(self,wide=False):
        l,t,r,b,bind,divider=(6,10,42,42,6,18) if wide else (8,8,40,44,4,16)
        self.box('calendar',l,t,r,b,4)
        self.add_line('divider',(l,divider),(r,divider))
        for x in (16,32): self.add_line(f'binding-{x}',(x,bind),(x,t))
    def dollar(self,x=24,y=24):
        self.path('dollar',(x+4,y-5),[('C',(x,y-6),(x+3,y-6),(x+1,y-6)),('C',(x,y),(x-8,y-6),(x-8,y-1)),('C',(x,y+6),(x+8,y+1),(x+8,y+6)),('C',(x-4,y+5),(x-1,y+6),(x-3,y+6))])
        self.add_line('dollar-top',(x,y-8),(x,y-6))
        self.add_line('dollar-bottom',(x,y+6),(x,y+8))
    def cross(self,n,x,y,r):
        for j,(dx,dy) in enumerate(((-r,0),(r,0),(0,-r),(0,r))):self.add_line(f'{n}-{j}',(x,y),(x+dx,y+dy))
    def handset(self,x=24,y=23):
        self.path('handset',(x-3,y-5),[('L',(x-6,y-6)),('L',(x-7,y-6)),('C',(x+4,y+5),(x-7,y),(x-1,y+5)),('L',(x+7,y+2)),('L',(x+4,y-1))])
    def contacts(self):
        # Split only actual straight attachment nodes; connect exact shared endpoints.
        from icon_set.model.primitives import Line
        from dataclasses import replace
        points={p.start for p in self.primitives}|{p.end for p in self.primitives}
        changes={}; fresh=[]
        for p in self.primitives:
            if isinstance(p,Line) and p.start!=p.end:
                a,b=p.start,p.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in points if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]; ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        name=f'{p.element_id}-join-{j}'; fresh.append(Line(name,u,v));ids.append(name)
                    changes[p.element_id]=ids;continue
            fresh.append(p)
        self.primitives[:]=fresh
        self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in changes.get(m,[m]))) for c in self.contours]
        for j,a in enumerate(self.primitives):
            for b in self.primitives[j+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)

    def build(self):

        self.path('car',(10,20),[('C',(18,8),(14,12),(15,8)),('L',(30,8)),('C',(38,20),(33,8),(34,12)),('C',(44,26),(42,20),(44,22)),('L',(44,32)),('L',(40,32)),('C',(34,40),(40,37),(38,40)),('C',(28,34),(30,40),(28,37)),('L',(20,34)),('C',(14,40),(20,37),(18,40)),('C',(8,32),(10,40),(8,37)),('L',(4,32)),('L',(4,26)),('C',(10,20),(4,22),(6,20))],True)
        self.path('left-jaw',(16,18),[('A',(20,22),4,4,True),('A',(16,26),4,4,True)])
        self.path('right-jaw',(32,18),[('A',(28,22),4,4,False),('A',(32,26),4,4,False)])
        self.add_line('wrench-shaft',(20,22),(28,22))

        self.contacts()
