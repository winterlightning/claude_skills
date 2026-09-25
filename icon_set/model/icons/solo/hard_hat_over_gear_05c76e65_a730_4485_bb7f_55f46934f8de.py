"""A hard hat sits directly over a lower gear. Lucide hard-hat informs the dome and ridge; settings informs repeated gear structure. Read as one integrated engineering emblem. Reduce paired ridge walls to one stroke and gear teeth to three broad projections, retaining the rounded center cutout. Mirrored about x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05c76e65-a730-4485-bb7f-55f46934f8de'
SOURCE_PATH = 'pictographic-primitives/protection/whitesource logo 1_05c76e65-a730-4485-bb7f-55f46934f8de.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'hard-hat-over-gear'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('hard hat', 'gear', 'engineering', 'maintenance', 'construction', 'safety', 'settings', 'worker')

    def build(self):
        # SQUARE centerline extremes (6, 6, 42, 42).

        # Hard hat and lower gear share a brim; teeth derive from the central axis.
        self.add_arc('dome-left',(8,20),(24,6),radius_x=16,radius_y=14)
        self.add_arc('dome-right',(24,6),(40,20),radius_x=16,radius_y=14)
        self.add_contour('dome','dome-left','dome-right')
        self.add_polyline('brim',(6,20),(8,20),(16,20),(32,20),(40,20),(42,20))
        self.relate('connect','brim','dome')
        self.add_line('ridge',(24,6),(24,12))
        self.relate('connect','ridge','dome')
        self.add_polyline('gear',(6,20),(6,28),(12,28),(16,34),(20,34),(20,42),(28,42),(28,34),(32,34),(36,28),(42,28),(42,20))
        self.relate('connect','gear','brim')
        self.add_arc('gear-center',(16,20),(32,20),radius_x=8,radius_y=10,sweep=False)
        self.relate('connect','gear-center','brim')
