"""Three Domed Pavilions on a Wall. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1641f69e-dc85-5136-a094-91f1627b55eb'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/red fort india_1641f69e-dc85-5136-a094-91f1627b55eb.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'three-domed-pavilion-wall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('fort', 'palace', 'dome', 'pavilion', 'wall', 'landmark', 'india', 'architecture', 'heritage')

    def build(self):
        self.add_polyline('wall', (2, 46), (2, 32), (10, 32), (18, 32), (30, 32), (38, 32), (46, 32), (46, 46), closed=False)
        self.add_polyline('legs', (18, 32), (18, 46), closed=False)
        self.add_polyline('leg-right', (30, 32), (30, 46), closed=False)
        self.relate("connect", "wall", "legs")
        self.relate("connect", "wall", "leg-right")
        self.add_arc("left-dome", (2,26), (14,26), radius_x=6)
        self.add_line("left-support-1", (14, 26), (14, 32))
        self.add_line("left-support-2", (14, 32), (2, 32))
        self.add_line("left-support-3", (2, 32), (2, 26))
        self.add_contour("left-pavilion", "left-dome", "left-support-1", "left-support-2", "left-support-3", closed=True)
        self.add_arc("right-dome", (34,26), (46,26), radius_x=6)
        self.add_line("right-support-1", (46, 26), (46, 32))
        self.add_line("right-support-2", (46, 32), (34, 32))
        self.add_line("right-support-3", (34, 32), (34, 26))
        self.add_contour("right-pavilion", "right-dome", "right-support-1", "right-support-2", "right-support-3", closed=True)
        self.relate("connect", "wall", "left-pavilion")
        self.relate("connect", "wall", "right-pavilion")
        self.add_polyline('center', (18, 32), (18, 22), (24, 14), (30, 22), (30, 32), closed=False)
        self.relate("connect", "wall", "center")
        self.add_polyline('cross-stem', (24, 2), (24, 6), (24, 14), closed=False)
        self.add_polyline('cross-bar', (20, 6), (24, 6), (28, 6), closed=False)
        self.relate("connect", "cross-stem", "cross-bar")
        self.relate("connect", "cross-stem", 'center')
