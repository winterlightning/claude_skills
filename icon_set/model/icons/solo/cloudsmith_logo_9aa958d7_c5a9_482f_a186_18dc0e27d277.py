"""One smooth diagonal double-lobed contour plus a detached lower-right ring; elliptical upper lobe and round lower lobe joined by a broad diagonal neck; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9aa958d7-c5a9-482f-a186-18dc0e27d277'
SOURCE_PATH = 'pictographic-primitives/logos/cloudsmith logo_9aa958d7-c5a9-482f-a186-18dc0e27d277.svg'
AUTHOR = 'gpt-6'

class CloudsmithLogo(Solo48):
    icon_id = 'cloudsmith-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('cloudsmith', 'package', 'logo', 'brand', 'devops', 'repository', 'cloud')

    def build(self):
        # Plan: One smooth diagonal double-lobed contour plus a detached lower-right ring; elliptical upper lobe and round lower lobe joined by a broad diagonal neck; extremes (6,6)-(42,42).
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

        path('lobes',(14,20),[('C',(32,6),(24,20),(22,6)),('A',(42,14),10,8,True),('A',(32,22),10,8,True),('C',(14,36),(22,22),(24,36)),('A',(6,28),8,8,True),('A',(14,20),8,8,True)],True)
        circle('satellite',38,38,4)
