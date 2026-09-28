"""A person rests their arms on a fence with their legs visible beneath the rails.

Construction: person-standing: head and simplified body; fence: repeated rails and shared post junctions.
Reduction: Reduced three rails to two, with the torso hidden by the fence. Mirrored around x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e29076a9-17a4-5730-a4ab-bc97eb440b98'
SOURCE_PATH = 'pictographic-primitives/travel/refugee immigration fence_e29076a9-17a4-5730-a4ab-bc97eb440b98.svg'
AUTHOR = 'gpt-6'


class PersonBehindFence(Solo48):
    icon_id = 'person-behind-fence'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "primitives")
    aliases = ()
    keywords = ('refugee', 'immigration', 'fence', 'border', 'person', 'barrier', 'waiting')

    def build(self) -> None:
        # SQUARE extremes (6,6)-(42,42); head bottom12 to shoulders top21 leaves9.
        self.add_arc('head-right',(24,6),(24,12),radius_x=3)
        self.add_arc('head-left',(24,12),(24,6),radius_x=3)
        self.add_contour('head','head-right','head-left',closed=True)
        self.add_arc('shoulders',(14,29),(34,29),radius_x=10,radius_y=8)
        for n,x in enumerate((6,42)):
         self.add_polyline(f'post-{n}',(x,25),(x,29),(x,37),(x,42))
        self.add_polyline('top-rail',(6,29),(14,29),(34,29),(42,29))
        self.add_polyline('lower-rail',(6,37),(20,37),(28,37),(42,37))
        for rail in ('top-rail','lower-rail'):
         for n in range(2):self.relate('connect',rail,f'post-{n}')
        self.relate('connect','shoulders','top-rail')
        self.add_line('leg-left',(20,37),(18,42))
        self.add_line('leg-right',(28,37),(30,42))
        self.relate('connect','leg-left','lower-rail')
        self.relate('connect','leg-right','lower-rail')
