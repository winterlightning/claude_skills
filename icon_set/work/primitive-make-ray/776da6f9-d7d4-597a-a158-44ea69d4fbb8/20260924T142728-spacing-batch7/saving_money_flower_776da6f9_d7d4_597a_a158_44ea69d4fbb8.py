"""saving money flower.
Plan: Large upper coin with dollar S and short terminal ticks; mirrored open leaf strokes converge on the plant stem.
Construction: Lucide dollar-sign and sprout; dollar ticks share actual S endpoints, leaves share stem base.
Omissions: Dollar central bar interrupted through S to avoid tiny enclosed holes; closed leaf outlines simplified to open diagonal strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '776da6f9-d7d4-597a-a158-44ea69d4fbb8'
SOURCE_PATH = 'pictographic-primitives/finance/saving money flower_776da6f9-d7d4-597a-a158-44ea69d4fbb8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'saving-money-flower'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('saving', 'money', 'flower')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)
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
        self.path('coin',(24,4),[('A',(24,32),14,14,True),('A',(24,4),14,14,True)],True)
        self.path('dollar',(26,14),[('L',(24,14)),('C',(19,14),(19,18),(24,18)),('C',(29,18),(29,22),(24,22)),('L',(22,22))])
        self.add_line('dollar-top',(24,13),(24,14));self.relate('connect','dollar','dollar-top')
        self.add_line('dollar-bottom',(24,22),(24,23));self.relate('connect','dollar','dollar-bottom')
        self.add_line('stem',(24,32),(24,44));self.relate('connect','coin','stem')
        self.add_polyline('leaves',(8,35),(24,44),(40,35))
        self.relate('connect','stem','leaves')
