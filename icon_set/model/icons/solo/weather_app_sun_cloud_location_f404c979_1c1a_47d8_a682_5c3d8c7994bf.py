"""weather app sun cloud location.
Plan: Exposed sun cap above left cloud; large pin overlays lower-right and shares a genuine cloud endpoint.
Construction: Source sun/cloud/pin arrangement, circular sun cap and smooth coherent cloud boundary.
Omissions: Sun rays removed; location center ring reduced to a dot.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = 'f404c979-1c1a-47d8-a682-5c3d8c7994bf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/weather app sun cloud location_f404c979-1c1a-47d8-a682-5c3d8c7994bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'weather-app-sun-cloud-location'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('weather', 'app', 'sun', 'cloud', 'location')
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
        self.add_arc('sun',(6,13),(20,13),radius_x=7)
        self.path('cloud',(16,42),[('L',(14,42)),('A',(6,34),8,8,True),('A',(14,26),8,8,True),('C',(14,19),(15,13),(20,13)),('C',(25,13),(29,14),(32,18))])
        self.relate('connect','sun','cloud')
        self.path('pin',(32,18),[('A',(42,28),10,10,True),('C',(42,33),(36,39),(32,42)),('C',(28,39),(22,33),(22,28)),('A',(32,18),10,10,True)],True)
        self.relate('connect','cloud','pin')
        self.add_dot('pin-center',(32,28))
