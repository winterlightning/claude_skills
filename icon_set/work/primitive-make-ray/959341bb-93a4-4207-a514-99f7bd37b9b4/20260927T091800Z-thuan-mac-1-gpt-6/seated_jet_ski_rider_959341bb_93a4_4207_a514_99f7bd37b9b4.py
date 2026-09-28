"""Seated Jet Ski Rider. Seated left-facing rider with a hanging bent leg and rounded rear cowling; retain one water row and omit hull trim.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: coherent hull curves; person-standing: circular head and articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '959341bb-93a4-4207-a514-99f7bd37b9b4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-jet-ski-rider/20260927T091411Z-thuan-mac-1/reference/sport jet skiing_959341bb-93a4-4207-a514-99f7bd37b9b4.svg'
AUTHOR = 'gpt-6'


class SeatedJetSkiRider(Solo48):
    icon_id = 'seated-jet-ski-rider'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('seated', 'jet', 'ski', 'rider')

    def build(self) -> None:
        self.add_arc('head-top', (13, 9), (19, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (19, 9), (13, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('rider-1', (13, 23), (18, 23))
        self.add_line('rider-2', (18, 23), (23, 18))
        self.add_line('rider-3', (23, 18), (29, 23))
        self.add_line('rider-4', (29, 23), (25, 30))
        self.add_line('rider-5', (25, 30), (29, 31))
        self.add_contour('rider', 'rider-1', 'rider-2', 'rider-3', 'rider-4', 'rider-5', closed=False)
        self.add_line('deck-1', (6, 29), (13, 23))
        self.add_line('deck-2', (13, 23), (18, 23))
        self.add_contour('deck', 'deck-1', 'deck-2', closed=False)
        self.add_arc('nose', (6, 29), (6, 31), radius_x=4, radius_y=4, sweep=True)
        self.add_line('seat-1', (29, 23), (36, 23))
        self.add_bezier('stern', (36, 23), ((42, 23), (42, 28), (42, 31)))
        self.add_contour('craft-rear', 'seat-1', 'stern', closed=False)
        self.relate("connect", 'rider', 'deck')
        self.relate("connect", 'deck', 'nose')
        self.relate("connect", 'craft-rear', 'rider')
        self.add_arc('wave-left', (6, 40), (24, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_arc('wave-right', (24, 40), (42, 40), radius_x=9, radius_y=2, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right', closed=False)
        self.add_polyline('hull-deck', (6, 31), (29, 31), (42, 31))
        self.relate('connect', 'hull-deck', 'nose')
        self.relate('connect', 'hull-deck', 'craft-rear')
        self.relate('connect', 'hull-deck', 'rider')
        self.mark_human_figure('person', head='head', torso='rider-3', torso_junction='start')
