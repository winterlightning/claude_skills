'A leaping dolphin with an enlarged tail fluke. SQUARE extremes (6,6)-(42,42) retain the original pose. Tail area expands into the lower negative space; no identity detail removed. No useful local Lucide dolphin match; directional asymmetry is intentional.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c0fe22a4-31db-554f-b6d7-6ce3be390288'
SOURCE_PATH = 'pictographic-primitives/animals/dolphin_c0fe22a4-31db-554f-b6d7-6ce3be390288.svg'
AUTHOR = 'gpt-6'

class LeapingDolphin(Solo48):
    icon_id = 'leaping-dolphin'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('dolphin', 'leap', 'jump', 'sea', 'marine', 'ocean', 'mammal', 'swim')

    def build(self):
        self.add_bezier('silhouette-1', (6, 36), *(((6, 32.28718708), (6, 27.71281292), (6, 24)),))
        self.add_bezier('silhouette-2', (6, 24), *(((6, 15.90815969), (11.64319416, 8.79622956), (20, 7)),))
        self.add_line('silhouette-3', (20, 7), (17, 6))
        self.add_bezier('silhouette-4', (17, 6), *(((21.1097623, 6), (25.38365041, 6), (29, 8)),))
        self.add_arc('silhouette-5', (29, 8), (42, 19), radius_x=22, radius_y=22, sweep=True)
        self.add_bezier('silhouette-6', (42, 19), *(((42, 21.47520861), (42, 24.52479139), (42, 27)),))
        self.add_arc('silhouette-7', (42, 27), (40, 27), radius_x=5, radius_y=5, sweep=True)
        self.add_line('silhouette-8', (40, 27), (33, 22))
        self.add_arc('silhouette-9', (33, 22), (24, 27), radius_x=10, radius_y=10, sweep=True)
        self.add_line('silhouette-10', (24, 27), (26, 19))
        self.add_arc('silhouette-11', (26, 19), (9, 34), radius_x=17, radius_y=17, sweep=False)
        self.add_arc('silhouette-12', (9, 34), (24, 40), radius_x=18, radius_y=16, sweep=True)
        self.add_line('silhouette-13', (24, 40), (12, 42))
        self.add_line('silhouette-14', (12, 42), (6, 42))
        self.add_line('silhouette-15', (6, 42), (6, 36))
        self.add_contour('silhouette', 'silhouette-1', 'silhouette-2', 'silhouette-3', 'silhouette-4', 'silhouette-5', 'silhouette-6', 'silhouette-7', 'silhouette-8', 'silhouette-9', 'silhouette-10', 'silhouette-11', 'silhouette-12', 'silhouette-13', 'silhouette-14', 'silhouette-15', closed=True)
