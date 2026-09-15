'Pharaoh nemes mask.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1975cc8c-a609-4ae8-b0fe-2049efc52c92'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/sphinx_1975cc8c-a609-4ae8-b0fe-2049efc52c92.svg'
AUTHOR = 'gpt-6'

class PharaohNemesMask(Solo48):
    icon_id = 'pharaoh-nemes-mask'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('pharaoh', 'mask', 'tutankhamun', 'egyptian', 'nemes', 'ancient', 'tomb', 'gold')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_34 = (6, 34)
        p_16_14 = (16, 14)
        p_24_14 = (24, 14)
        p_32_14 = (32, 14)
        p_42_34 = (42, 34)
        p_14_34 = (14, 34)
        p_14_42 = (14, 42)
        p_34_34 = (34, 34)
        p_34_42 = (34, 42)
        p_16_26 = (16, 26)
        p_24_34 = (24, 34)
        p_32_26 = (32, 26)
        p_24_6 = (24, 6)
        p_24_42 = (24, 42)
        self.add_arc('cloth-left', p_6_34, p_16_14, radius_x=10, radius_y=20, sweep=True, large_arc=False)
        self.add_line('crown', p_16_14, p_24_14)
        self.add_line('crown-right', p_24_14, p_32_14)
        self.add_arc('cloth-right', p_32_14, p_42_34, radius_x=10, radius_y=20, sweep=True, large_arc=False)
        self.add_line('drape-left-0', p_6_34, p_14_34)
        self.add_line('drape-left-1', p_14_34, p_14_42)
        self.add_line('drape-right-0', p_42_34, p_34_34)
        self.add_line('drape-right-1', p_34_34, p_34_42)
        self.add_line('face-left', p_16_14, p_16_26)
        self.add_arc('jaw-left', p_16_26, p_24_34, radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('jaw-right', p_24_34, p_32_26, radius_x=8, radius_y=8, sweep=False, large_arc=False)
        self.add_line('face-right', p_32_26, p_32_14)
        self.add_line('crest', p_24_6, p_24_14)
        self.add_line('beard', p_24_34, p_24_42)
        self.add_contour('drape-left', 'drape-left-0', 'drape-left-1', closed=False)
        self.add_contour('drape-right', 'drape-right-0', 'drape-right-1', closed=False)
        self.add_contour('face', 'face-left', 'jaw-left', 'jaw-right', 'face-right', closed=False)
        self.relate('connect', 'cloth-left', 'drape-left')
        self.relate('connect', 'cloth-right', 'drape-right')
        self.relate('connect', 'cloth-left', 'crown')
        self.relate('connect', 'cloth-right', 'crown-right')
        self.relate('connect', 'face', 'crown')
        self.relate('connect', 'face', 'crown-right')
        self.relate('connect', 'face', 'cloth-left')
        self.relate('connect', 'face', 'cloth-right')
        self.relate('connect', 'crown', 'crown-right')
        self.relate('connect', 'crest', 'crown')
        self.relate('connect', 'crest', 'crown-right')
        self.relate('connect', 'beard', 'face')
