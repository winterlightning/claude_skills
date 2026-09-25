"""Pour Over Coffee Brewing Process.

Plan: Pour-over filter, falling drop and handled cup. Bounds (8,4)-(40,44); three vertically separated stages. Drop simplified to a short round stroke.
Construction reference: Lucide funnel and coffee: filter and cup construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'bf6b8c32-fb1f-56f9-ac2e-42277a8fef9d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee drip_bf6b8c32-fb1f-56f9-ac2e-42277a8fef9d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'pour-over-filter-dripping-into-cup'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('pour', 'over', 'coffee', 'brewing', 'process')

    def build(self):
        poly(self,'filter',(8,4),(36,4),(26,14),(18,14),(8,4))
        self.add_dot('drop',(22,23))
        path(self,'cup',(8,32),('L',(30,32)),('L',(30,40)),('A',4,4,True,(26,44)),('L',(12,44)),('A',4,4,True,(8,40)),('L',(8,32)),closed=True)
        path(self,'handle',(30,32),('A',10,4,True,(30,40)))
        contacts(self)
