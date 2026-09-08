"""Continuous swan silhouette with a broad hull and S neck. Bounds (2,5)-(46,43). Lucide bird informs coherent outline; omit eye. Deliberately right-facing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1c2ec12-29d4-43de-8365-abebc8b3719d'
SOURCE_PATH = 'pictographic-primitives/animals/swan_e1c2ec12-29d4-43de-8365-abebc8b3719d.svg'
AUTHOR = 'gpt-6'


class Swan(Solo48):
    icon_id = 'swan'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('swan', 'bird', 'neck', 'curve', 'pond', 'elegant', 'waterfowl', 'grace')

    def build(self) -> None:
        self.add_line('beak',(46,20),(44,15))
        self.add_arc('head-right',(44,15),(34,5),radius_x=10,sweep=False)
        self.add_arc('head-left',(34,5),(24,15),radius_x=10,sweep=False)
        self.add_arc('neck-outer',(24,15),(26,25),radius_x=14,sweep=False)
        self.add_line('neck-diagonal',(26,25),(30,30))
        self.add_arc('neck-turn',(30,30),(24,35),radius_x=4,sweep=True)
        self.add_arc('wing-top',(24,35),(14,25),radius_x=16,sweep=False)
        self.add_arc('wing-back',(14,25),(2,32),radius_x=12,radius_y=7,sweep=False)
        self.add_arc('hull-left',(2,32),(24,43),radius_x=22,radius_y=11,sweep=False)
        self.add_arc('hull-right',(24,43),(44,33),radius_x=20,radius_y=10,sweep=False)
        self.add_arc('breast',(44,33),(38,27),radius_x=15,sweep=False)
        self.add_arc('neck-inner',(38,27),(31,15),radius_x=14,sweep=True)
        self.add_arc('head-inner',(31,15),(37,15),radius_x=3,radius_y=3,sweep=True)
        self.add_arc('face',(37,15),(46,20),radius_x=8,radius_y=5,sweep=False)
        self.add_contour('outline','beak','head-right','head-left','neck-outer','neck-diagonal','neck-turn','wing-top','wing-back','hull-left','hull-right','breast','neck-inner','head-inner','face',closed=True)
