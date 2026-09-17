"""Electric Water Kettle.

Plan: Electric kettle with left spout, domed roof, oval water window and right handle. Bounds (4,8)-(44,40). Knob and base seam dropped for window clearance.
Construction reference: Lucide coffee: attached handle and rounded base; no useful exact kettle match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'a049528e-fa8f-4ccb-a020-8a2719585427'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/tea kettle_a049528e-fa8f-4ccb-a020-8a2719585427.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'electric-kettle-with-oval-water-window'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('electric', 'water', 'kettle')

    def build(self):
        path(self,'body',(4,16),('L',(12,16)),('A',11,8,True,(23,8)),('A',11,8,True,(34,16)),('L',(34,36)),('A',4,4,True,(30,40)),('L',(12,40)),('A',4,4,True,(8,36)),('L',(10,24)),('L',(4,16)),closed=True)
        path(self,'handle',(34,16),('A',10,10,True,(34,36)))
        ellipse(self,'window',22,27,3,4)
        contacts(self)
