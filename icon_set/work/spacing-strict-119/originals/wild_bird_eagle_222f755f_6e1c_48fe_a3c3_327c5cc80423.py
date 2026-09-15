"""Right-facing perched bird; extremes (8,6)-(40,42). Lucide bird informs head arc, hanging wing and attached straight legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '222f755f-6e1c-48fe-a3c3-327c5cc80423'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird eagle_222f755f-6e1c-48fe-a3c3-327c5cc80423.svg'
AUTHOR = 'gpt-6'


class PerchedBird(Solo48):
    icon_id = 'perched-bird'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bird', 'perched', 'standing', 'beak', 'wing', 'legs', 'wildlife', 'simple')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('crown',(18, 12),*(((19.70141156, 6.57772739), (23.72479037, 4), (28, 4)),))
        self.add_bezier('forehead',(28, 4),*(((32.27520963, 4), (36.29858844, 6.57772739), (38, 12)),))
        self.add_line('beak-upper',(38, 12),(40, 18))
        self.add_line('beak-lower',(40, 18),(32, 16))
        self.add_arc('breast',(32, 16),(32, 34),radius_x=16,radius_y=16,large_arc=False,sweep=True)
        self.add_bezier('belly',(32, 34),*(((30.81824478, 37.15064767), (27.55669741, 39.18911478), (24, 39)),))
        self.add_bezier('belly-left',(24, 39),*(((21.7554753, 38.65893119), (19.67414087, 37.79170852), (18, 36)),))
        self.add_line('back',(18, 36),(18, 19))
        self.add_line('back-top',(18, 19),(18, 12))
        self.add_arc('wing-top',(18, 19),(8, 29),radius_x=10,radius_y=10,large_arc=False,sweep=False)
        self.add_line('wing-edge',(8, 29),(8, 39))
        self.add_bezier('wing-tip',(8, 39),*(((13.03137444, 39.12916941), (17.31409283, 29.96617057), (18, 19)),))
        self.add_line('left-leg',(24, 39),(24, 44))
        self.add_line('right-leg',(32, 34),(32, 44))
        self.add_contour('body',*('crown', 'forehead', 'beak-upper', 'beak-lower', 'breast', 'belly', 'belly-left', 'back', 'back-top'),closed=True)
        self.add_contour('wing',*('wing-top', 'wing-edge', 'wing-tip'),closed=True)
        self.relate('connect',*('wing', 'body'))
        self.relate('connect',*('left-leg', 'body'))
        self.relate('connect',*('right-leg', 'body'))
