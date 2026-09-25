"""A conical flask hangs from a neck clamp attached to a tall stand on its right. A wavy liquid surface crosses the flask body, and a teardrop-shaped flame appears immediately above the neck.

SQUARE visible bounds (4,4)-(44,44); flask clamped to a right stand, pointed flame above the mouth. Liquid wave omitted for clearance. Lucide flask-conical construction from earlier batches informs the vessel; asymmetry retains the stand location.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c60e7add-c7b3-4b65-8c5f-9c9d60df12dc'
SOURCE_PATH = 'pictographic-primitives/science/lab flame experiment_c60e7add-c7b3-4b65-8c5f-9c9d60df12dc.svg'
AUTHOR = 'gpt-6'

class FlaskOnLaboratoryStand(Solo48):
    icon_id = 'flask-on-laboratory-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('flask', 'stand', 'clamp', 'laboratory', 'flame', 'experiment')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('stand',(38,6),(38,28),(38,42))
        self.add_line('clamp',(26,28),(38,28));self.add_line('clamp-end',(38,28),(42,28))
        self.relate('connect','stand','clamp');self.relate('connect','stand','clamp-end');self.relate('connect','clamp','clamp-end')
        self.segments('neck-left',(14,28),(14,31),(6,39))
        self.add_arc('bowl-left',(6,39),(9,42),radius_x=3,sweep=False)
        self.add_line('bottom',(9,42),(29,42))
        self.add_arc('bowl-right',(29,42),(32,39),radius_x=3,sweep=False)
        self.segments('neck-right',(32,39),(26,31),(26,28),(14,28))
        self.add_contour('flask','neck-left-1','neck-left-2','bowl-left','bottom','bowl-right','neck-right-1','neck-right-2','neck-right-3',closed=True)
        self.relate('connect','flask','clamp')
        self.add_arc('flame-rise-right',(20,6),(26,13),radius_x=10)
        self.add_arc('flame-bottom-right',(26,13),(20,19),radius_x=6)
        self.add_arc('flame-bottom-left',(20,19),(14,13),radius_x=6)
        self.add_arc('flame-rise-left',(14,13),(20,6),radius_x=10)
        self.add_contour('flame','flame-rise-right','flame-bottom-right','flame-bottom-left','flame-rise-left',closed=True)
