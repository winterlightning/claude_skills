'A woman with long hair holds an open book with two rounded hand grips and a straight central fold.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/user.svg: rounded head; book-open: symmetric covers and central spine.\nOmissions: Facial marks and the fine hair part omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ed13ba86-a993-4e4d-b461-5ce413a5cd46'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/newspaper read woman_ed13ba86-a993-4e4d-b461-5ce413a5cd46.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='woman-reading-a-book'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "content"
    categories = ("primitives", "content")
    aliases=()
    keywords=('woman', 'reading', 'a', 'book')
    def build(self):

        def path(name,start,commands,closed=False):
            point=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,point,end)
                elif kind=='A': self.add_arc(member,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,point,(args[0],args[1],end))
                point=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        circle('face',24,14,8)
        for side in (-1,1):
         x=lambda d:24+side*d
         path(f'hair-{side}',(x(8),14),[('C',(x(14),28),(x(8),20),(x(14),24))]);join(f'hair-{side}','face')
        poly('book-top',(10,30),(10,28),(24,32),(38,28),(38,30))
        poly('book-bottom',(10,38),(10,40),(24,42),(38,40),(38,38))
        line('fold',(24,32),(24,42));join('fold','book-top');join('fold','book-bottom')
        for side in (-1,1):
         x=24+side*14
         path(f'hand-{side}',(x,30),[('A',(x,38),4,4,side>0)])
         join(f'hand-{side}','book-top');join(f'hand-{side}','book-bottom');join(f'hair-{side}','book-top')
