"""Selected Layer Stack.

Symbol plan: Top diamond and matching lower V share x28 axis; detached selection corner at lower-left. Centerline extremes (6,6)-(42,42). Lower layer upper edges are hidden behind the top layer. Asymmetric corner retains selection meaning.
Source reference: SOURCE_PATH. Lucide originals and atomic-debug layers-2 and
sun informed the layer silhouette and radial brightness mark respectively.
No human or text elements. Preserve this integrated subject from its brief.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f12d063-a22b-41cb-b794-1c2e34cc8aa5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/layers select_1f12d063-a22b-41cb-b794-1c2e34cc8aa5.svg'
AUTHOR = 'gpt-6'

class SelectedLayerStack(Solo48):
    icon_id = 'selected-layer-stack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('selected', 'layer', 'stack')

    def build(self):
        axis, half_width = 28, 14
        self.add_polyline('upper-layer',(axis,6),(axis+half_width,14),(axis,22),(axis-half_width,14),closed=True)
        self.add_polyline('lower-layer',(axis-half_width+1,25),(axis,33),(axis+half_width-1,25))
        self.add_line('selection-side',(6,22),(6,38))
        self.add_arc('selection-corner',(6,38),(10,42),radius_x=4,sweep=False)
        self.add_line('selection-bottom',(10,42),(28,42))
        self.add_contour('selection','selection-side','selection-corner','selection-bottom')
