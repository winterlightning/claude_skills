"""A telephone handset stands vertically, with its curved outer back on the left. Broad upper and lower earpieces project right from the narrower central grip, enclosing an open inner gap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c77144a9-35d2-4377-bddd-6845d3a0bbad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/phone vertical_c77144a9-35d2-4377-bddd-6845d3a0bbad.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'vertical-telephone-handset-batch-032'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('vertical-telephone-handset',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: One curved receiver silhouette; left back and right-facing mirrored earpieces; extrema (10,4)-(38,44).

        self.add_bezier('back',(28,4),((14,4),(10,12),(10,24)),((10,36),(14,44),(28,44)))
        self.add_line('bottom',(28,44),(34,44))
        self.add_arc('lower-tip',(34,44),(38,40),radius_x=4,sweep=False)
        self.add_line('lower-outer',(38,40),(38,36))
        self.add_arc('lower-inner',(38,36),(34,32),radius_x=4,sweep=False)
        self.add_line('lower-face',(34,32),(26,32))
        self.add_bezier('grip',(26,32),((22,32),(22,28),(22,24)),((22,20),(22,16),(26,16)))
        self.add_line('upper-face',(26,16),(34,16))
        self.add_arc('upper-inner',(34,16),(38,12),radius_x=4,sweep=False)
        self.add_line('upper-outer',(38,12),(38,8))
        self.add_arc('upper-tip',(38,8),(34,4),radius_x=4,sweep=False)
        self.add_line('top',(34,4),(28,4))
        self.add_contour('outline','back','bottom','lower-tip','lower-outer','lower-inner','lower-face','grip','upper-face','upper-inner','upper-outer','upper-tip','top',closed=True)
