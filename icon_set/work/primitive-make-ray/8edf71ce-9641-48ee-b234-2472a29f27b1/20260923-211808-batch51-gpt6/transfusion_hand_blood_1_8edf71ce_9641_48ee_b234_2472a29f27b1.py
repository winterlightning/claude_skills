"""A hand connects by a curved tube to a raised blood-transfusion bag.
Plan: Hand and bag retain opposite upper positions; a U-shaped tube links their lower ports.
Keyshape SQUARE: exact ink and centerline envelopes ((4, 4, 44, 44), (6, 6, 42, 42)).
References: Supplied SVG, rendered and visually inspected. Lucide original/hand.svg and atomic-debug/hand.svg: coherent contours, shared nodes, consistent rounding; re-authored on SOLO48. Shared human-reference.md and human_ref references: coherent human-part construction; no detached head occurs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8edf71ce-9641-48ee-b234-2472a29f27b1'
SOURCE_PATH = 'icon_set/work/todo-references/transfusion hand blood 1_8edf71ce-9641-48ee-b234-2472a29f27b1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'transfusion-hand-blood-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('transfusion', 'hand', 'blood', '1')

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

        self.path('hand',(8,42),[('L',(8,30)),('C',(8,26),(6,24),(6,20)),('C',(6,13),(7,6),(14,6)),('C',(17,6),(19,7),(18,11)),('L',(17,20)),('L',(21,17)),('C',(26,13),(25,22),(20,28)),('L',(20,34))])
        self.path('tube',(14,30),[('L',(14,34)),('A',(22,42),8,8,False),('L',(28,42)),('A',(36,34),8,8,False),('L',(36,26))])

        self.path('bag',(34,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,18)),('A',(38,22),4,4,True),('L',(38,26)),('L',(34,26)),('L',(34,22)),('A',(30,18),4,4,True),('L',(30,10)),('A',(34,6),4,4,True)],True)
        self.cross('medical-cross',36,14,3)
        self.join('tube','bag')
