"""A rightward flip arrow crossing a divided panel.

Symbol plan: one rounded SQUARE panel, split top/bottom center divider, and one
rightward arched arrow. Centerline extremes (6,6)-(42,42); corner radius4.
The reviewed source brief explicitly preserves this integrated operation.
Panel mirrors about x24; arrow direction deliberately breaks the symmetry.
Lucide flip-horizontal-2 original/atomic-debug informs the interrupted center
axis, but the source's arched rightward arrow and panel are retained.
Shorten divider segments to preserve arrow clearance. No features are split
into another family. No human or text elements.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e8bb155-113e-43ce-848d-0a864def86be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/flip right_3e8bb155-113e-43ce-848d-0a864def86be.svg'
AUTHOR = 'gpt-6'


class HorizontalFlipRightArrow(Solo48):
    icon_id = 'horizontal-flip-right-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ('flip-right-panel',)
    keywords = ('horizontal', 'flip', 'right', 'arrow', 'panel', 'design')

    def build(self):
        axis, low, high, radius = 24, 6, 42, 4
        self.add_line('top-left',(low+radius,low),(axis,low))
        self.add_line('top-right',(axis,low),(high-radius,low))
        self.add_arc('corner-tr',(high-radius,low),(high,low+radius),radius_x=radius)
        self.add_line('right',(high,low+radius),(high,high-radius))
        self.add_arc('corner-br',(high,high-radius),(high-radius,high),radius_x=radius)
        self.add_line('bottom-right',(high-radius,high),(axis,high))
        self.add_line('bottom-left',(axis,high),(low+radius,high))
        self.add_arc('corner-bl',(low+radius,high),(low,high-radius),radius_x=radius)
        self.add_line('left',(low,high-radius),(low,low+radius))
        self.add_arc('corner-tl',(low,low+radius),(low+radius,low),radius_x=radius)
        self.add_contour('panel','top-left','top-right','corner-tr','right','corner-br',
                         'bottom-right','bottom-left','corner-bl','left','corner-tl',closed=True)
        for name,y1,y2 in [('top',low,10),('bottom',38,high)]:
            self.add_line('divider-'+name,(axis,y1),(axis,y2))
            self.relate('connect','panel','divider-'+name)
        self.add_arc('arrow-curve',(15,26),(33,26),radius_x=15)
        self.add_polyline('arrowhead',(29,18),(33,26),(25,29))
        self.relate('connect','arrow-curve','arrowhead')
