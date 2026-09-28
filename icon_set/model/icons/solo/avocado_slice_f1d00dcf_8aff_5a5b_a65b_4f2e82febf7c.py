'Avocado half: smooth symmetric pear-shaped outline with a circular stone and balanced flesh around it.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f1d00dcf-8aff-5a5b-a65b-4f2e82febf7c'
SOURCE_PATH = 'pictographic-primitives/food/avocado slice_f1d00dcf-8aff-5a5b-a65b-4f2e82febf7c.svg'
AUTHOR = 'gpt-6'

class AvocadoSlice(Solo48):
    icon_id = 'avocado-slice'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('avocado', 'slice', 'food')

    def build(self) -> None:
        # VRECT_L ink envelope; equal lower halves, smooth pear-shaped upper flanks.
        self.add_bezier('upper-left',(24,4),((17,4),(17,13),(13,19)),((10,23),(8,26),(8,29)))
        self.add_bezier('lower-left',(8,29),((8,37),(15,44),(24,44)))
        self.add_bezier('lower-right',(24,44),((33,44),(40,37),(40,29)))
        self.add_bezier('upper-right',(40,29),((40,26),(38,23),(35,19)),((31,13),(31,4),(24,4)))
        self.add_contour('fruit','upper-left','lower-left','lower-right','upper-right',closed=True)

        self.add_arc('stone-top', (18,29), (30,29), radius_x=6, radius_y=6)
        self.add_arc('stone-bottom', (30,29), (18,29), radius_x=6, radius_y=6)
        self.add_contour('stone', 'stone-top', 'stone-bottom', closed=True)
