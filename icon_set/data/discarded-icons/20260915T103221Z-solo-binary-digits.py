"""Two rows read 010 and 001. Lucide binary informs repeated rounded zero contours; shared columns preserve alignment.
Fresh SOLO48 geometry. Keyshape HRECT_L; bounds are resolved from the live contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abff6337-b854-552e-afe3-b89605887cad'
SOURCE_PATH = 'pictographic-primitives/programing/binary_abff6337-b854-552e-afe3-b89605887cad.svg'
AUTHOR = 'gpt-6'

class BinaryDigits(Solo48):
    icon_id = 'binary-digits'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/programming"
    aliases = ()
    keywords = ('binary', 'code', 'digits', 'data', 'zero', 'one', 'computing', 'bits')

    def build(self) -> None:
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def oval(name, x, y, rx, ry):
            self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        for row, digits in enumerate(('010','001')):
            y = 13 + row*22
            for col, digit in enumerate(digits):
                x = 7 + col*17
                name = f'digit-{row}-{col}'
                if digit == '0':
                    oval(name,x,y,3,5)
                else:
                    self.add_line(name,(x,y-5),(x,y+5))
