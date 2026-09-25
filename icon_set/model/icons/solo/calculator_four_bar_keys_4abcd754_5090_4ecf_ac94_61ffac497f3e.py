"""Simple Digital Calculator.
Plan: Rounded calculator with upper blank display and two-by-two short bar keys. Extrema (10,4)-(38,44).
Reference: Lucide calculator: rounded upright housing, blank display and repeated aligned keys.
Reduction: Four keys retained. Display uses the upper housing as its border, leaving more space for the two keypad rows.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4abcd754-5090-4ecf-ac94-61ffac497f3e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/calculator_4abcd754-5090-4ecf-ac94-61ffac497f3e.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'calculator-four-bar-keys'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ()
    keywords = ('simple', 'digital', 'calculator')

    def build(self):

        self.add_line('body-top',(14,4),(34,4))
        self.add_arc('body-tr',(34,4),(38,8),radius_x=4)
        self.add_line('body-right-a',(38,8),(38,17))
        self.add_line('body-right-b',(38,17),(38,40))
        self.add_arc('body-br',(38,40),(34,44),radius_x=4)
        self.add_line('body-base',(34,44),(14,44))
        self.add_arc('body-bl',(14,44),(10,40),radius_x=4)
        self.add_line('body-left-a',(10,40),(10,17))
        self.add_line('body-left-b',(10,17),(10,8))
        self.add_arc('body-tl',(10,8),(14,4),radius_x=4)
        self.add_contour('body',*[f'body-{s}' for s in ('top','tr','right-a','right-b','br','base','bl','left-a','left-b','tl')],closed=True)

        self.add_line('display',(10,17),(38,17));self.relate('connect','display','body')
        for i,y in enumerate((26,35)):
            self.add_line(f'key-{i}-left',(19,y),(20,y))
            self.add_line(f'key-{i}-right',(28,y),(29,y))
