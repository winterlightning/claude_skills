"""An open hand with a palm mark sits beside a microchip.
Plan: Three tall fingertips and a thumb form one outline; the chip owns an evenly spaced pin series.
Keyshape: SQUARE. Exact envelope: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Construction references: icon_set/references/lucide/original/hand.svg and atomic-debug/hand.svg: coherent contours, shared junctions, and consistent rounding; re-authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '40415ff8-ab5e-4613-9886-33d055540f90'
SOURCE_PATH = 'icon_set/work/todo-references/technology hand chip_40415ff8-ab5e-4613-9886-33d055540f90.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'technology-hand-chip'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('technology', 'hand', 'chip')

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

        self.path('hand',(6,42),[('L',(6,14)),('A',(12,14),3,3,True),('L',(12,9)),('A',(18,9),3,3,True),('L',(18,13)),('A',(24,13),3,3,True),('L',(24,22)),('A',(30,22),3,3,True),('L',(30,29)),('C',(30,34),(22,35),(22,39)),('L',(22,42))])
        self.add_line('finger-division-left',(12,14),(12,22));self.join('hand','finger-division-left')
        self.add_line('finger-division-right',(18,13),(18,22));self.join('hand','finger-division-right')
        self.path('palm-mark',(15,26),[('C',(11,30),(11,32),(15,36)),('C',(19,32),(19,30),(15,26))],True)
        self.rect('chip',32,28,8,8,1,split_x=(34,38),split_y=(30,34))
        for i,p in enumerate((34,38)):
            for name,a,b in [(f'pin-top-{i}',(p,26),(p,28)),(f'pin-bottom-{i}',(p,36),(p,38))]:
                self.add_line(name,a,b);self.join('chip',name)
        for i,p in enumerate((30,34)):
            for name,a,b in [(f'pin-left-{i}',(30,p),(32,p)),(f'pin-right-{i}',(40,p),(42,p))]:
                self.add_line(name,a,b);self.join('chip',name)
