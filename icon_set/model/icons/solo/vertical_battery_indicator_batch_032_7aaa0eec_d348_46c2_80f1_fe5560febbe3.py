"""An upright battery has a plain rounded rectangular body and a smaller raised terminal centered on top. Its interior is empty, with no charge bars or polarity marks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7aaa0eec-d348-46c2-80f1-fe5560febbe3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/battery vertical_7aaa0eec-d348-46c2-80f1-fe5560febbe3.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'vertical-battery-indicator-batch-032'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('vertical-battery-indicator',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Body with raised terminal; shared axis 24; extrema (8,4)-(40,44).

        self.add_polyline('terminal',(16,12),(16,4),(32,4),(32,12))
        self.add_line('top-left',(12,12),(16,12))
        self.add_line('top-mid',(16,12),(32,12))
        self.add_line('top-right',(32,12),(36,12))
        self.add_arc('tr',(36,12),(40,16),radius_x=4)
        self.add_line('right',(40,16),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('base',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,16))
        self.add_arc('tl',(8,16),(12,12),radius_x=4)
        self.add_contour('body','top-left','top-mid','top-right','tr','right','br','base','bl','left','tl',closed=True)
        self.relate('connect','terminal','body')
