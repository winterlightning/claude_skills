"""A panoramic virtual environment is represented by a curved wraparound wall.
Plan: Elliptical top and bottom edges frame the two narrow side panels.
Keyshape SQUARE: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
References: Supplied SVG rendered and inspected. No useful local Lucide subject match used; geometric reconstruction follows the supplied drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b019ae14-f0e2-47a0-aa92-21e5e4cd1cc4'
SOURCE_PATH = 'icon_set/work/todo-references/virtual environment 1_b019ae14-f0e2-47a0-aa92-21e5e4cd1cc4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'virtual-environment-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('virtual', 'environment', '1')

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

        self.path('wall',(6,14),[('C',(6,10),(14,6),(24,6)),('C',(34,6),(42,10),(42,14)),
('L', (42, 34)), ('C', (42, 37), (38, 39), (34, 40)), ('C', (30, 41), (27, 42), (24, 42)), ('C', (21, 42), (18, 41), (14, 40)), ('C', (10, 39), (6, 37), (6, 34)),('L',(6,14))],True)
        self.add_polyline('left-panel',(6,14),(14,18),(14,40));self.join('wall','left-panel')
        self.add_polyline('right-panel',(42,14),(34,18),(34,40));self.join('wall','right-panel')
