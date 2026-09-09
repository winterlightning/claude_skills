"""Beetle with true elliptical wing case and exact shared attachment points. VRECT_XL (5,2)-(43,46). Lucide bug informs bilateral legs and central seam; replaced straight body sides and pinched base."""
# Variant of beetle; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82fb3003-56b5-5594-a35c-f4552fbc42d8'
SOURCE_PATH = 'pictographic-primitives/animals/insect_82fb3003-56b5-5594-a35c-f4552fbc42d8.svg'
AUTHOR = 'gpt-6'

class BeetleVariant2(Solo48):
    icon_id = 'beetle-v2'
    variant_of = 'beetle'
    variant_label = 'Oval wing case'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('beetle', 'bug', 'insect', 'shell', 'antennae', 'legs', 'nature', 'wildlife')

    def build(self) -> None:
        # Oval wing case (rx 10, ry 15); exact shared leg/head attachment points.
        # VRECT_XL centerline extremes (5,2)-(43,46).
        self.add_arc('head-left',(16,22),(24,8),radius_x=8,radius_y=14)
        self.add_arc('head-right',(24,8),(32,22),radius_x=8,radius_y=14)
        self.add_contour('head','head-left','head-right')
        self.add_arc('shell-top-left',(16,22),(24,16),radius_x=10,radius_y=15)
        self.add_arc('shell-top-right',(24,16),(32,22),radius_x=10,radius_y=15)
        self.add_arc('shell-right-upper',(32,22),(34,31),radius_x=10,radius_y=15)
        self.add_arc('shell-right-lower',(34,31),(32,40),radius_x=10,radius_y=15)
        self.add_arc('shell-base-right',(32,40),(24,46),radius_x=10,radius_y=15)
        self.add_arc('shell-base-left',(24,46),(16,40),radius_x=10,radius_y=15)
        self.add_arc('shell-left-lower',(16,40),(14,31),radius_x=10,radius_y=15)
        self.add_arc('shell-left-upper',(14,31),(16,22),radius_x=10,radius_y=15)
        self.add_contour('shell','shell-top-left','shell-top-right','shell-right-upper','shell-right-lower','shell-base-right','shell-base-left','shell-left-lower','shell-left-upper',closed=True)
        self.relate('connect','head','shell')
        self.add_line('seam',(24,16),(24,46))
        self.relate('connect','shell','seam')
        self.add_line('antenna-left',(24,8),(16,2))
        self.add_line('antenna-right',(24,8),(32,2))
        self.relate('connect','antenna-left','head')
        self.relate('connect','antenna-right','head')
        self.relate('connect','antenna-left','antenna-right')
        for side,upper,middle,lower,end in (('left',(16,22),(14,31),(16,40),5),('right',(32,22),(34,31),(32,40),43)):
            for label,start,y in (('upper',upper,17),('middle',middle,31),('lower',lower,45)):
                name=f'{label}-{side}'
                self.add_line(name,start,(end,y))
                self.relate('connect','shell',name)
                if label=='upper':
                    self.relate('connect','head',name)
