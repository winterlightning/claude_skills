"""Bedside Nightstand with Drawer.

Nightstand with rounded top, central drawer pull, lower divider and two straight legs. Centerline extremes (6,6)-(42,42). Rounded rectangle divided at shared endpoints; no useful local Lucide nightstand match. Keep the broad single drawer rather than a double cabinet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85ea0c15-c53c-458c-8c59-f9c710664f34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/furniture_85ea0c15-c53c-458c-8c59-f9c710664f34.svg'
AUTHOR = 'gpt-6'

class NightstandCentralDrawer(Solo48):
    icon_id = 'nightstand-central-drawer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('bedside', 'nightstand', 'with', 'drawer')

    def build(self):
        # Symbol plan: Nightstand with rounded top, central drawer pull, lower divider and two straight legs. Centerline extremes (6,6)-(42,42). Rounded rectangle divided at shared endpoints; no useful local Lucide nightstand match. Keep the broad single drawer rather than a double cabinet.

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

        path('frame',(6,42),[('L',(6,32)),('L',(6,14)),('L',(6,10)),('A',(10,6),4,4,True),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,14)),('L',(42,32)),('L',(42,42))])
        for n,y in [('top',14),('bottom',32)]:line(n,(6,y),(42,y));join(n,'frame')
        line('pull',(22,23),(26,23))
