"""A hand connects to a lower blood-transfusion bag.
Plan: Raised hand at left, lower bag at right, and a broad connecting tube.
Keyshape SQUARE: exact ink and centerline envelopes ((4, 4, 44, 44), (6, 6, 42, 42)).
References: Supplied SVG, rendered and visually inspected. Lucide original/hand.svg and atomic-debug/hand.svg: coherent contours, shared nodes, consistent rounding; re-authored on SOLO48. Shared human-reference.md and human_ref references: coherent human-part construction; no detached head occurs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c1a874c-bde4-457e-8690-be53b0c8ed3b'
SOURCE_PATH = 'icon_set/work/todo-references/transfusion hand blood_1c1a874c-bde4-457e-8690-be53b0c8ed3b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'transfusion-hand-blood'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('transfusion', 'hand', 'blood')

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

        self.path('hand',(10,28),[('L',(10,24)),('C',(6,22),(6,17),(6,12)),('A',(14,6),8,6,True),('A',(22,14),8,8,True),('L',(22,16)),('C',(28,16),(28,22),(22,27)),('L',(22,35))])
        self.add_line('cuff',(10,28),(14,28));self.join('hand','cuff')
        self.path('tube',(14,24),[('L',(14,34)),('A',(22,42),8,8,False),('L',(34,42)),('A',(36,40),2,2,False)])

        self.path('bag',(34,20),[('L',(38,20)),('A',(42,24),4,4,True),('L',(42,32)),('A',(38,36),4,4,True),('L',(38,40)),('L',(34,40)),('L',(34,36)),('A',(30,32),4,4,True),('L',(30,24)),('A',(34,20),4,4,True)],True)
        self.cross('medical-cross',36,28,3)
        self.join('tube','bag')
