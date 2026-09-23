"""A game monitor showing a mouth-shaped character connects to a controller.
Plan: Upper-left screen, short stand and wire; lower-right slanted controller silhouette.
Keyshape SQUARE: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
References: Supplied SVG rendered and inspected. Lucide original/gamepad-2.svg and atomic-debug/gamepad-2.svg: coherent contours, repeated radii and explicit shared junctions, freshly authored for SOLO48. Lucide original/video.svg and atomic-debug/video.svg: coherent contours, repeated radii and explicit shared junctions, freshly authored for SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '861e17b0-a761-4ce1-aadb-ee4995755d3f'
SOURCE_PATH = 'icon_set/work/todo-references/video game controller monitor_861e17b0-a761-4ce1-aadb-ee4995755d3f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'video-game-controller-monitor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('video', 'game', 'controller', 'monitor')

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

        self.rect('monitor',6,6,28,20,3,split_x=(20,))
        self.add_line('stand',(20,26),(20,30));self.add_polyline('stand-foot',(16,30),(20,30),(24,30));self.join('monitor','stand');self.join('stand','stand-foot')
        self.add_arc('character',(19,11),(19,21),radius_x=6,large_arc=True,sweep=False)
        self.add_polyline('mouth',(19,11),(15,16),(19,21));self.join('character','mouth');self.add_dot('pellet',(25,16))
        self.add_bezier('cable',(34,20),((40,20),(40,26),(36,28)));self.join('monitor','cable')
        self.path('controller',(23,33),[('L',(35,28)),('C',(39,26),(42,30),(42,33)),('C',(42,38),(38,39),(35,37)),('L',(28,40)),('C',(24,44),(19,42),(19,38)),('C',(19,36),(20,34),(23,33))],True)
