"""High Heel Shoe.

Low-backed high heel with steep sloping vamp and thin block heel. Centerline extremes (4,8)-(44,40). Lucide sport-shoe informs the simple directional silhouette. Keep this shoe lower and longer than both ankle styles; omit heel seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5072748-24c2-50f4-9bdc-ae3f524c3ea3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/heels_a5072748-24c2-50f4-9bdc-ae3f524c3ea3.svg'
AUTHOR = 'gpt-6'

class HighHeelShoeSteepArch(Solo48):
    icon_id = 'high-heel-shoe-steep-arch'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    aliases = ()
    keywords = ('high', 'heel', 'shoe')

    def build(self):
        # Symbol plan: Low-backed high heel with steep sloping vamp and thin block heel. Centerline extremes (4,8)-(44,40). Lucide sport-shoe informs the simple directional silhouette. Keep this shoe lower and longer than both ankle styles; omit heel seam.

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

        path('shoe',(6,8),[('C',(18,16),(12,8),(15,10)),('L',(28,28)),('C',(36,30),(30,30),(32,30)),('C',(44,36),(41,31),(44,32)),('C',(40,40),(44,39),(43,40)),('L',(28,40)),('C',(14,28),(23,40),(19,28)),('L',(14,40)),('L',(4,40)),('L',(4,22)),('C',(6,8),(4,17),(4,12))],True)
