"""Circular shell and a rounded spherical core meeting the upper-right rim at two exact nodes; omit the extra narrow lower-left highlight band."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '952a0c19-80be-4da2-a573-745cc15b18fb'
SOURCE_PATH = 'pictographic-primitives/logos/cinema 4d logo_952a0c19-80be-4da2-a573-745cc15b18fb.svg'
AUTHOR = 'gpt-6'

class Cinema4DLogo(Solo48):
    icon_id = 'cinema-4d-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('cinema-4d', 'maxon', '3d', 'logo', 'brand', 'modeling', 'animation')

    def build(self):
        # Plan: Circular shell and a rounded spherical core meeting the upper-right rim at two exact nodes; omit the extra narrow lower-left highlight band.
        # Construction reference: No useful subject match found; source brand render informs the geometry.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i, command in enumerate(commands):
                kind, end, *args=command
                part=f"{name}-{i}"
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(part,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C': self.add_bezier(part,here,(args[0],args[1],end))
                members.append(part); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def c_ring(name):
            # Exact radius-20 points on the circle about (24,24).
            self.add_arc(name,(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        poly=self.add_polyline
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        # The outer circle is split at the exact points where the core meets it.
        r=20
        path('shell',(36,8),[('A',(40,12),r,r,True),('A',(44,24),r,r,True),('A',(24,44),r,r,True),('A',(4,24),r,r,True),('A',(24,4),r,r,True),('A',(36,8),r,r,True)],True)
        path('core',(36,8),[('C',(16,18),(34,13),(18,12)),('C',(22,31),(14,23),(17,29)),('C',(32,30),(26,34),(30,34)),('C',(44,24),(36,26),(38,24))])
        join('shell','core')
