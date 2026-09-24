"""video game 360 vr.
Plan: Full-height 360 with narrowed three, eight-unit six internal run, rounded open band sides and enlarged upward-facing game mouth. Band rim omitted where symbols need clearance.
Fresh SOLO48 repair. Shared human reference applies to people.
Lucide trash-2 informs simple lid and rounded bin construction where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c710459a-2d6e-4c8e-89da-f6b82e663367'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/video game 360 vr_c710459a-2d6e-4c8e-89da-f6b82e663367.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='video-game-360-vr'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('video', 'game', '360', 'vr')
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
        self.add_polyline('three',(6,6),(10,6),(10,14),(6,14))
        self.add_polyline('three-bottom',(10,14),(10,22),(6,22));self.join('three','three-bottom')
        self.circle('six-loop',22,18,4);self.add_polyline('six-stem',(18,18),(18,6),(26,6));self.join('six-loop','six-stem')
        self.path('zero',(34,10),[('A',(42,10),4,4,True),('L',(42,18)),('A',(34,18),4,4,True),('L',(34,10))],True)
        self.path('band-left',(10,30),[('A',(6,34),4,4,False),('L',(6,38)),('A',(10,42),4,4,False)])
        self.path('band-right',(38,30),[('A',(42,34),4,4,True),('L',(42,38)),('A',(38,42),4,4,True)])
        self.add_arc('game-arc',(24,30),(30,36),radius_x=6,large_arc=True,sweep=False)
        self.add_polyline('game-mouth',(30,36),(24,36),(24,30));self.join('game-arc','game-mouth')
