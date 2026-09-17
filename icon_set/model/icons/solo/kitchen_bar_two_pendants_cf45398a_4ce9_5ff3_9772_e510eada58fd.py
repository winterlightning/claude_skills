"""Kitchen Bar with Stools and Lights.

Kitchen counter with two hanging pendant lights and two matching pedestal stools. Centerline extremes (6,6)-(42,42). Lucide lamp-ceiling informs suspended shades. Reduce the counter to one line and stools to seat, stem and base; preserve all paired elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf45398a-4ce9-5ff3-9772-e510eada58fd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/kitchen counter_cf45398a-4ce9-5ff3-9772-e510eada58fd.svg'
AUTHOR = 'gpt-6'

class KitchenBarTwoPendants(Solo48):
    icon_id = 'kitchen-bar-two-pendants'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('kitchen', 'bar', 'with', 'stools', 'and', 'lights')

    def build(self):
        # Symbol plan: Kitchen counter with two hanging pendant lights and two matching pedestal stools. Centerline extremes (6,6)-(42,42). Lucide lamp-ceiling informs suspended shades. Reduce the counter to one line and stools to seat, stem and base; preserve all paired elements.

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
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
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

        line('counter',(6,26),(42,26))
        for i,x in enumerate((14,34)):
            line(f'cord-{i}',(x,6),(x,8))
            self.add_polyline(f'shade-{i}',(x,8),(x-6,18),(x+6,18),closed=True);join(f'cord-{i}',f'shade-{i}')
            self.add_polyline(f'seat-{i}',(x-5,34),(x,34),(x+5,34));line(f'stem-{i}',(x,34),(x,42));join(f'stem-{i}',f'seat-{i}')
            self.add_polyline(f'base-{i}',(x-4,42),(x,42),(x+4,42));join(f'stem-{i}',f'base-{i}')
