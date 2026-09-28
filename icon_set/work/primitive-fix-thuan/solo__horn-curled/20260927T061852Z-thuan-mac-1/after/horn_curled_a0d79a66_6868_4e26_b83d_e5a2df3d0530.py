"""Fresh SOLO48 revision of horn-curled from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a0d79a66-6868-4e26-b83d-e5a2df3d0530'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horn-curled/20260927T061852Z-thuan-mac-1/reference/horn 1_a0d79a66-6868-4e26-b83d-e5a2df3d0530.svg'
AUTHOR = 'gpt-6'

class HornCurled(Solo48):
    icon_id = 'horn-curled'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('horn', 'instrument', 'music', 'brass', 'curled', 'bugle', 'sound', 'wind')

    def build(self) -> None:

        # A curved bell and smooth S-shaped upper tube.
        self.add_bezier('bell-top',(8,25),((12,23),(17,23),(22,21)))
        self.add_line('neck-left',(22,21),(22,12))
        self.add_bezier('crown-left',(22,12),((23,7),(26,4),(30,4)))
        self.add_bezier('crown-right',(30,4),((34,4),(37,7),(38,12)))
        self.add_line('mouth-top',(38,12),(40,20))
        self.add_line('mouth-bottom',(40,20),(33,16))
        self.add_arc('neck-inner',(33,16),(31,20),radius_x=3,radius_y=3,sweep=False)
        self.add_line('tube-inner',(31,20),(34,30))
        self.add_bezier('tube-bottom',(34,30),((33,38),(28,44),(22,44)))
        self.add_bezier('bell-bottom',(22,44),((15,44),(9,38),(8,30)))
        self.add_line('bell-left',(8,30),(8,25))
        self.add_bezier('bell-divider',(22,21),((26,27),(26,38),(22,44)))
        self.add_contour('horn','bell-top','neck-left','crown-left','crown-right',
                         'mouth-top','mouth-bottom','neck-inner','tube-inner',
                         'tube-bottom','bell-bottom','bell-left',closed=True)
        contacts(self)
