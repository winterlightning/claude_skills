"""Whole and Halved Coconut.

Whole coconut behind an open half, preserving the lower-right placement. Centerline extremes (6,6)-(42,42). Half owns an elliptical cut opening and bowl-shaped shell joined at the rim endpoints. Lucide citrus informs the cut-surface distinction; omit extra concentric rim.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56b93384-adbb-4bc0-859d-6bfa2c2ab4ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/coconut_56b93384-adbb-4bc0-859d-6bfa2c2ab4ef.svg'
AUTHOR = 'gpt-6'

class WholeAndHalvedCoconut(Solo48):
    icon_id = 'whole-and-halved-coconut'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('whole', 'and', 'halved', 'coconut')

    def build(self):
        # Symbol plan: Whole coconut behind an open half, preserving the lower-right placement. Centerline extremes (6,6)-(42,42). Half owns an elliptical cut opening and bowl-shaped shell joined at the rim endpoints. Lucide citrus informs the cut-surface distinction; omit extra concentric rim.

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

        path('whole',(10,30),[('C',(6,20),(7,28),(6,24)),('C',(20,6),(6,12),(12,6)),('C',(27,8),(23,6),(25,7))])
        path('half',(18,28),[('A',(42,28),12,10,True),('C',(30,42),(42,37),(38,42)),('C',(18,28),(22,42),(18,37))],True)
        line('cut-rim',(18,28),(42,28));join('cut-rim','half')
