"""Question Mark Message Bubble. Smooth speech bubble with a diagonal tail and clear hook-to-dot separation.
Keyshape VRECT_L: extremes authored from its SOLO48 centerline box.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'dd81b6db-6dd5-4927-8f6a-80c73d19c8cd'
SOURCE_PATH = 'pictographic-primitives/messages/messages bubble square question_dd81b6db-6dd5-4927-8f6a-80c73d19c8cd.svg'
AUTHOR = 'gpt-6'
PLAN = 'Smooth speech bubble with a diagonal tail and clear hook-to-dot separation.'
OMISSIONS = 'None.'
CONSTRUCTION_REFERENCES = ['message-square']
PARENT_MODULE = 'icon_set/model/icons/solo/messages_bubble_square_question_dd81b6db_6dd5_4927_8f6a_80c73d19c8cd.py'

class Drawing(Solo48):
    icon_id = 'messages-bubble-square-question'
    keyshape = Keyshape.VRECT_L
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

        self.path('bubble',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,34)),('A',(36,38),4,4,True),('L',(25,38)),('L',(16,44)),('L',(16,38)),('L',(12,38)),('A',(8,34),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('question',(19,17),[('A',(29,17),5,5,True),('C',(24,22),(29,20),(24,20))])
        self.add_dot('question-dot',(24,30))

        self.contacts()
