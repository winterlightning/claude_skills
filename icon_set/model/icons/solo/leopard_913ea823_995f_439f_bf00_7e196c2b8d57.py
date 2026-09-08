"""Simplified left-facing winged lion: one broad swept wing, one coherent feline silhouette, two visible legs and a curved tail. Removed the second wing, separate muzzle loop and feather detail. Deliberate profile asymmetry; rounded contour construction informed by Lucide cat."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '913ea823-995f-439f-bf00-7e196c2b8d57'
SOURCE_PATH = 'pictographic-primitives/animals/leopard_913ea823-995f-439f-bf00-7e196c2b8d57.svg'
AUTHOR = 'gpt-6'


class WingedLion(Solo48):
    icon_id = 'winged-lion'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('winged', 'lion', 'animal')

    def build(self) -> None:
        # SQUARE: authored to its exact SOLO48 centerline bounds.
        self.add_arc('crown', (2, 19), (8, 13), radius_x=6, radius_y=6, sweep=True)
        self.add_line('ear', (8, 13), (12, 8))
        self.add_arc('mane', (12, 8), (19, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_line('neck', (19, 18), (19, 24))
        self.add_line('wing-rise', (19, 24), (26, 10))
        self.add_line('wing-top', (26, 10), (46, 2))
        self.add_arc('wing-tip', (46, 2), (37, 27), radius_x=9, radius_y=25, sweep=True)
        self.add_arc('rump', (37, 27), (43, 34), radius_x=7, radius_y=7, sweep=True)
        self.add_line('hock', (43, 34), (45, 46))
        self.add_line('hindfoot', (45, 46), (37, 46))
        self.add_line('hindleg', (37, 46), (34, 34))
        self.add_arc('belly', (34, 34), (22, 34), radius_x=18, radius_y=18, sweep=True)
        self.add_line('foreleg', (22, 34), (18, 46))
        self.add_line('forefoot', (18, 46), (9, 46))
        self.add_line('fore-shin', (9, 46), (12, 36))
        self.add_arc('chest', (12, 36), (9, 30), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('muzzle', (9, 30), (2, 25), radius_x=7, radius_y=5, sweep=True)
        self.add_line('nose', (2, 25), (2, 19))
        self.add_contour('silhouette', 'crown', 'ear', 'mane', 'neck', 'wing-rise', 'wing-top', 'wing-tip', 'rump', 'hock', 'hindfoot', 'hindleg', 'belly', 'foreleg', 'forefoot', 'fore-shin', 'chest', 'muzzle', 'nose', closed=True)
        self.add_line('wing-base', (37, 27), (27, 27))
        self.relate("connect", 'wing-base', 'silhouette')
        self.add_arc('tail', (43, 34), (46, 25), radius_x=3, radius_y=9, sweep=False)
        self.relate("connect", 'tail', 'silhouette')
        self.add_dot('eye', (9, 21))
