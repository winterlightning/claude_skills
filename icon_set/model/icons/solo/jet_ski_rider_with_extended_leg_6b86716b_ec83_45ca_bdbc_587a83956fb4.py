"""Jet Ski Rider Jumping a Wave. Left-facing jet ski rider above a curling wave; rear leg extends behind the rider. Omit duplicate body outlines and extra wave crests.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: unified side silhouette; person-standing: sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b86716b-ec83-45ca-bdbc-587a83956fb4'
SOURCE_PATH = 'pictographic-primitives/recreation/sport jet skiing 1_6b86716b-ec83-45ca-bdbc-587a83956fb4.svg'
AUTHOR = 'gpt-6'


class JetSkiRiderWithExtendedLeg(Solo48):
    icon_id = 'jet-ski-rider-with-extended-leg'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('jet', 'ski', 'rider', 'with', 'extended', 'leg')

    def build(self) -> None:
        self.add_arc('head-top', (20, 8), (24, 8), radius_x=2, radius_y=2, sweep=True)
        self.add_arc('head-bottom', (24, 8), (20, 8), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('rider-1', (13, 25), (19, 27))
        self.add_line('rider-2', (19, 27), (24, 18))
        self.add_line('rider-3', (24, 18), (31, 22))
        self.add_line('rider-4', (31, 22), (34, 28))
        self.add_line('rider-5', (34, 28), (42, 25))
        self.add_contour('rider', 'rider-1', 'rider-2', 'rider-3', 'rider-4', 'rider-5', closed=False)
        self.add_line('craft-1', (6, 30), (6, 25))
        self.add_line('craft-2', (6, 25), (13, 25))
        self.add_line('craft-3', (13, 25), (21, 29))
        self.add_line('craft-4', (21, 29), (34, 32))
        self.add_line('craft-5', (34, 32), (36, 32))
        self.add_line('craft-6', (36, 32), (42, 32))
        self.add_contour('craft', 'craft-1', 'craft-2', 'craft-3', 'craft-4', 'craft-5', 'craft-6', closed=False)
        self.relate("connect", 'craft', 'rider')
        self.add_arc('wave', (6, 42), (18, 42), radius_x=6, radius_y=3, sweep=True)
        self.add_line('water', (18, 42), (42, 42))
        self.relate("connect", 'wave', 'water')
