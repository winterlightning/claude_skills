"""Dollar Sign Settings Gear. Eight smoothly repeated gear teeth surround a taller curved dollar sign.
Keyshape SQUARE: extremes authored from its SOLO48 centerline box.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fa84ff77-a565-4df3-9360-0b7e9c3de772'
SOURCE_PATH = 'pictographic-primitives/other/cog dollar_fa84ff77-a565-4df3-9360-0b7e9c3de772.svg'
AUTHOR = 'gpt-6'
PLAN = 'Eight smoothly repeated gear teeth surround a taller curved dollar sign.'
OMISSIONS = 'None.'
CONSTRUCTION_REFERENCES = ['settings']
PARENT_MODULE = 'icon_set/model/icons/solo/cog_dollar_fa84ff77_a565_4df3_9360_0b7e9c3de772.py'

class Drawing(Solo48):
    icon_id = 'cog-dollar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('cog', 'dollar')

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
        self.box('phone',8,4,40,44,5)
        self.add_line('phone-band',(8,36),(40,36))
    def calendar(self,wide=False):
        l,t,r,b,bind,divider=(6,10,42,42,6,18) if wide else (8,8,40,44,4,16)
        self.box('calendar',l,t,r,b,4)
        self.add_line('divider',(l,divider),(r,divider))
        for x in (16,32): self.add_line(f'binding-{x}',(x,bind),(x,t))
    def dollar(self,x=24,y=24):
        self.path('dollar',(x+4,y-7),[('C',(x,y-8),(x+3,y-8),(x+1,y-8)),('C',(x,y),(x-8,y-8),(x-8,y-1)),('C',(x,y+8),(x+8,y+1),(x+8,y+8)),('C',(x-4,y+7),(x-1,y+8),(x-3,y+8))])
        self.add_line('dollar-top',(x,y-11),(x,y-8))
        self.add_line('dollar-bottom',(x,y+8),(x,y+11))
    def cross(self,n,x,y,r):
        for j,(dx,dy) in enumerate(((-r,0),(r,0),(0,-r),(0,r))):self.add_line(f'{n}-{j}',(x,y),(x+dx,y+dy))
    def handset(self,x=24,y=23):
        self.path('handset',(x-7,y-8),[('L',(x-4,y-5)),('C',(x-5,y-2),(x-2,y-3),(x-4,y-2)),('C',(x+2,y+5),(x-4,y+1),(x-1,y+4)),('C',(x+5,y+4),(x+2,y+4),(x+3,y+2)),('L',(x+8,y+7)),('C',(x+5,y+10),(x+10,y+9),(x+7,y+10)),('C',(x-10,y-5),(x-1,y+10),(x-10,y+1)),('C',(x-7,y-8),(x-10,y-7),(x-9,y-10))],True)
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

        quarter=[('C',(27,6),(23,6),(25,6)),('C',(30,10),(29,6),(28,10)),('C',(35,10),(32,10),(33,8)),('C',(38,13),(37,10),(38,11)),('C',(38,18),(40,15),(38,16)),('C',(42,21),(38,20),(42,19))]
        def rot(p,k):
            x,y=p[0]-24,p[1]-24
            for _ in range(k):x,y=-y,x
            return x+24,y+24
        commands=[('C',rot(c[1],k),rot(c[2],k),rot(c[3],k)) for k in range(4) for c in quarter]
        self.path('gear',(21,6),commands,True)
        self.dollar()

        self.contacts()
