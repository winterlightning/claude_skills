"""The CodePen open wireframe hexagon with a central diamond; omit the generic outer roundel so the identifying cage remains readable at 48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ccee7312-ac65-4eca-9d55-0f9edcb733e0'
SOURCE_PATH = 'pictographic-primitives/logos/codepen logo_ccee7312-ac65-4eca-9d55-0f9edcb733e0.svg'
AUTHOR = 'gpt-6'

class CodepenLogo(Solo48):
    icon_id = 'codepen-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('codepen', 'cube', 'logo', 'brand', 'developer', 'editor', 'frontend')

    def build(self):
        # Plan: The CodePen open wireframe hexagon with a central diamond; omit the generic outer roundel so the identifying cage remains readable at 48.
        # Construction reference: Lucide box: broad faces and common seam nodes.

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

        poly('outline',(24,6),(42,18),(42,30),(24,42),(6,30),(6,18),closed=True)
        poly('diamond',(6,30),(15,24),(24,18),(33,24),(42,30))
        poly('rear',(6,18),(15,24),(24,30),(33,24),(42,18))
        line('top-post',(24,6),(24,18));line('bottom-post',(24,30),(24,42))
        for a,b in [('outline','diamond'),('outline','rear'),('diamond','rear'),('top-post','outline'),('top-post','diamond'),('bottom-post','outline'),('bottom-post','rear')]: join(a,b)
