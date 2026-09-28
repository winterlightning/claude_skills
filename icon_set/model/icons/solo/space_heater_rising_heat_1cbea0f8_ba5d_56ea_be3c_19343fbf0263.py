"""Electric Space Heater with Heat Waves.

Low heater with three bars and three separate rising heat waves. Centerline extremes (6,6)-(42,42). Lucide heater informs the waves and rounded case. Bars connect to the case bottom to keep all three readable; retain both feet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cbea0f8-ba5d-56ea-be3c-19343fbf0263'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/heater_1cbea0f8-ba5d-56ea-be3c-19343fbf0263.svg'
AUTHOR = 'gpt-6'

class SpaceHeaterRisingHeat(Solo48):
    icon_id = 'space-heater-rising-heat'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases = ()
    keywords = ('electric', 'space', 'heater', 'with', 'heat', 'waves')

    def build(self):
        # Symbol plan: Low heater with three bars and three separate rising heat waves. Centerline extremes (6,6)-(42,42). Lucide heater informs the waves and rounded case. Bars connect to the case bottom to keep all three readable; retain both feet.

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

        path('case',(10,24),[('L',(38,24)),('A',(42,28),4,4,True),('L',(42,34)),('A',(38,38),4,4,True),('L',(34,38)),('L',(24,38)),('L',(14,38)),('L',(10,38)),('A',(6,34),4,4,True),('L',(6,28)),('A',(10,24),4,4,True)],True)
        for x in (14,24,34):line(f'bar-{x}',(x,32),(x,38));join(f'bar-{x}','case')
        for x in (14,34):line(f'foot-{x}',(x,38),(x,42));join(f'foot-{x}','case')
        for i,x in enumerate((14,24,34)):path(f'heat-{i}',(x,6),[('C',(x,16),(x+4,10),(x-4,12))])
