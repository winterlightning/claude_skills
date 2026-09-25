"""A regular three-ring column and two unequal horizontal bars; collapse capsules to round-capped strokes; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de32221d-3ae3-4517-b767-d8728cf1083f'
SOURCE_PATH = 'pictographic-primitives/logos/codefactor logo_de32221d-3ae3-4517-b767-d8728cf1083f.svg'
AUTHOR = 'gpt-6'

class CodefactorLogo(Solo48):
    icon_id = 'codefactor-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('codefactor', 'code-review', 'logo', 'brand', 'developer', 'list', 'quality')

    def build(self):
        # Plan: A regular three-ring column and two unequal horizontal bars; collapse capsules to round-capped strokes; extremes (6,6)-(42,42).
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

        radius=3; x=9; first_y=9; step=15
        for i in range(3): circle(f'bullet-{i}',x,first_y+i*step,radius)
        line('long-bar',(23,9),(42,9))
        line('short-bar',(23,24),(34,24))
