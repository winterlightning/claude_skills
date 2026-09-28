"""Zucchini Squash Vegetable.

Long curved zucchini widening to a rounded lower-right tip, with a short stalk and a lengthwise mark. Centerline extremes (6,6)-(42,42). Lucide bean informs a smooth asymmetric contour. Reduce the source surface marks to one coherent stroke and the tiny squared stalk to one line.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28444d75-a581-57f2-b0c8-ef5e7ac4bb47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/zucchini_28444d75-a581-57f2-b0c8-ef5e7ac4bb47.svg'
AUTHOR = 'gpt-6'

class ZucchiniSquashLongBody(Solo48):
    icon_id = 'zucchini-squash-long-body'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('zucchini', 'squash', 'vegetable')

    def build(self):
        # Symbol plan: Long curved zucchini widening to a rounded lower-right tip, with a short stalk and a lengthwise mark. Centerline extremes (6,6)-(42,42). Lucide bean informs a smooth asymmetric contour. Reduce the source surface marks to one coherent stroke and the tiny squared stalk to one line.

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

        path('body',(14,12),[('C',(23,18),(18,12),(20,15)),('C',(34,25),(27,22),(30,23)),('C',(42,33),(40,28),(42,29)),('C',(33,42),(42,39),(39,42)),('C',(14,29),(26,42),(19,35)),('C',(6,18),(9,24),(6,22)),('C',(14,12),(6,14),(10,12))],True)
        line('stem',(14,12),(6,6));join('stem','body')
        path('ridge',(28,31),[('L',(30,32))])
