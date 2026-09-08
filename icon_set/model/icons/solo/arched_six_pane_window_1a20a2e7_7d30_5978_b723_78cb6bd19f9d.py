"""A standalone arched architectural window with six panes and a projecting sill."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a20a2e7-7d30-5978-b723-78cb6bd19f9d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/asian interior windows_1a20a2e7-7d30-5978-b723-78cb6bd19f9d.svg'
AUTHOR = 'gpt-6'


class ArchedSixPaneWindow(Solo48):
    icon_id = 'arched-six-pane-window'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('window', 'arch', 'panes', 'frame', 'architecture', 'interior', 'glazing')

    def build(self) -> None:
        self.add_arc('arch-left', (8,18), (24,2), radius_x=16)
        self.add_arc('arch-right', (24,2), (40,18), radius_x=16)
        self.add_polyline('right-wall', (40,18),(40,32),(40,46))
        self.add_polyline('sill', (43,46),(40,46),(24,46),(8,46),(5,46))
        self.add_polyline('left-wall', (8,46),(8,32),(8,18))
        self.add_contour('arch','arch-left','arch-right')
        self.add_polyline('mullion', (24,2),(24,18),(24,32),(24,46))
        self.add_polyline('upper-transom',(8,18),(24,18),(40,18))
        self.add_polyline('lower-transom',(8,32),(24,32),(40,32))
        for a,b in [('arch','right-wall'),('arch','left-wall'),('arch','mullion'),('arch','upper-transom'),('right-wall','sill'),('left-wall','sill'),('mullion','sill'),('mullion','upper-transom'),('mullion','lower-transom'),('upper-transom','right-wall'),('upper-transom','left-wall'),('lower-transom','right-wall'),('lower-transom','left-wall')]:
            self.relate('connect',a,b)
