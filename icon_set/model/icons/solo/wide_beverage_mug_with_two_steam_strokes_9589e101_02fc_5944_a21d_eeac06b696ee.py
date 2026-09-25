"""Hot Steaming Beverage Cup.

Plan: Wide rounded mug with right handle and two sinuous steam strokes. Bounds (6,6)-(42,42); repeated steam shares shape and spacing.
Construction reference: Lucide coffee: rounded cup and steam rhythm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9589e101-02fc-5944-a21d-eeac06b696ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/coffee cup hot_9589e101-02fc-5944-a21d-eeac06b696ee.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'wide-beverage-mug-with-two-steam-strokes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    categories = ("drinks", "primitives")
    aliases = ()
    keywords = ('hot', 'steaming', 'beverage', 'cup')

    def build(self):
        path(self,'mug',(6,24),('L',(32,24)),('L',(32,36)),('A',6,6,True,(26,42)),('L',(12,42)),('A',6,6,True,(6,36)),('L',(6,24)),closed=True)
        path(self,'handle',(32,24),('A',10,6,True,(32,36)))
        for i,x in enumerate((14,26)):
         path(self,f'steam-{i}',(x,6),('A',1,2,True,(x,10)),('A',1,2,False,(x,14)))
        contacts(self)
