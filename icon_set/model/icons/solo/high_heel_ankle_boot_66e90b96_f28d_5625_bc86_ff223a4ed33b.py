"""High Heel Ankle Boot.

Tall-cuffed right-facing ankle boot with block heel and a deep arch. Centerline extremes (6,6)-(42,42). One silhouette owns heel, arch and toe; Lucide sport-shoe informs coherent shoe outline, no matching local heel. No extra seams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66e90b96-f28d-5625-bc86-ff223a4ed33b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/footwear/footwear heels ankle_66e90b96-f28d-5625-bc86-ff223a4ed33b.svg'
AUTHOR = 'gpt-6'

class HighHeelAnkleBoot(Solo48):
    icon_id = 'high-heel-ankle-boot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'footwear'
    categories = ('primitives', 'footwear')
    aliases = ()
    keywords = ('high', 'heel', 'ankle', 'boot')

    def build(self):
        # Symbol plan: Tall-cuffed right-facing ankle boot with block heel and a deep arch. Centerline extremes (6,6)-(42,42). One silhouette owns heel, arch and toe; Lucide sport-shoe informs coherent shoe outline, no matching local heel. No extra seams.

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

        path('boot',(8,6),[('L',(24,6)),('L',(24,14)),('C',(34,31),(24,23),(28,29)),('C',(42,38),(40,33),(42,34)),('A',(38,42),4,4,True),('L',(30,42)),('C',(16,28),(24,42),(22,28)),('L',(16,42)),('L',(6,42)),('L',(6,26)),('C',(8,14),(6,22),(8,18)),('L',(8,6))],True)
