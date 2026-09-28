from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1dcbc13f-91d1-5ef7-8094-46fff023b679'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/color painting palette_1dcbc13f-91d1-5ef7-8094-46fff023b679.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'kidney-palette-with-four-round-wells'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('palette', 'artist', 'paint', 'color', 'wells', 'art', 'painting', 'kidney')

    def build(self):
        # Plan: kidney silhouette with four evenly readable round paint spots.
        # Centerline extremes: (6,6)-(42,42). Construction: Lucide palette: filled circular paint spots retain count with open spacing.
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

        for n,(x,y) in enumerate(((18,17),(30,16),(16,27),(22,33))):self.add_dot('well-'+str(n),(x,y))
