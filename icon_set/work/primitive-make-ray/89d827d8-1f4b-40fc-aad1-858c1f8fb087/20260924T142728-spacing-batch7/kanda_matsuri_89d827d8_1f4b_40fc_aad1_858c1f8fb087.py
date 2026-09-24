"""kanda matsuri.
Plan: One downward heart above two inward-facing hearts, with three lower festival tassels. Lower hearts share mirrored geometry.
Construction: No useful exact Lucide match for this motif; source supplies three-heart arrangement and tassels, smooth lobes use circular arcs.
Omissions: Outer medallion ring and radial suspension strokes omitted to reserve space for the three defining heart shapes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '89d827d8-1f4b-40fc-aad1-858c1f8fb087'
SOURCE_PATH = 'pictographic-primitives/holidays/kanda matsuri_89d827d8-1f4b-40fc-aad1-858c1f8fb087.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'kanda-matsuri'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('kanda', 'matsuri')
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
        # Top heart and mirrored, inward-pointing lower hearts preserve the three-heart festival motif.
        self.path('heart-top',(24,7),[('A',(30,7),3,3,True),('C',(30,11),(27,14),(24,16)),('C',(21,14),(18,11),(18,7)),('A',(24,7),3,3,True)],True)
        self.path('heart-left',(11,28),[('A',(11,22),3,3,True),('C',(15,22),(18,25),(20,28)),('C',(18,31),(15,34),(11,34)),('A',(11,28),3,3,True)],True)
        self.path('heart-right',(37,28),[('A',(37,22),3,3,False),('C',(33,22),(30,25),(28,28)),('C',(30,31),(33,34),(37,34)),('A',(37,28),3,3,False)],True)
        self.add_line('tassel-left',(8,42),(10,44));self.add_line('tassel-right',(40,42),(38,44));self.add_dot('tassel-center',(24,44))
