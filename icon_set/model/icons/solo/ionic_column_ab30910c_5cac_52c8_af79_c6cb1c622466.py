'Ionic column.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab30910c-5cac-52c8-af79-c6cb1c622466'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/empire_ab30910c-5cac-52c8-af79-c6cb1c622466.svg'
AUTHOR = 'gpt-6'

class IonicColumn(Solo48):
    icon_id = 'ionic-column'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('column', 'ionic', 'classical', 'greek', 'roman', 'architecture', 'pillar', 'antiquity')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_12_6 = (12, 6)
        p_12_18 = (12, 18)
        p_36_6 = (36, 6)
        p_36_18 = (36, 18)
        p_12_34 = (12, 34)
        p_36_34 = (36, 34)
        p_9_42 = (9, 42)
        p_9_34 = (9, 34)
        p_39_34 = (39, 34)
        p_39_42 = (39, 42)
        self.add_arc('left-scroll-a', p_12_6, p_12_18, radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('left-scroll-b', p_12_18, p_12_6, radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('right-scroll-a', p_36_6, p_36_18, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('right-scroll-b', p_36_18, p_36_6, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('capital-top', p_12_6, p_36_6)
        self.add_line('capital-bottom', p_12_18, p_36_18)
        self.add_line('shaft-left', p_12_18, p_12_34)
        self.add_line('shaft-right', p_36_18, p_36_34)
        self.add_line('plinth-1', p_9_42, p_9_34)
        self.add_line('plinth-2', p_9_34, p_12_34)
        self.add_line('plinth-3', p_12_34, p_36_34)
        self.add_line('plinth-4', p_36_34, p_39_34)
        self.add_line('plinth-5', p_39_34, p_39_42)
        self.add_line('plinth-6', p_39_42, p_9_42)
        self.add_contour('left-scroll', 'left-scroll-a', 'left-scroll-b', closed=True)
        self.add_contour('right-scroll', 'right-scroll-a', 'right-scroll-b', closed=True)
        self.add_contour('plinth', 'plinth-1', 'plinth-2', 'plinth-3', 'plinth-4', 'plinth-5', 'plinth-6', closed=False)
        self.relate('connect', 'left-scroll', 'capital-top')
        self.relate('connect', 'left-scroll', 'capital-bottom')
        self.relate('connect', 'right-scroll', 'capital-top')
        self.relate('connect', 'right-scroll', 'capital-bottom')
        self.relate('connect', 'shaft-left', 'plinth')
        self.relate('connect', 'shaft-left', 'left-scroll')
        self.relate('connect', 'shaft-left', 'capital-bottom')
        self.relate('connect', 'shaft-right', 'right-scroll')
        self.relate('connect', 'shaft-right', 'capital-bottom')
        self.relate('connect', 'shaft-right', 'plinth')
