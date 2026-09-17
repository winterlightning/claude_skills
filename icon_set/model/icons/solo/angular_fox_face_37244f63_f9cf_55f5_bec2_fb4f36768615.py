"""Geometric Fox Head.
Plan: Mirrored tall ears and faceted cheeks around eyes and a pointed nose. Extrema (6,6)-(42,42).
Reference: Supplied original; no useful exact local Lucide match. Shared axes and simple geometric construction.
Reduction: Extra left inner-ear contour omitted and pentagonal nose reduced to a dot; face remains bilateral.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37244f63-f9cf-55f5-bec2-fb4f36768615'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/finance/crypto wallet metamask_37244f63-f9cf-55f5-bec2-fb4f36768615.svg'
AUTHOR = 'gpt-6'

class Batch30Icon(Solo48):
    icon_id = 'angular-fox-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ()
    keywords = ('geometric', 'fox', 'head')

    def build(self):

        self.add_polyline('face',(6,6),(18,16),(30,16),(42,6),(38,26),(42,32),(30,42),(18,42),(6,32),(10,26),(6,6))
        self.add_line('eye-left',(18,25),(20,26))
        self.add_line('eye-right',(30,25),(28,26))
        self.add_dot('nose',(24,34))
