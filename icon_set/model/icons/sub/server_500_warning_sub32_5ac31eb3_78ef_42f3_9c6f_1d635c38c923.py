"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '5ac31eb3-78ef-42f3-9c6f-1d635c38c923'
SOURCE_PATH = 'pictographic-primitives/state/warning with 500 error_5ac31eb3-78ef-42f3-9c6f-1d635c38c923.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('outlined warning triangle', 'exclamation stem and dot', '500 on the lower row')

class Drawing(Sub32):
    icon_id = 'server-500-warning-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    keywords = ('internal', 'server', 'error', 'warning')
    TYPEFACE_GLYPH_IDS = ('digit-5', 'digit-0', 'digit-0')

    def build(self):
        self.add_polyline('triangle',(16,2),(27,18),(5,18),closed=True)
        self.add_line('warning-stem',(16,8),(16,9))
        self.add_dot('warning-dot',(16,14))
        self.add_line('text-5-0-0-0-0',(7.3645, 24),(2.252387, 24))
        self.primitives.append(Bezier('text-5-0-0-1-0',Point(*(2.252387, 24)),Point(*(2, 24.175043)),(((2.112999, 24), (2, 24.07837), (2, 24.175043)),)))
        self.add_line('text-5-0-0-1-1',(2, 24.175043),(2, 26.326948))
        self.add_contour('glyph-5-0-0-1',*['text-5-0-0-1-0', 'text-5-0-0-1-1'],closed=False)
        self.primitives.append(Bezier('text-5-0-0-2-0',Point(*(2, 26.326948)),Point(*(2.252387, 26.501992)),(((2, 26.423621), (2.112999, 26.501992), (2.252387, 26.501992)),)))
        self.add_line('text-5-0-0-3-0',(2.252387, 26.501992),(5.473155, 26.501992))
        self.primitives.append(Bezier('text-5-0-0-4-0',Point(*(5.473155, 26.501992)),Point(*(7.289043, 29.464637)),(((7.697417, 26.501992), (8.832462, 28.35382), (7.289043, 29.464637)),)))
        self.primitives.append(Bezier('text-5-0-0-5-0',Point(*(7.289043, 29.464637)),Point(*(5.473155, 30)),(((6.813704, 29.806729), (6.158172, 30), (5.473155, 30)),)))
        self.add_line('text-5-0-0-6-0',(5.473155, 30),(2.280282, 30))
        self.primitives.append(Bezier('text-0-1-0-0-0',Point(*(13, 25.713092)),Point(*(19, 25.713092)),(((13, 25.258926), (13.316286, 24.822897), (13.87868, 24.501753)), ((14.441073, 24.180609), (15.204656, 24), (16, 24)), ((16.795344, 24), (17.558927, 24.180609), (18.12132, 24.501753)), ((18.683714, 24.822897), (19, 25.258926), (19, 25.713092)))))
        self.add_line('text-0-1-0-0-1',(19, 25.713092),(19, 28.286908))
        self.primitives.append(Bezier('text-0-1-0-0-2',Point(*(19, 28.286908)),Point(*(13, 28.286908)),(((19, 28.741074), (18.683714, 29.177103), (18.12132, 29.498247)), ((17.558927, 29.819391), (16.795344, 30), (16, 30)), ((15.204656, 30), (14.441073, 29.819391), (13.87868, 29.498247)), ((13.316286, 29.177103), (13, 28.741074), (13, 28.286908)))))
        self.add_line('text-0-1-0-0-3',(13, 28.286908),(13, 25.713092))
        self.add_contour('glyph-0-1-0-0',*['text-0-1-0-0-0', 'text-0-1-0-0-1', 'text-0-1-0-0-2', 'text-0-1-0-0-3'],closed=True)
        self.primitives.append(Bezier('text-0-2-0-0-0',Point(*(24, 25.713092)),Point(*(30, 25.713092)),(((24, 25.258926), (24.316286, 24.822897), (24.87868, 24.501753)), ((25.441073, 24.180609), (26.204656, 24), (27, 24)), ((27.795344, 24), (28.558927, 24.180609), (29.12132, 24.501753)), ((29.683714, 24.822897), (30, 25.258926), (30, 25.713092)))))
        self.add_line('text-0-2-0-0-1',(30, 25.713092),(30, 28.286908))
        self.primitives.append(Bezier('text-0-2-0-0-2',Point(*(30, 28.286908)),Point(*(24, 28.286908)),(((30, 28.741074), (29.683714, 29.177103), (29.12132, 29.498247)), ((28.558927, 29.819391), (27.795344, 30), (27, 30)), ((26.204656, 30), (25.441073, 29.819391), (24.87868, 29.498247)), ((24.316286, 29.177103), (24, 28.741074), (24, 28.286908)))))
        self.add_line('text-0-2-0-0-3',(24, 28.286908),(24, 25.713092))
        self.add_contour('glyph-0-2-0-0',*['text-0-2-0-0-0', 'text-0-2-0-0-1', 'text-0-2-0-0-2', 'text-0-2-0-0-3'],closed=True)

