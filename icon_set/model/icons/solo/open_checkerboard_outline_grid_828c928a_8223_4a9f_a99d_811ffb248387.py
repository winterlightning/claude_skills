from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '828c928a-8223-4a9f-a99d-811ffb248387'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/transparent_828c928a-8223-4a9f-a99d-811ffb248387.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'open-checkerboard-outline-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('checkerboard', 'grid', 'transparency', 'squares', 'lattice', 'pattern', 'mesh', 'design')

    def build(self):
        # Plan: four-by-four checker pattern of equal outlined cells; matching corner contacts.
        # Centerline extremes: (6,6)-(42,42). Construction: Source checkerboard reduced coherently to a 4-by-4 cell series.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        step,origin=9,6
        cells=[]
        for row in range(4):
            for col in range(4):
                if (row+col)%2:continue
                x,y=origin+col*step,origin+row*step;name=f'cell-{row}-{col}'
                points={(x,y),(x+step,y),(x+step,y+step),(x,y+step)}
                path(name,(x,y),(x+step,y),(x+step,y+step),(x,y+step),closed=True)
                for other,vertices in cells:
                    if points & vertices:join(name,other)
                cells.append((name,points))
