"""Anteater with long downturned snout and domed back; centerline extremes (2,11)-(46,37). Overlapping far legs omitted. No useful Lucide match; natural profile asymmetry retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8e192b8-9278-5d94-943f-c50ada364cfe'
SOURCE_PATH = 'pictographic-primitives/animals/anteater_b8e192b8-9278-5d94-943f-c50ada364cfe.svg'
AUTHOR = 'gpt-6'


class Anteater(Solo48):
    icon_id = 'anteater'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('anteater', 'animal', 'mammal', 'snout', 'wildlife', 'zoo', 'silhouette', 'nose')

    def build(self) -> None:
        # Anteater with long downturned snout and domed back; centerline extremes (2,11)-(46,37). Overlapping far legs omitted. No useful Lucide match; natural profile asymmetry retained.
        self.add_arc('back', (2, 30), (46, 30), radius_x=22, radius_y=19, sweep=True)
        self.add_line('rear', (46, 30), (46, 37))
        self.add_line('hind-foot-1', (46, 37), (38, 37))
        self.add_line('hind-foot-2', (38, 37), (36, 29))
        self.add_arc('belly', (36, 29), (26, 24), radius_x=13, radius_y=10, sweep=False)
        self.add_line('fore-foot-1', (26, 24), (24, 37))
        self.add_line('fore-foot-2', (24, 37), (17, 37))
        self.add_line('fore-foot-3', (17, 37), (15, 24))
        self.add_arc('snout-inner', (15, 24), (6, 33), radius_x=9, radius_y=9, sweep=False)
        self.add_arc('snout-tip', (6, 33), (2, 33), radius_x=2, radius_y=2, sweep=True)
        self.add_line('snout-front', (2, 33), (2, 30))
        self.add_contour('silhouette', 'back', 'rear', 'hind-foot-1', 'hind-foot-2', 'belly', 'fore-foot-1', 'fore-foot-2', 'fore-foot-3', 'snout-inner', 'snout-tip', 'snout-front', closed=True)
