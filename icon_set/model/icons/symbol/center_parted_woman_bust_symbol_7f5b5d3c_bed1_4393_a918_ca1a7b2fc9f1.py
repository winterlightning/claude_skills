"""A front-facing woman bust with a circular face, center-parted hair continuing down each side and shoulders with a V-shaped neckline. Exclude the square frame.

Plan: Center-parted hair silhouette, circular lower face and V neckline. Omit duplicate inner hairline to keep it legible. Jaw radius7 at (16,10), neckline nodes (7,22) and (25,22): radius7 + centerline gap8 = distance15 by the 9-12-15 triangle; exact four-unit ink gap. Bounds (2,2)-(30,30).
Construction reference: Shared human_ref/user.svg: circular jaw and broad shoulders; source supplies parted hair and neckline."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1'
SOURCE_PATH = 'pictographic-primitives/other/square woman_7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1.svg'
SOURCE_ICON_IDS = ('7f5b5d3c-bed1-4393-a918-ca1a7b2fc9f1',)
AUTHOR = 'gpt-6'

class CenterPartedWomanBustSymbol(Symbol32):
    icon_id = 'center-parted-woman-bust-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('center', 'parted', 'woman', 'bust', 'symbol')

    def build(self) -> None:
        self.add_arc('jaw',(9,10),(23,10),radius_x=7,sweep=False)
        self.add_bezier('hair',(23,10),((23,6),(23,2),(20,2)),((18,2),(17,5),(16,5)),((15,5),(14,2),(12,2)),((9,2),(9,6),(9,10)))
        self.add_contour('head','jaw','hair',closed=True)
        for sign,name in ((1,'left'),(-1,'right')):
            def pt(x,y):return (16+sign*(x-16),y)
            self.add_bezier(name+'-hair',pt(9,10),(pt(9,12),pt(8,13),pt(7,14)))
            self.relate('connect','head',name+'-hair')
            self.add_bezier(name+'-shoulder',pt(2,30),(pt(3,26),pt(5,22),pt(7,22)))
        self.add_polyline('neckline',(7,22),(16,30),(25,22))
        self.relate('connect','neckline','left-shoulder')
        self.relate('connect','neckline','right-shoulder')
