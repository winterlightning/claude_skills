"""An angular gear with seven regularly spaced trapezoidal teeth, matching the reference. Bounds (6,6)-(42,42). A shared seven-tooth radial definition owns all repeated corners.
Construction reference: Lucide settings: repeated radial tooth construction; original seven angular teeth preserved.
Omissions: Subpixel center speck omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ce3c661-d221-45e9-90b3-0342f52ed76e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_8ce3c661-d221-45e9-90b3-0342f52ed76e.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='angular-gear'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/interface-essential"
    aliases=()
    keywords=('cog',)
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        import math
        count=7; points=[]
        for i in range(count):
         center=-90+i*360/count
         for delta,radius in [(-20,15),(-8,20),(8,20),(20,15)]:
          a=math.radians(center+delta);points.append((radius*math.cos(a),radius*math.sin(a)))
        x0=min(x for x,y in points);x1=max(x for x,y in points)
        y0=min(y for x,y in points);y1=max(y for x,y in points)
        vertices=[(6+round(36*(x-x0)/(x1-x0)),6+round(36*(y-y0)/(y1-y0))) for x,y in points]
        poly('gear',*vertices,closed=True)
