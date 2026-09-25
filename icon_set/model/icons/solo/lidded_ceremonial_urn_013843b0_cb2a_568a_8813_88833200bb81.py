'Lidded ceremonial urn.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '013843b0-cb2a-568a-8813-88833200bb81'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/urn_013843b0-cb2a-568a-8813-88833200bb81.svg'
AUTHOR = 'gpt-6'

class LiddedCeremonialUrn(Solo48):
    icon_id = 'lidded-ceremonial-urn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('urn', 'vessel', 'pottery', 'funerary', 'ceramic', 'antique', 'museum', 'ashes')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_16_4 = (16, 4)
        p_32_4 = (32, 4)
        p_19_4 = (19, 4)
        p_19_12 = (19, 12)
        p_16_12 = (16, 12)
        p_14_20 = (14, 20)
        p_21_36 = (21, 36)
        p_27_36 = (27, 36)
        p_34_20 = (34, 20)
        p_32_12 = (32, 12)
        p_29_12 = (29, 12)
        p_29_4 = (29, 4)
        p_14_30 = (14, 30)
        p_34_30 = (34, 30)
        p_16_44 = (16, 44)
        p_32_44 = (32, 44)
        self.add_line('lid', p_16_4, p_32_4)
        self.add_line('neck-1', p_19_4, p_19_12)
        self.add_line('neck-2', p_19_12, p_16_12)
        self.add_arc('shoulder-left', p_16_12, p_14_20, radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('bowl-left', p_14_20, p_21_36, radius_x=21, radius_y=23, sweep=False, large_arc=False)
        self.add_line('bowl-bottom', p_21_36, p_27_36)
        self.add_arc('bowl-right', p_27_36, p_34_20, radius_x=21, radius_y=23, sweep=False, large_arc=False)
        self.add_arc('shoulder-right', p_34_20, p_32_12, radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_line('neck-right-1', p_32_12, p_29_12)
        self.add_line('neck-right-2', p_29_12, p_29_4)
        self.add_arc('handle-left', p_14_20, p_14_30, radius_x=6, radius_y=5, sweep=False, large_arc=False)
        self.add_arc('handle-right', p_34_30, p_34_20, radius_x=6, radius_y=5, sweep=False, large_arc=False)
        self.add_line('foot-1', p_21_36, p_16_44)
        self.add_line('foot-2', p_16_44, p_32_44)
        self.add_line('foot-3', p_32_44, p_27_36)
        self.add_contour('vessel', 'neck-1', 'neck-2', 'shoulder-left', 'bowl-left', 'bowl-bottom', 'bowl-right', 'shoulder-right', 'neck-right-1', 'neck-right-2', closed=False)
        self.add_contour('foot', 'foot-1', 'foot-2', 'foot-3', closed=False)
        self.relate('connect', 'lid', 'vessel')
        self.relate('connect', 'vessel', 'handle-left')
        self.relate('connect', 'vessel', 'handle-right')
        self.relate('connect', 'vessel', 'foot')
