from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc5b59be-4ef1-4ebf-99fa-15d310d43971'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/flatten_bc5b59be-4ef1-4ebf-99fa-15d310d43971.svg'
AUTHOR = 'gpt-6'


class DownwardArrowAboveTwoBaselines(Solo48):
    icon_id = 'downward-arrow-above-two-baselines'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('arrow', 'down', 'flatten', 'layers', 'baseline', 'merge', 'direction', 'design')

    def build(self) -> None:
        # Centered downward arrow and two progressively wider baselines.
        axis=24
        self.add_line('stem',(axis,6),(axis,26))
        self.add_polyline('head',(axis-10,16),(axis,26),(axis+10,16))
        self.relate('connect','stem','head')
        for name,y,halfwidth in [('upper',34,10),('lower',42,18)]:self.add_line(name,(axis-halfwidth,y),(axis+halfwidth,y))
