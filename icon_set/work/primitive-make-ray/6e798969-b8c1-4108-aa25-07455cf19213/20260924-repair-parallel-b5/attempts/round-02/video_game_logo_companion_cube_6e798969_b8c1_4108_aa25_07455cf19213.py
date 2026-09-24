"""video game logo companion cube. Plan: Four mirrored corner blocks connected by straight rails; drop narrow connector sleeves and medallion ring while retaining central heart. Raise tip to give bottom rail8-unit clearance.
Keyshape SQUARE; shared parameters own repeated elements and genuine junctions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6e798969-b8c1-4108-aa25-07455cf19213'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/video game logo companion cube_6e798969-b8c1-4108-aa25-07455cf19213.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'video-game-logo-companion-cube'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('video', 'game', 'logo', 'companion', 'cube')
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
        for i,(x,y) in enumerate(((6,6),(34,6),(6,34),(34,34))):self.rect(f'corner-{i}',x,y,8,8,2,split_x=(10,38),split_y=(10,38))
        for name,a,b,c,d in [('top',(14,10),(34,10),'corner-0','corner-1'),('bottom',(14,38),(34,38),'corner-2','corner-3'),('left',(10,14),(10,34),'corner-0','corner-2'),('right',(38,14),(38,34),'corner-1','corner-3')]:
            self.add_line(name,a,b);self.join(name,c);self.join(name,d)
        self.path('heart',(24,30),[('L',(19,27)),('C',(15,23),(20,18),(24,22)),('C',(28,18),(33,23),(29,27)),('L',(24,30))],True)
