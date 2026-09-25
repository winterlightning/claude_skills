"""Seated Jet Ski Rider. Seated left-facing rider with a hanging bent leg and rounded rear cowling; retain one water row and omit hull trim.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: coherent hull curves; person-standing: circular head and articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '959341bb-93a4-4207-a514-99f7bd37b9b4'
SOURCE_PATH = 'pictographic-primitives/recreation/sport jet skiing_959341bb-93a4-4207-a514-99f7bd37b9b4.svg'
AUTHOR = 'gpt-6'


class SeatedJetSkiRider(Solo48):
    icon_id = 'seated-jet-ski-rider'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    aliases = ()
    keywords = ('seated', 'jet', 'ski', 'rider')

    def build(self) -> None:
        self.add_arc('head-top', (19, 8), (23, 8), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('head-bottom', (23, 8), (19, 8), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('rider-1', (13, 23), (18, 23))
        self.add_line('rider-2', (18, 23), (23, 18))
        self.add_line('rider-3', (23, 18), (29, 25))
        self.add_line('rider-4', (29, 25), (25, 30))
        self.add_line('rider-5', (25, 30), (29, 33))
        self.add_contour('rider', 'rider-1', 'rider-2', 'rider-3', 'rider-4', 'rider-5', closed=False)
        self.add_line('deck-1', (6, 29), (13, 23))
        self.add_line('deck-2', (13, 23), (18, 23))
        self.add_contour('deck', 'deck-1', 'deck-2', closed=False)
        self.add_arc('nose', (6, 29), (6, 31), radius_x=4, radius_y=4, sweep=True)
        self.add_line('seat-1', (29, 25), (36, 25))
        self.add_arc('stern', (36, 25), (42, 31), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('craft-rear', 'seat-1', 'stern', closed=False)
        self.relate("connect", 'rider', 'deck')
        self.relate("connect", 'deck', 'nose')
        self.relate("connect", 'craft-rear', 'rider')
        self.add_arc('wave-left', (6, 40), (24, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_arc('wave-right', (24, 40), (42, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right', closed=False)
