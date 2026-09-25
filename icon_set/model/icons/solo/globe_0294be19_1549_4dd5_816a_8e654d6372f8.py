"""A globe shows an equator and paired meridians. CIRCLE centerline radius20. Lucide globe informs fourfold rim construction and the central lens. Split arcs at the actual equator intersections; retain all source features."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0294be19-1549-4dd5-816a-8e654d6372f8'
SOURCE_PATH = 'pictographic-primitives/symbol/globe_0294be19-1549-4dd5-816a-8e654d6372f8.svg'
AUTHOR = 'gpt-6'


class Globe(Solo48):
    icon_id = 'globe'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('globe', 'world', 'internet', 'earth', 'web', 'language', 'international', 'planet')

    def build(self) -> None:
        rim=[(24,4),(44,24),(24,44),(4,24)]
        for i in range(4):
            self.add_arc(f'rim-{i}',rim[i],rim[(i+1)%4],radius_x=20)
        self.add_contour('rim',*(f'rim-{i}' for i in range(4)),closed=True)
        self.add_arc('meridian-left-top',(24,4),(14,24),radius_x=10,radius_y=20,sweep=False)
        self.add_arc('meridian-left-bottom',(14,24),(24,44),radius_x=10,radius_y=20,sweep=False)
        self.add_arc('meridian-right-bottom',(24,44),(34,24),radius_x=10,radius_y=20,sweep=False)
        self.add_arc('meridian-right-top',(34,24),(24,4),radius_x=10,radius_y=20,sweep=False)
        self.add_contour('meridians','meridian-left-top','meridian-left-bottom','meridian-right-bottom','meridian-right-top',closed=True)
        self.add_polyline('equator',(4,24),(14,24),(34,24),(44,24))
        self.relate('connect','rim','meridians')
        self.relate('connect','rim','equator')
        self.relate('connect','meridians','equator')
