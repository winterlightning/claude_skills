"""A heart blossom and paired leaves grow from a rounded vase; veins omitted.

Construction references: Lucide rose, heart, gem and hand as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3'
SOURCE_PATH = 'pictographic-primitives/romance/dating flowers vase_c6a8f9b5-4b58-5f76-86c0-ef27a854f0e3.svg'
AUTHOR = 'gpt-6'


class HeartFlowerInVase(Solo48):
    icon_id = 'heart-flower-in-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "romance"
    categories = ("primitives", "romance")
    aliases = ()
    keywords = ('heart', 'flower', 'vase', 'romance', 'plant', 'decoration')

    def build(self) -> None:
        # Mirrored heart lobes share radius 6 around the vertical axis.
        self.add_arc('lobe-l', (24,9), (14,9), radius_x=5, sweep=False)
        self.add_arc('shoulder-l', (14,9), (18,16), radius_x=10, sweep=False)
        self.add_line('tip-1',(18,16),(24,21))
        self.add_line('tip-2',(24,21),(30,16))
        self.add_arc('shoulder-r', (30,16), (34,9), radius_x=10, sweep=False)
        self.add_arc('lobe-r', (34,9), (24,9), radius_x=5, sweep=False)
        self.add_contour('bloom','lobe-l','shoulder-l','tip-1','tip-2','shoulder-r','lobe-r',closed=True)
        self.add_line('stem',(24,21),(24,30))
        self.relate('connect','bloom','stem')
        for side in (-1,1):
            name='leaf-left' if side<0 else 'leaf-right'
            self.add_arc(name+'-a',(24,30),(24+side*16,20),radius_x=16,radius_y=10,sweep=side<0)
            self.add_arc(name+'-b',(24+side*16,20),(24,30),radius_x=16,radius_y=10,sweep=side<0)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
            self.relate('connect',name,'stem')
        self.add_line('vase-lip',(18,30),(30,30))
        self.add_arc('vase-r',(30,30),(30,44),radius_x=7,radius_y=7)
        self.add_line('vase-base',(30,44),(18,44))
        self.add_arc('vase-l',(18,44),(18,30),radius_x=7,radius_y=7)
        self.add_contour('vase','vase-lip','vase-r','vase-base','vase-l',closed=True)
        self.relate('connect','stem','vase')
        for name in ('leaf-left','leaf-right'):
            self.relate('connect',name,'vase')
        self.relate('connect','leaf-left','leaf-right')
