"""pen tools.
Plan: Bezier control nodes and arch above a large pointed fountain nib with central slit.
Construction: Lucide pen-tool pointed nib and slit, source control-node arrangement.
Omissions: Nib hole merged into slit; separate base band omitted to enlarge nib interior.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e4b8631c-5185-5ace-a823-05b73325753b'
SOURCE_PATH = 'pictographic-primitives/design/pen tools_e4b8631c-5185-5ace-a823-05b73325753b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pen-tools'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('pen', 'tools')
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
        self.circle('left-node',8,8,2);self.circle('right-node',40,8,2)
        self.add_polyline('control-square',(20,6),(28,6),(28,8),(28,10),(28,14),(20,14),(20,10),(20,8),closed=True)
        self.add_line('left-control',(10,8),(20,8));self.relate('connect','left-control','left-node');self.relate('connect','left-control','control-square')
        self.add_line('right-control',(28,8),(38,8));self.relate('connect','right-control','right-node');self.relate('connect','right-control','control-square')
        self.add_arc('curve-left',(8,24),(20,10),radius_x=16,radius_y=16)
        self.add_arc('curve-right',(28,10),(40,24),radius_x=16,radius_y=16)
        self.relate('connect','curve-left','control-square');self.relate('connect','curve-right','control-square')
        self.add_polyline('nib',(24,23),(12,34),(18,42),(30,42),(36,34),closed=True)
        self.add_line('slit',(24,23),(24,31));self.relate('connect','slit','nib')
