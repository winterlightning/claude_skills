"""A trophy sits above a branching tournament diagram.
Plan: A symmetric cup owns paired handles and a central stem; two capsule nodes repeat below.
Keyshape SQUARE: exact ink and centerline envelopes ((4, 4, 44, 44), (6, 6, 42, 42)).
References: Supplied SVG, rendered and visually inspected. Lucide original/trophy.svg and atomic-debug/trophy.svg: coherent contours, shared nodes, consistent rounding; re-authored on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6d731820-468b-5c38-b10b-859f24a8eab3'
SOURCE_PATH = 'pictographic-primitives/sports/tournament bracket_6d731820-468b-5c38-b10b-859f24a8eab3.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'tournament-bracket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tournament', 'bracket')

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
        self.path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

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
        self.path('cup',(16,6),[('L',(32,6)),('L',(32,10)),('L',(32,14)),('A',(24,22),8,8,True),('A',(16,14),8,8,True),('L',(16,10))],True)
        self.path('handle-left',(16,6),[('L',(10,6)),('A',(6,10),4,4,False),('A',(10,14),4,4,False),('L',(16,14))])
        self.path('handle-right',(32,6),[('L',(38,6)),('A',(42,10),4,4,True),('A',(38,14),4,4,True),('L',(32,14))])
        self.join('cup','handle-left');self.join('cup','handle-right')
        self.add_line('stem',(24,22),(24,30));self.join('cup','stem')
        self.add_polyline('bracket',(12,38),(12,30),(24,30),(36,30),(36,38));self.join('stem','bracket')
        for name,x in [('node-left',12),('node-right',36)]:
            self.circle(name,x,40,2)
            self.join(name,'bracket')

