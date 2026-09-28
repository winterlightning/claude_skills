"""An open right-angle jaw trap with zigzag teeth and a round hinge; dense teeth reduced to two per jaw."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84bf6aa6-6941-407f-ace3-91e52015b6ea'
SOURCE_PATH = 'pictographic-primitives/tools/roleplay game ability trap_84bf6aa6-6941-407f-ace3-91e52015b6ea.svg'
AUTHOR = 'gpt-6'

class OpenJawTrap(Solo48):
    icon_id = 'open-jaw-trap'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('trap', 'bear trap', 'jaws', 'teeth', 'snare', 'hunting', 'danger', 'game')

    def build(self) -> None:

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)

        self.add_polyline('upright',(6,36),(6,6),(18,6),(12,12),(18,18),(14,24),(12,30))
        self.add_polyline('lower',(18,36),(24,30),(30,36),(36,30),(42,36),(42,42),(12,42))
        circle('hinge',12,36,6)
        self.relate('connect','upright','hinge')
        self.relate('connect','lower','hinge')
