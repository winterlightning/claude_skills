"""Lucide square-pen: open page contour and diagonal pencil; cap seam omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c42c4e8e-4653-4686-a5ee-3d71cfbfbd10'
SOURCE_PATH = 'pictographic-primitives/school-learning/drawing_c42c4e8e-4653-4686-a5ee-3d71cfbfbd10.svg'
AUTHOR = 'gpt-6'


class PencilDrawingOnPaper(Solo48):
    icon_id = 'pencil-drawing-on-paper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('pencil', 'paper', 'drawing', 'writing', 'sketch', 'stationery')

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def bust(self, name, x, y, r=2, width=5):
        self.circle(name+'-head',x,y,r)
        self.add_arc(name+'-sl',(x-width,y+7),(x,y+r),radius_x=width,radius_y=7-r)
        self.add_arc(name+'-sr',(x,y+r),(x+width,y+7),radius_x=width,radius_y=7-r)
        self.add_contour(name+'-shoulders',name+'-sl',name+'-sr')
        self.relate('connect',name+'-head',name+'-shoulders')

    def build(self) -> None:
        # Bounds are derived from the live SOLO48 contract, not the stale skill table.

        self.add_polyline('paper',(23,6),(6,6),(6,42),(42,42),(42,26))
        self.add_polyline('pencil',(19,29),(22,20),(36,6),(42,12),(28,26),(19,29))
