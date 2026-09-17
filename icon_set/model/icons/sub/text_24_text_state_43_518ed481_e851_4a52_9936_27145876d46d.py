"""24 Text: The digits 24 stand in a horizontal row, with a curved two and an angular open four. Generate this component alone; exclude Double-Ended Wrench.

Construction: A rounded 2 precedes an open 4 with its projecting bar; both source digits retained.
Keyshape: HRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '518ed481-e851-4a52-9936-27145876d46d'
SOURCE_PATH = 'pictographic-primitives/state/circle 24 with wrench_518ed481-e851-4a52-9936-27145876d46d.svg'
AUTHOR = 'gpt-6'


class Text24TextState43(Sub32):
    icon_id = 'text-24-text-state-43'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('24', 'text', 'digits', 'stand', 'horizontal', 'row', 'curved', 'angular')

    def build(self):
        self.add_arc('two-top',(2,11),(10,11),radius_x=4,radius_y=5)
        self.add_line('two-slope',(10,11),(2,26))
        self.add_line('two-base',(2,26),(10,26))
        self.add_contour('two','two-top','two-slope','two-base')
        self.add_polyline('four-arm',(24,6),(18,20),(30,20))
        self.add_line('four-stem',(30,6),(30,26))
        self.relate('connect','four-arm','four-stem')
