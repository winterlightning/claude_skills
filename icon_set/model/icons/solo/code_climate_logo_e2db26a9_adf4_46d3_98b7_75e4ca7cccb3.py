"""Two unequal rising peaks; reduce outlined ribbons to two open strokes to retain legal spacing; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2db26a9-adf4-46d3-98b7-75e4ca7cccb3'
SOURCE_PATH = 'pictographic-primitives/logos/code climate logo_e2db26a9-adf4-46d3-98b7-75e4ca7cccb3.svg'
AUTHOR = 'gpt-6'

class CodeClimateLogo(Solo48):
    icon_id = 'code-climate-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('code-climate', 'code-quality', 'logo', 'brand', 'developer', 'analysis', 'peaks')

    def build(self):
        # Plan: Two unequal rising peaks; reduce outlined ribbons to two open strokes to retain legal spacing; extremes (4,8)-(44,40).
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

        poly('large-peak',(4,40),(20,16),(36,40))
        line('small-peak',(28,8),(44,28))
