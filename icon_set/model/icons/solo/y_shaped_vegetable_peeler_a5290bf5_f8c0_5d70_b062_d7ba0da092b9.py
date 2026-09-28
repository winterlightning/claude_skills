"""Y Shaped Vegetable Peeler.

Y-shaped peeler with a broad U head, a crosswise blade and a narrow rounded handle. Centerline extremes (8,4)-(40,44). Mirror arms about x=24 and split them at blade endpoints. No useful local Lucide peeler match; remove the duplicated upper border.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5290bf5-f8c0-5d70-b062-d7ba0da092b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/peeler_a5290bf5-f8c0-5d70-b062-d7ba0da092b9.svg'
AUTHOR = 'gpt-6'

class YShapedVegetablePeeler(Solo48):
    icon_id = 'y-shaped-vegetable-peeler'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('y', 'shaped', 'vegetable', 'peeler')

    def build(self):
        # Symbol plan: Y-shaped peeler with a broad U head, a crosswise blade and a narrow rounded handle. Centerline extremes (8,4)-(40,44). Mirror arms about x=24 and split them at blade endpoints. No useful local Lucide peeler match; remove the duplicated upper border.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def bilateral(name, start, right, closed=True):
            # One half owns geometry; mirror and reverse it about the shared axis.
            axis=24
            mirror=lambda p:(2*axis-p[0],p[1])
            segments=[]
            here=start
            for kind,end,*args in right:
                segments.append((kind,here,end,args));here=end
            left=[]
            for kind,begin,end,args in reversed(segments):
                if kind=='C': left.append((kind,mirror(begin),mirror(args[1]),mirror(args[0])))
                elif kind=='A': left.append((kind,mirror(begin),*args))
                else:left.append((kind,mirror(begin)))
            if closed:path(name,start,right+left,True)
            else:path(name,mirror(here),left+right)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        bilateral('frame',(24,44),[('A',(28,40),4,4,False),('L',(28,28)),('C',(40,16),(28,22),(40,24)),('L',(40,12)),('L',(40,4))],False)
        line('blade',(8,12),(40,12));join('blade','frame')
