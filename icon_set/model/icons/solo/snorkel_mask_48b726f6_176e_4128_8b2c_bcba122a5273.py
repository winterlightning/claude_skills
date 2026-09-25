"""Two-lobed diving mask with a nose bridge, snorkel and round mouthpiece. Lucide rectangle-goggles informs the shared mask contour; no separate lens divider added.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48b726f6-176e-4128-8b2c-bcba122a5273'
SOURCE_PATH = 'pictographic-primitives/symbol/snorkel_48b726f6-176e-4128-8b2c-bcba122a5273.svg'
AUTHOR = 'gpt-6'


class SnorkelMask(Solo48):
    icon_id = 'snorkel-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('snorkel', 'mask', 'diving', 'swimming', 'sea', 'underwater', 'beach', 'scuba')

    def build(self) -> None:

        self.add_line('mask-top',(12,12),(26,12))
        self.add_arc('lens-right',(26,12),(26,24),radius_x=6)
        pts=[(26,24),(23,24),(20,20),(18,20),(15,24),(12,24)]
        for j,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line('nose-'+str(j),a,b)
        self.add_arc('lens-left',(12,24),(12,12),radius_x=6)
        self.add_contour('mask','mask-top','lens-right',*['nose-'+str(i) for i in range(1,6)],'lens-left',closed=True)
        self.add_line('tube-upright',(42,6),(42,29))
        self.add_arc('tube-bend',(42,29),(32,39),radius_x=10)
        self.add_line('tube-end',(32,39),(27,39))
        self.add_contour('snorkel','tube-upright','tube-bend','tube-end')
        self.add_arc('mouth-top',(21,39),(27,39),radius_x=3)
        self.add_arc('mouth-bottom',(27,39),(21,39),radius_x=3)
        self.add_contour('mouthpiece','mouth-top','mouth-bottom',closed=True)
        self.relate('connect','snorkel','mouthpiece')
