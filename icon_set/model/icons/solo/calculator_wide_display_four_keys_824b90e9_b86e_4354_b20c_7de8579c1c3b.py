"""Simple Digital Calculator.
Plan: Rounded calculator with upper blank display and two-by-two short bar keys. Extrema (8,4)-(40,44).
Reference: Lucide calculator: rounded upright housing, blank display and repeated aligned keys.
Reduction: Four keys retained. Display uses the upper housing as its border, leaving more space for the two keypad rows.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '824b90e9-b86e-4354-b20c-7de8579c1c3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/calculator_824b90e9-b86e-4354-b20c-7de8579c1c3b.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'calculator-wide-display-four-keys'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance"
    aliases = ()
    keywords = ('simple', 'digital', 'calculator')

    def build(self):

        self.add_line('body-top',(12,4),(36,4))
        self.add_arc('body-tr',(36,4),(40,8),radius_x=4)
        self.add_line('body-right-a',(40,8),(40,17))
        self.add_line('body-right-b',(40,17),(40,40))
        self.add_arc('body-br',(40,40),(36,44),radius_x=4)
        self.add_line('body-base',(36,44),(12,44))
        self.add_arc('body-bl',(12,44),(8,40),radius_x=4)
        self.add_line('body-left-a',(8,40),(8,17))
        self.add_line('body-left-b',(8,17),(8,8))
        self.add_arc('body-tl',(8,8),(12,4),radius_x=4)
        self.add_contour('body',*[f'body-{s}' for s in ('top','tr','right-a','right-b','br','base','bl','left-a','left-b','tl')],closed=True)

        self.add_line('display',(8,17),(40,17));self.relate('connect','display','body')
        for i,y in enumerate((26,35)):
            self.add_line(f'key-{i}-left',(17,y),(20,y))
            self.add_line(f'key-{i}-right',(28,y),(31,y))
