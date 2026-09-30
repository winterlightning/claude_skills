"""Whole and Halved Passion Fruit.

Whole passion fruit behind a front-left cut half with two visible seeds. Centerline extremes (6,6)-(42,42). Lucide citrus informs clear separation of whole and cut fruit; remove the tiny scalloped flesh and doubled rim.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '468502b8-d856-4658-a768-bafd5faaf824'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/exotic food passion fruit_468502b8-d856-4658-a768-bafd5faaf824.svg'
AUTHOR = 'gpt-6'

class WholeAndHalvedPassionFruit(Solo48):
    icon_id = 'whole-and-halved-passion-fruit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'and', 'halved', 'passion', 'fruit')

    def build(self):
        # Symbol plan: Whole passion fruit behind a front-left cut half with two visible seeds. Centerline extremes (6,6)-(42,42). Lucide citrus informs clear separation of whole and cut fruit; remove the tiny scalloped flesh and doubled rim.

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

        path('whole',(22,8),[('C',(28,6),(24,6),(26,6)),('C',(42,20),(36,6),(42,12)),('C',(40,28),(42,23),(41,26))])
        oval('cut-face',19,30,13,12)
        for i,(x,y) in enumerate(((15,29),(23,31))): dot(f'seed-{i}',(x,y))
