"""A circular C and central X; collapse the outlined ribbons to simple strokes, retaining their intrinsic brand relationship."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c99ffdf7-3b29-430b-9d7d-5fe72ab86640'
SOURCE_PATH = 'pictographic-primitives/logos/coroflot logo_c99ffdf7-3b29-430b-9d7d-5fe72ab86640.svg'
AUTHOR = 'gpt-6'

class CoroflotLogo(Solo48):
    icon_id = 'coroflot-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('coroflot', 'design-jobs', 'logo', 'brand', 'portfolio', 'creative', 'letter-c')

    def build(self):
        # Plan: A circular C and central X; collapse the outlined ribbons to simple strokes, retaining their intrinsic brand relationship.
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
        centre=(24,24); half=6
        for i,(dx,dy) in enumerate(((-half,-half),(half,half),(-half,half),(half,-half))):
            line(f'cross-{i}',centre,(24+dx,24+dy))
        for i in range(4):
            for j in range(i): join(f'cross-{i}',f'cross-{j}')
