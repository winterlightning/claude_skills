"""One C-shaped circular stroke with two equal rings; collapse the outlined C ribbon to one stroke while preserving the open-right constellation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b735ec8-ebef-449c-bc78-315b581cb382'
SOURCE_PATH = 'pictographic-primitives/logos/consul logo_2b735ec8-ebef-449c-bc78-315b581cb382.svg'
AUTHOR = 'gpt-6'

class ConsulLogo(Solo48):
    icon_id = 'consul-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('consul', 'hashicorp', 'logo', 'brand', 'service-mesh', 'devops', 'network')

    def build(self):
        # Plan: One C-shaped circular stroke with two equal rings; collapse the outlined C ribbon to one stroke while preserving the open-right constellation.
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

        c_ring('outer-c')
        radius=3
        for i,x in enumerate((24,41)): circle(f'node-{i}',x,24,radius)
