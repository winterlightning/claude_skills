from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0a6ea07b-96af-593d-a5c6-dbc342111877'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kidney-palette-with-three-round-wells/20260927T133723Z-thuan-mac-1/reference/color palette sample_0a6ea07b-96af-593d-a5c6-dbc342111877.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'kidney-palette-with-three-round-wells'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
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

        self.add_bezier('upper-right',(24,6),((34,6),(42,10),(42,18)))
        self.add_bezier('thumb-in',(42,18),((42,22),(36,23),(36,27)))
        self.add_bezier('thumb-out',(36,27),((36,31),(42,30),(42,34)))
        self.add_bezier('lower-right',(42,34),((42,40),(34,42),(24,42)))
        self.add_bezier('lower-left',(24,42),((12,42),(6,34),(6,24)))
        self.add_bezier('upper-left',(6,24),((6,14),(14,6),(24,6)))
        self.add_contour('palette','upper-right','thumb-in','thumb-out','lower-right','lower-left','upper-left',closed=True)

        for n,(x,y) in enumerate(((17,23),(28,18),(26,31))):circle('well-'+str(n),x,y,2)
