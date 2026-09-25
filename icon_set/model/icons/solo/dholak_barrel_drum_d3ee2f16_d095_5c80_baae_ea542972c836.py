"""One elliptical drumhead joins a mirrored tapering barrel shell. Omit the secondary close collar. Extremes (8,4)-(40,44); Lucide drum ellipse construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3ee2f16-d095-5c80-baae-ea542972c836'
SOURCE_PATH = 'pictographic-primitives/music/dholak_d3ee2f16-d095-5c80-baae-ea542972c836.svg'
AUTHOR = 'gpt-6'

class DholakBarrelDrum(Solo48):
    icon_id = 'dholak-barrel-drum'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    aliases = ()
    keywords = ('dholak', 'drum', 'barrel', 'percussion', 'indian', 'instrument', 'folk', 'music')

    def build(self):
        axis=24
        self.add_arc('head-back', (8,12), (40,12), radius_x=16, radius_y=8)
        self.add_arc('head-front', (40,12), (8,12), radius_x=16, radius_y=8)
        self.add_contour('head', 'head-back', 'head-front', closed=True)
        self.add_bezier('shell', (8,12), ((8,22),(10,32),(14,40)), ((16,44),(20,44),(24,44)), ((28,44),(32,44),(34,40)), ((38,32),(40,22),(40,12)))
        self.relate('connect','head','shell')
