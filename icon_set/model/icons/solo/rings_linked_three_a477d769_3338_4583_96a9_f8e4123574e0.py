"""Three equal rings connected through a shared junction. Lucide share-2 informs equal circles and scoped connector contacts; the source Y-junction is retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a477d769-3338-4583-96a9-f8e4123574e0'
SOURCE_PATH = 'pictographic-primitives/symbol/ripple_a477d769-3338-4583-96a9-f8e4123574e0.svg'
AUTHOR = 'gpt-6'


class RingsLinkedThree(Solo48):
    icon_id = 'rings-linked-three'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('share', 'nodes', 'network', 'connect', 'ripple', 'molecule', 'rings', 'link')

    def build(self) -> None:

        rings=[('left',(6,24),(16,24)),('upper',(34,15),(40,7)),('lower',(34,33),(40,41))]
        for name,a,b in rings:
            self.add_arc(name+'-first',a,b,radius_x=5)
            self.add_arc(name+'-second',b,a,radius_x=5)
            self.add_contour(name,name+'-first',name+'-second',closed=True)
        self.add_line('link-left',(16,24),(24,24))
        self.add_line('link-upper',(24,24),(34,15))
        self.add_line('link-lower',(24,24),(34,33))
        for name in ('left','upper','lower'):self.relate('connect',name,'link-'+name)
        self.relate('connect','link-left','link-upper')
        self.relate('connect','link-left','link-lower')
        self.relate('connect','link-upper','link-lower')
