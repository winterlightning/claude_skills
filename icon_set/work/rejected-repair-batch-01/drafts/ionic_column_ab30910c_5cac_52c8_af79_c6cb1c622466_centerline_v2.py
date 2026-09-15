"""Widen the column base and taper the shaft slightly inward toward the capital; the scrolls now sit above a more convincing column proportion.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab30910c-5cac-52c8-af79-c6cb1c622466'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/empire_ab30910c-5cac-52c8-af79-c6cb1c622466.svg'
AUTHOR = 'gpt-6'

class IonicColumn(Solo48):
    icon_id = 'ionic-column-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('column', 'ionic', 'classical', 'greek', 'roman', 'architecture', 'pillar', 'antiquity')

    def build(self) -> None:
        p_12_6 = (12, 6)
        p_12_18 = (12, 18)
        p_36_6 = (36, 6)
        p_36_18 = (36, 18)
        p_12_34 = (10, 34)
        p_36_34 = (38, 34)
        p_9_42 = (6, 42)
        p_9_34 = (6, 34)
        p_39_34 = (42, 34)
        p_39_42 = (42, 42)
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
    variant_of = 'ionic-column'
    variant_label = 'Batch 01 centerline repair'
