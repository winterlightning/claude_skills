"""Female User Profile Avatar. Avatar with circular jaw and smooth shoulder arcs. Body top32 = jaw bottom28 + HEAD_BODY_CENTERLINE_GAP; zero visible head/body gap.
Keyshape VRECT_L: extremes authored from its SOLO48 centerline box.
Omissions: Tiny neck seams omitted; original hairstyle and open bust retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '909c8013-e74f-52f3-bc3c-88ac60cd382c'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_909c8013-e74f-52f3-bc3c-88ac60cd382c.svg'
AUTHOR = 'gpt-6'
PLAN = 'Avatar with circular jaw and smooth shoulder arcs. Body top32 = jaw bottom28 + HEAD_BODY_CENTERLINE_GAP; zero visible head/body gap.'
OMISSIONS = 'Tiny neck seams omitted; original hairstyle and open bust retained.'
CONSTRUCTION_REFERENCES = ['human_ref/user.svg']
PARENT_MODULE = 'icon_set/model/icons/solo/person_with_side_parted_bob_909c8013_e74f_52f3_bc3c_88ac60cd382c.py'

class Drawing(Solo48):
    icon_id = 'person-with-side-parted-bob'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('person', 'with', 'side-parted', 'bob')

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
        self.path('hair',(8,26),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,26))])

        # Circular jaw bottom28; shoulder top32 yields zero ink gap at stroke4.
        self.path('fringe',(16,20),[('C',(27,14),(21,19),(25,17)),('C',(32,20),(28,17),(30,19))])
        self.path('jaw',(32,20),[('A',(24,28),8,8,True),('A',(16,20),8,8,True)])
        self.path('shoulders',(8,44),[('L',(8,40)),('A',(16,32),8,8,True),('L',(32,32)),('A',(40,40),8,8,True),('L',(40,44))])

        self.relate('connect','jaw','shoulders')

        self.contacts()
