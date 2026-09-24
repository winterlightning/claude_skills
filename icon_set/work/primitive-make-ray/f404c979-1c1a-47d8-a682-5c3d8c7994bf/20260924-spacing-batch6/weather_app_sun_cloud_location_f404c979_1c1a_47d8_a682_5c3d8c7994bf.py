"""weather app sun cloud location.
Plan: Restore four sun rays with genuine shared endpoint joins to quarter-circle sun. Separate cloud and pin; omit minor pin eye. Preserve all three recognizable weather/location symbols.
Fresh SOLO48 repair. Shared human reference applies to people.
Lucide trash-2 informs simple lid and rounded bin construction where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f404c979-1c1a-47d8-a682-5c3d8c7994bf'
SOURCE_PATH='pictographic-primitives/_uncategorized_40/weather app sun cloud location_f404c979-1c1a-47d8-a682-5c3d8c7994bf.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='weather-app-sun-cloud-location'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('weather', 'app', 'sun', 'cloud', 'location')
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
        self.path('sun',(9,12),[('A',(12,9),3,3,True),('A',(15,12),3,3,True),('A',(12,15),3,3,True),('A',(9,12),3,3,True)],True)
        for n,a,b in [('west',(9,12),(6,12)),('north',(12,9),(12,6)),('east',(15,12),(18,12)),('south',(12,15),(12,18))]:
            self.add_line('ray-'+n,a,b);self.join('sun','ray-'+n)
        self.path('pin',(26,14),[('A',(42,14),8,8,True),('C',(42,20),(37,26),(34,30)),('C',(31,26),(26,20),(26,14))],True)
        self.path('cloud',(12,42),[('C',(8,42),(6,40),(6,36)),('C',(6,32),(8,30),(12,30)),('C',(12,26),(20,26),(20,32)),('C',(26,32),(26,42),(20,42)),('L',(12,42))],True)
