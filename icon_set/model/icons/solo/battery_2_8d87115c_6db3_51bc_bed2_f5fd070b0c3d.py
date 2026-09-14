'Battery placeholder'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8d87115c-6db3-51bc-bed2-f5fd070b0c3d'
SOURCE_PATH = 'icons-json/photography/battery 2_8d87115c-6db3-51bc-bed2-f5fd070b0c3d.json'
AUTHOR = 'gpt-6'

class Battery2(Solo48):
    icon_id = 'battery-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('battery', 'photography')

    def build(self) -> None:
        # VRECT_L terminal and rounded body. Divider omitted to give both polarity marks air.
        points=((14,10),(18,10),(18,4),(30,4),(30,10),(34,10))
        for i,(a,b) in enumerate(zip(points,points[1:])): self.add_line('terminal-'+str(i),a,b)
        self.add_arc('tr',(34,10),(40,16),radius_x=6)
        self.add_line('right',(40,16),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('base',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,16))
        self.add_arc('tl',(8,16),(14,10),radius_x=6)
        self.add_contour('battery',*('terminal-'+str(i) for i in range(5)),'tr','right','br','base','bl','left','tl',closed=True)
        self.add_polyline('plus-h',(20,21),(24,21),(28,21))
        self.add_polyline('plus-v',(24,17),(24,21),(24,25))
        self.relate('connect','plus-h','plus-v')
        self.add_line('minus',(20,35),(28,35))
