from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a6ea07b-96af-593d-a5c6-dbc342111877'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color palette sample_0a6ea07b-96af-593d-a5c6-dbc342111877.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'kidney-palette-with-three-round-wells'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/design"
    aliases = ()
    keywords = ('palette', 'paint', 'artist', 'wells', 'color', 'art', 'kidney', 'painting')

    def build(self):
        # Plan: broad kidney silhouette; three equal circular paint wells in an offset triangle.
        # Centerline extremes: (6,6)-(42,42). Construction: Lucide palette: smooth outer contour and spaced circular wells.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        self.add_bezier('upper-left',(6,18),((6,10),(10,6),(18,6)))
        self.add_line('top',(18,6),(30,6))
        self.add_bezier('upper-right',(30,6),((38,6),(42,10),(42,18)),((42,22),(36,23),(36,27)))
        self.add_bezier('lower-right',(36,27),((36,31),(42,30),(42,34)),((42,40),(34,42),(24,42)))
        self.add_line('bottom',(24,42),(18,42))
        self.add_bezier('lower-left',(18,42),((10,42),(6,38),(6,30)))
        self.add_line('left',(6,30),(6,18))
        self.add_contour('palette','upper-left','top','upper-right','lower-right','bottom','lower-left','left',closed=True)

        for n,(x,y) in enumerate(((18,18),(30,17),(17,31))):circle('well-'+str(n),x,y,2)
