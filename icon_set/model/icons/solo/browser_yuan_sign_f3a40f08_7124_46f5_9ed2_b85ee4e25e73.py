from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3a40f08-7124-46f5-9ed2-b85ee4e25e73'
SOURCE_PATH = 'pictographic-primitives/other/browser yuan sign right_f3a40f08-7124-46f5-9ed2-b85ee4e25e73.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    """Browser frame with one-bar yuan sign aligned to the right. Bounds (8,4)-(40,44)."""
    icon_id = 'browser-yuan-sign-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('browser', 'window', 'with', 'yuan', 'sign')

    def build(self):
        self.add_line('top',(12,4),(36,4))
        self.add_arc('tr',(36,4),(40,8),radius_x=4)
        self.add_line('ru',(40,8),(40,12))
        self.add_line('rl',(40,12),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('ll',(8,40),(8,12))
        self.add_line('lu',(8,12),(8,8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('frame','top','tr','ru','rl','br','bottom','bl','ll','lu','tl',closed=True)
        self.add_line('header',(8,12),(40,12))
        self.relate('connect','frame','header')
        # Right-aligned yuan: branch node and bar crossing shared by the strokes.
        self.add_polyline('fork',(23,21),(27,27),(31,21))
        self.add_polyline('stem',(27,27),(27,30),(27,35))
        self.add_polyline('bar',(23,30),(27,30),(31,30))
        self.relate('connect','fork','stem')
        self.relate('connect','stem','bar')
