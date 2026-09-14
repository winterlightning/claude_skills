"""A large tilted satellite dish rises on a support above a low building with a rectangular doorway. Its feed projects across the bowl, while a smaller adjoining section carries two short rooftop antennas.

SQUARE visible bounds (4,4)-(44,44); tilted dish with feed, main building and adjoining antenna section; one crowded antenna omitted. Lucide satellite-dish informed its bowl and feed; asymmetry preserves the installation arrangement.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e308e971-c7ef-4df9-9951-bf9a96a6397f'
SOURCE_PATH = 'pictographic-primitives/science/science_e308e971-c7ef-4df9-9951-bf9a96a6397f.svg'
AUTHOR = 'gpt-6'

class SatelliteGroundStation(Solo48):
    icon_id = 'satellite-ground-station-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('satellite', 'dish', 'station', 'antenna', 'building', 'communication')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('dish-upper',(14,6),(10,14),radius_x=10,sweep=False)
        self.add_arc('dish-lower',(10,14),(20,24),radius_x=10,sweep=False)
        self.add_arc('dish-end',(20,24),(26,22),radius_x=10,sweep=False)
        self.segments('dish-rim',(26,22),(20,14),(14,6))
        self.add_contour('dish','dish-upper','dish-lower','dish-end','dish-rim-1','dish-rim-2',closed=True)
        self.add_line('feed',(20,14),(28,6));self.relate('connect','feed','dish')
        self.add_line('mast',(20,24),(20,26));self.relate('connect','mast','dish')
        self.add_polyline('building',(6,42),(6,26),(20,26),(30,26),(30,34),(38,34),(42,34),(42,42),(22,42),(14,42),closed=True)
        self.relate('connect','mast','building')
        self.add_polyline('door',(14,42),(14,34),(22,34),(22,42));self.relate('connect','door','building')
        self.add_line('antenna-two',(42,34),(42,22))
        self.relate('connect','antenna-two','building')
