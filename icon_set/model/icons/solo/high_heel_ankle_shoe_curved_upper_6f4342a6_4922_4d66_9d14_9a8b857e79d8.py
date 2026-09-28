"""High Heel Ankle Shoe.

Low ankle shoe with a curved upper, tall rear heel and rounded right toe. Centerline extremes (6,6)-(42,42). Lucide sport-shoe informs the integrated contour. Preserve the source pointed low cuff, generous arch and curved vamp; omit the tiny heel seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f4342a6-4922-4d66-9d14-9a8b857e79d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/heels ankle_6f4342a6-4922-4d66-9d14-9a8b857e79d8.svg'
AUTHOR = 'gpt-6'

class HighHeelAnkleShoeCurvedUpper(Solo48):
    icon_id = 'high-heel-ankle-shoe-curved-upper'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    categories = ('primitives', 'footwear')
    aliases = ()
    keywords = ('high', 'heel', 'ankle', 'shoe')

    def build(self):
        # Symbol plan: Low ankle shoe with a curved upper, tall rear heel and rounded right toe. Centerline extremes (6,6)-(42,42). Lucide sport-shoe informs the integrated contour. Preserve the source pointed low cuff, generous arch and curved vamp; omit the tiny heel seam.

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

        path('shoe',(10,6),[('C',(24,18),(14,14),(17,18)),('L',(27,18)),('C',(37,32),(28,24),(31,28)),('C',(42,37),(41,34),(42,35)),('C',(36,42),(42,41),(40,42)),('L',(30,42)),('C',(16,28),(24,42),(22,28)),('L',(16,42)),('L',(6,42)),('L',(6,22)),('C',(10,6),(6,16),(6,12))],True)
