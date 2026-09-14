'Compact car: round wheels, shared axle, smooth body and clear glazing. Reconstructed wheel openings remove the converted overlaps; Lucide car informs the body and wheel joins.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c02dbb47-ed6d-437d-9b09-015be167c963'
SOURCE_PATH = 'icons-json/transportation/car_c02dbb47-ed6d-437d-9b09-015be167c963.json'
AUTHOR = 'gpt-6'

class CarC02dbb47(Solo48):
    icon_id = 'car-c02dbb47'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'transportation')

    def build(self) -> None:
        # HRECT_L ink (2,6)-(46,42). Circular wheels share radius and axle height.
        # Roof corners and body are smooth; wheel tops form real wheel openings.
        self.add_bezier('rear',(8,35),((5,35),(4,32),(4,29)),((4,24),(7,21),(12,21)))
        self.add_line('rear-window',(12,21),(16,12))
        self.add_bezier('roof-left',(16,12),((16+4/3,9),(18,8),(21,8)))
        self.add_line('roof-a',(21,8),(25,8))
        self.add_line('roof-b',(25,8),(30,8))
        self.add_bezier('roof-right',(30,8),((33,8),(34,9),(35,12)))
        self.add_line('windscreen',(35,12),(38,21))
        self.add_bezier('front',(38,21),((42,22),(44,25),(44,29)),((44,32),(43,35),(40,35)))
        self.add_arc('front-wheel-top',(40,35),(30,35),radius_x=5,sweep=False)
        self.add_line('chassis',(30,35),(18,35))
        self.add_arc('rear-wheel-top',(18,35),(8,35),radius_x=5,sweep=False)
        self.add_contour('body','rear','rear-window','roof-left','roof-a','roof-b','roof-right','windscreen','front','front-wheel-top','chassis','rear-wheel-top',closed=True)
        self.add_polyline('waist',(12,21),(25,21),(38,21))
        self.relate('connect','waist','body')
        self.add_line('pillar',(25,8),(25,21))
        self.relate('connect','pillar','body')
        self.relate('connect','pillar','waist')
        for label,x in (('rear-wheel',13),('front-wheel',35)):
            self.add_arc(label+'-bottom',(x-5,35),(x+5,35),radius_x=5,sweep=False)
            self.relate('connect',label+'-bottom','body')
