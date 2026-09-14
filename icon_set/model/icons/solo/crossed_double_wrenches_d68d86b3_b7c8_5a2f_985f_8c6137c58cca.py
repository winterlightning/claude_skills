"""Two double-ended wrenches cross in an X with four outward open jaws; narrow doubled shafts reduced to single crossing strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd68d86b3-b7c8-5a2f-985f-8c6137c58cca'
SOURCE_PATH = 'pictographic-primitives/tools/tools wrench_d68d86b3-b7c8-5a2f-985f-8c6137c58cca.svg'
AUTHOR = 'gpt-6'

class CrossedDoubleWrenches(Solo48):
    icon_id = 'crossed-double-wrenches'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('wrenches', 'wrench', 'crossed', 'spanner', 'repair', 'maintenance', 'mechanic', 'tools')

    def build(self) -> None:
        for name,mx,my in [('top-left',False,False),('top-right',True,False),('bottom-left',False,True),('bottom-right',True,True)]:
            def point(x,y):
                return (48-x if mx else x,48-y if my else y)
            self.add_line(name+'-lip',point(15,6),point(15,8))
            self.add_arc(name+'-jaw',point(15,8),point(6,11),radius_x=5,large_arc=True,sweep=mx==my)
            self.add_contour(name,name+'-lip',name+'-jaw')
        self.add_line('shaft-a',(14,15),(34,33))
        self.add_line('shaft-b',(34,15),(14,33))
        self.relate('connect','shaft-a','top-left')
        self.relate('connect','shaft-a','bottom-right')
        self.relate('connect','shaft-b','top-right')
        self.relate('connect','shaft-b','bottom-left')
        self.relate('connect','shaft-a','shaft-b')
