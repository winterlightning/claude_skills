"""A small gear with rounded teeth and a central hole sits in the middle of a radial pattern. Short straight rays and separated dots surround it above, beside and below.
Lucide settings tooth construction. Four broad teeth, a center dot and four diagonal radiation marks replace the dense eight-ray ring. Mirrored geometry about both axes.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac409f41-db55-4174-adc1-189d24e36f0d'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork cog share_ac409f41-db55-4174-adc1-189d24e36f0d.svg'
AUTHOR = 'gpt-6'


class RadiatingGear(Solo48):
    icon_id = 'radiating-gear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('gear', 'cog', 'rays', 'network', 'mechanism', 'teamwork')

    def build(self) -> None:
        self.add_polyline('gear', (20, 12), (28, 12), (28, 16), (32, 16), (32, 20), (36, 20), (36, 28), (32, 28), (32, 32), (28, 32), (28, 36), (20, 36), (20, 32), (16, 32), (16, 28), (12, 28), (12, 20), (16, 20), (16, 16), (20, 16), closed=True)
        self.add_dot('gear-hub', (24, 24))
        self.add_dot('ray-0', (6, 6))
        self.add_dot('ray-1', (42, 6))
        self.add_dot('ray-2', (6, 42))
        self.add_dot('ray-3', (42, 42))
