"""Needle Sewing Fabric.

Plan: Needle crosses fabric diagonally; thread makes a broad loop beyond the eye. Eye reduced to a round tip and fabric corners simplified. Bounds (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8180ae35-1c75-59d8-ad57-ff9729f28bc5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__needle-sewing-fabric/20260927T164916Z-thuan-mac-1/reference/sewing sewing scarf_8180ae35-1c75-59d8-ad57-ff9729f28bc5.svg'
AUTHOR = 'gpt-6'

class NeedleSewingFabric(Solo48):
    icon_id = 'needle-sewing-fabric'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('needle', 'sewing', 'fabric')

    def build(self):
        # Split the cloth rim where the needle pierces it.
        self.add_line('fabric-top-left',(6,18),(26,18))
        self.add_line('fabric-top-right',(26,18),(30,18))
        self.add_line('fabric-right',(30,18),(30,42))
        self.add_line('fabric-bottom',(30,42),(6,42))
        self.add_line('fabric-left',(6,42),(6,18))
        self.add_contour('fabric','fabric-top-left','fabric-top-right','fabric-right','fabric-bottom','fabric-left',closed=True)
        self.add_line('needle-lower',(6,42),(26,18))
        self.add_line('needle-upper',(26,18),(36,6))
        self.add_arc('thread',(36,6),(42,12),radius_x=6)
        self.relate('connect','fabric','needle-lower','needle-upper')
        self.relate('connect','needle-lower','needle-upper')
        self.relate('connect','needle-upper','thread')
