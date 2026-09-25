"""Home Video Play Button. Rounded house with its original circular play medallion restored.
Keyshape SQUARE: extremes authored from its SOLO48 centerline box.
Omissions: No defining omissions; nested play medallion may require a spacing exception after visual review.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '7e3b79f2-dcc5-4988-ab08-8460306de315'
SOURCE_PATH = 'pictographic-primitives/other/house with play button_7e3b79f2-dcc5-4988-ab08-8460306de315.svg'
AUTHOR = 'gpt-6'
PLAN = 'Rounded house with its original circular play medallion restored.'
OMISSIONS = 'No defining omissions; nested play medallion may require a spacing exception after visual review.'
CONSTRUCTION_REFERENCES = ['house']
PARENT_MODULE = 'icon_set/model/icons/solo/house_with_play_button_7e3b79f2_dcc5_4988_ab08_8460306de315.py'

class Drawing(Solo48):
    icon_id = 'house-with-play-button'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('house', 'with', 'play', 'button')

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

        self.path('house',(6,21),[('L',(24,6)),('L',(42,21)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,21))],True)
        self.circle('medallion',24,27,8)
        self.add_polyline('play',(22,24),(27,27),(22,30),closed=True)

        self.contacts()
