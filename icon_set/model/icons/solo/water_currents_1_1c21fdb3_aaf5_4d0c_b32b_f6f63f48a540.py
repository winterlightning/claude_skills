'Water currents: two reflected outward current arrows above two smooth, equally spaced wave runs; reduce the crowded scallops.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c21fdb3-aaf5-4d0c-b32b-f6f63f48a540'
SOURCE_PATH = 'pictographic-primitives/weather/water currents 1_1c21fdb3-aaf5-4d0c-b32b-f6f63f48a540.svg'
AUTHOR = 'gpt-6'

class WaterCurrents1(Solo48):
    icon_id = 'water-currents-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('water', 'currents', 'weather')

    def build(self) -> None:
        for name,s in (('left',1),('right',-1)):
            def p(x,y):return (x,y) if s==1 else (48-x,y)
            self.add_bezier(name+'-current',p(19,19),(p(19,14),p(15,12),p(4,12)))
            self.add_polyline(name+'-head',p(8,8),p(4,12),p(8,16))
            self.relate('connect',name+'-current',name+'-head')
        # Equal smooth wave runs separated vertically by eleven units.
        for j,y in enumerate((29,40)):
            parts=[]
            for k,x in enumerate((4,14,24,34)):
                name=f'wave-{j}-{k}'
                self.add_bezier(name,(x,y-2),((x+2,y-2),(x+3,y),(x+5,y)),((x+7,y),(x+8,y-2),(x+10,y-2)))
                parts.append(name)
            self.add_contour(f'wave-{j}',*parts)
