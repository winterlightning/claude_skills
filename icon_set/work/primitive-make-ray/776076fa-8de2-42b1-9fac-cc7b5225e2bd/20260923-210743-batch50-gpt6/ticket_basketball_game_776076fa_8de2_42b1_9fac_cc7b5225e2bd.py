"""A basketball and small circular mark sit behind an angled admission ticket.
Plan: A large circular ball is partially open behind the ticket; the ticket has opposed inward notches.
Keyshape: SQUARE. Exact envelope: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Construction references: icon_set/references/lucide/original/ticket.svg and atomic-debug/ticket.svg: coherent contours, shared junctions, and consistent rounding; re-authored on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '776076fa-8de2-42b1-9fac-cc7b5225e2bd'
SOURCE_PATH = 'icon_set/work/todo-references/ticket basketball game_776076fa-8de2-42b1-9fac-cc7b5225e2bd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ticket-basketball-game'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('ticket', 'basketball', 'game')

    def path(self, name, start, operations, closed=False):
        # A coherent path owns its members exactly once.
        current=start; members=[]
        for i,op in enumerate(operations):
            n=f'{name}-{i}'
            if op[0]=='L':
                end=op[1]; self.add_line(n,current,end)
            elif op[0]=='A':
                end,rx,ry,sweep=op[1:]; self.add_arc(n,current,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                c1,c2,end=op[1:]; self.add_bezier(n,current,(c1,c2,end))
            members.append(n);current=end
        if closed and current!=start:
            n=f'{name}-close';self.add_line(n,current,start);members.append(n)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def rect(self,name,x,y,w,h,r=4,split_x=(),split_y=()):
        ops=[]
        for xx in sorted(v for v in split_x if x+r<v<x+w-r): ops.append(('L',(xx,y)))
        ops += [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True)]
        for yy in sorted(v for v in split_y if y+r<v<y+h-r): ops.append(('L',(x+w,yy)))
        ops += [('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True)]
        for xx in sorted((v for v in split_x if x+r<v<x+w-r),reverse=True): ops.append(('L',(xx,y+h)))
        ops += [('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True)]
        for yy in sorted((v for v in split_y if y+r<v<y+h-r),reverse=True): ops.append(('L',(x,yy)))
        ops += [('L',(x,y+r)),('A',(x+r,y),r,r,True)]
        # Capsules can have zero-length straight runs; omit those.
        cleaned=[];p=(x+r,y)
        for op in ops:
            if op[0]!='L' or op[1]!=p: cleaned.append(op)
            p=op[1]
        self.path(name,(x+r,y),cleaned,True)

    def join(self,*names):
        for i,a in enumerate(names):
            for b in names[i+1:]: self.relate('connect',a,b)

    def cross(self,name,x,y,r,diagonal=False):
        offsets=[(-r,-r),(r,r),(-r,r),(r,-r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        names=[]
        for i,(dx,dy) in enumerate(offsets):
            n=f'{name}-{i}';self.add_line(n,(x,y),(x+dx,y+dy));names.append(n)
        self.join(*names)

    def letter_a(self,name,apex,left,right,bar_left,bar_right):
        self.add_polyline(name,left,bar_left,apex,bar_right,right)
        self.add_line(name+'-bar',bar_left,bar_right)
        self.join(name,name+'-bar')

    def build(self):

        self.add_arc('ball',(32,19),(19,32),radius_x=13,large_arc=True,sweep=False)
        self.add_bezier('seam-one',(10,10),((19,14),(24,20),(27,27)))
        self.add_bezier('seam-two',(6,20),((17,20),(24,14),(25,8)))
        self.add_bezier('seam-three',(15,31),((17,23),(23,19),(31,16)))
        self.circle('small-mark',38,10,4)
        self.path('ticket',(16,30),[('L',(38,22)),('L',(40,27)),('C',(34,28),(36,34),(42,33)),('L',(42,34)),('L',(20,42)),('L',(18,37)),('C',(23,35),(21,29),(16,32)),('L',(16,30))],True)
        self.add_line('ticket-rule-0',(26,31),(32,29))
        self.add_line('ticket-rule-1',(28,36),(34,34))
