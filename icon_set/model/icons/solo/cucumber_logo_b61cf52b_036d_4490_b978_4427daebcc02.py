"""Rounded teardrop speech mark enclosing a four-stroke seed pattern; preserve downward tail and repeated short seeds; extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b61cf52b-036d-4490-b978-4427daebcc02'
SOURCE_PATH = 'pictographic-primitives/logos/cucumber io logo_b61cf52b-036d-4490-b978-4427daebcc02.svg'
AUTHOR = 'gpt-6'

class CucumberLogo(Solo48):
    icon_id = 'cucumber-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('cucumber', 'bdd', 'testing', 'logo', 'brand', 'developer', 'speech-bubble')

    def build(self):
        # Plan: Rounded teardrop speech mark enclosing a four-stroke seed pattern; preserve downward tail and repeated short seeds; extremes (8,4)-(40,44).
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

        path('bubble',(24,36),[('A',(8,20),16,16,True),('A',(40,20),16,16,True),('C',(24,44),(40,32),(30,40)),('L',(24,36))],True)
        for i,(a,b) in enumerate((((24,13),(24,14)),((24,26),(24,27)),((17,20),(18,20)),((30,20),(31,20)))): line(f'seed-{i}',a,b)
