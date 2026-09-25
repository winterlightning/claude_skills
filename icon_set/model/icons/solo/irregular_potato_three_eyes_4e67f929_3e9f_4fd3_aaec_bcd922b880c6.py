"""Whole Raw Potato.

Uneven raw potato with an indented right shoulder and three scattered eyes. Centerline extremes (6,6)-(42,42). Use a few coherent curves and intentionally uneven eye positions; no useful Lucide potato match and no marks omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e67f929-3e9f-4fd3-aaec-bcd922b880c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/painting_4e67f929-3e9f-4fd3-aaec-bcd922b880c6.svg'
AUTHOR = 'gpt-6'

class IrregularPotatoThreeEyes(Solo48):
    icon_id = 'irregular-potato-three-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('food', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('whole', 'raw', 'potato')

    def build(self):
        # Symbol plan: Uneven raw potato with an indented right shoulder and three scattered eyes. Centerline extremes (6,6)-(42,42). Use a few coherent curves and intentionally uneven eye positions; no useful Lucide potato match and no marks omitted.

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

        path('potato',(24,6),[('C',(42,16),(34,6),(42,10)),('C',(36,27),(42,22),(36,23)),('C',(34,38),(36,32),(38,35)),('C',(22,42),(31,41),(27,42)),('C',(6,28),(12,42),(6,36)),('C',(24,6),(6,16),(14,6))],True)
        for i,p in enumerate(((18,17),(31,18),(20,32))): dot(f'eye-{i}',p)
