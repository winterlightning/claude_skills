"""A tall rounded rectangular panel is crossed by two parallel flowing curves. Each wave rises from lower-left to upper-right, creating a broad ribbon-like band across the middle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95368e36-69fd-40b6-94ae-03fe0a41a272'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rectangle with waves_95368e36-69fd-40b6-94ae-03fe0a41a272.svg'
AUTHOR = 'gpt-6'


class Batch032Icon(Solo48):
    icon_id = 'upright-panel-with-flowing-waves-batch-032'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('upright-panel-with-flowing-waves',)
    keywords = ('batch-032',)

    def build(self):
        # Symbol plan: Upright panel with two translated smooth waves; split wall attachment nodes; extrema (8,4)-(40,44).

        self.add_polyline('left',(8,44),(8,32),(8,20),(8,4))
        self.add_line('top',(8,4),(40,4))
        self.add_polyline('right',(40,4),(40,16),(40,28),(40,44))
        self.add_line('bottom',(40,44),(8,44))
        self.contours.clear()
        self.add_contour('panel','left-1','left-2','left-3','top','right-1','right-2','right-3','bottom',closed=True)
        for i,y in enumerate((20,32)):
            self.add_bezier(f'wave-{i}',(8,y),((18,y-8),(30,y+4),(40,y-4)))
            self.relate('connect','panel',f'wave-{i}')
