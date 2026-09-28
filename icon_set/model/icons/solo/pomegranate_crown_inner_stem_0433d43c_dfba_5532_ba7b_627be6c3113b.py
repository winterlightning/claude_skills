"""Whole Pomegranate Fruit.

Rounded pomegranate with a pointed calyx and restrained branching interior mark. Centerline extremes (6,6)-(42,42). Mirror body and crown; branch asymmetry follows the source. Lucide apple informs fruit contour and attachment; reduce the crown to three open points to avoid narrow folded slots.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0433d43c-dfba-5532-ba7b-627be6c3113b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pomegranate_0433d43c-dfba-5532-ba7b-627be6c3113b.svg'
AUTHOR = 'gpt-6'

class PomegranateCrownInnerStem(Solo48):
    icon_id = 'pomegranate-crown-inner-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('whole', 'pomegranate', 'fruit')

    def build(self):
        # Symbol plan: Rounded pomegranate with a pointed calyx and restrained branching interior mark. Centerline extremes (6,6)-(42,42). Mirror body and crown; branch asymmetry follows the source. Lucide apple informs fruit contour and attachment; reduce the crown to three open points to avoid narrow folded slots.

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

        bilateral('fruit',(24,14),[('A',(42,28),18,14,True),('A',(24,42),18,14,True)])
        for i,x in enumerate((16,24,32)):
            line(f'crown-{i}',(24,14),(x,6));join(f'crown-{i}','fruit')
        for a,b in ((0,1),(0,2),(1,2)):join(f'crown-{a}',f'crown-{b}')
        self.add_polyline('inner-stem',(24,23),(24,29),(24,33))
        line('branch-left',(24,29),(18,26));line('branch-right',(24,29),(30,25))
        join('inner-stem','branch-left');join('inner-stem','branch-right');join('branch-left','branch-right')
