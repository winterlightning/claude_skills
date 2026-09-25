"""Question Mark Message Bubble. Smooth speech-bubble corners and a genuine diagonal tail replace the clipped polygon.
Keyshape SQUARE: extremes authored from its SOLO48 centerline box.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dd81b6db-6dd5-4927-8f6a-80c73d19c8cd'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square question_dd81b6db-6dd5-4927-8f6a-80c73d19c8cd.svg'
AUTHOR = 'gpt-6'
PLAN = 'Smooth speech-bubble corners and a genuine diagonal tail replace the clipped polygon.'
OMISSIONS = 'None.'
CONSTRUCTION_REFERENCES = ['message-square']
PARENT_MODULE = 'icon_set/model/icons/solo/messages_bubble_square_question_dd81b6db_6dd5_4927_8f6a_80c73d19c8cd.py'

class Drawing(Solo48):
    icon_id = 'messages-bubble-square-question'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('messages', 'bubble', 'square', 'question')

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

        self.path('bubble',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,32)),('A',(38,36),4,4,True),('L',(25,36)),('L',(16,42)),('L',(16,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        self.path('question',(19,18),[('A',(29,18),5,5,True),('C',(24,24),(29,22),(24,21))])
        self.add_dot('question-dot',(24,31))

        self.contacts()
