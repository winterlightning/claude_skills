"""A stylus and wireframe box accompany a VR headset.
Plan: Upper-left stylus and open cube lead into the lower-right headset with paired lens circles.
Keyshape SQUARE: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
References: Supplied SVG rendered and inspected. Lucide original/box.svg and atomic-debug/box.svg: coherent contours, repeated radii and explicit shared junctions, freshly authored for SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '66464e9f-35f0-4894-b4e2-7c801bd38b27'
SOURCE_PATH = 'icon_set/work/todo-references/vr video 1_66464e9f-35f0-4894-b4e2-7c801bd38b27.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'vr-video-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('vr', 'video', '1')

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

        self.add_polyline('stylus',(8,6),(14,12),(16,18),(10,16),(6,10),closed=True)
        self.add_polyline('cube-left',(6,22),(18,26),(18,36),(6,32),closed=True)
        self.add_polyline('cube-top',(24,20),(30,22),(18,26));self.join('cube-left','cube-top')
        self.add_line('cube-right',(30,22),(30,27));self.join('cube-top','cube-right')
        self.path('headset',(22,30),[('C',(22,27),(25,27),(27,30)),('L',(37,30)),('C',(39,27),(42,27),(42,30)),('L',(42,38)),('A',(38,42),4,4,True),('L',(35,42)),('C',(33,42),(34,39),(32,39)),('C',(30,39),(31,42),(29,42)),('L',(26,42)),('A',(22,38),4,4,True),('L',(22,30))],True)
        self.add_line('headset-rim',(22,33),(42,33))
        for i,x in enumerate((27,37)):self.circle(f'lens-{i}',x,37,2)
