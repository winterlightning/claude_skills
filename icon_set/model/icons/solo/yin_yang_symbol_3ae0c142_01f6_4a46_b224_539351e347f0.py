"""An outlined yin-yang with an S boundary and paired dots. Preserve both interlocking halves; no useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ae0c142-01f6-4a46-b224-539351e347f0'
SOURCE_PATH = 'pictographic-primitives/religion/taoism_3ae0c142-01f6-4a46-b224-539351e347f0.svg'
AUTHOR = 'gpt-6'

class YinYangSymbol(Solo48):
    icon_id = 'yin-yang-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('yin yang', 'taoism', 'circle', 'balance', 'symbol', 'duality')

    def oval(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Live circle radius20 on centerlines; boundary and dots share y=24.
        self.oval('outer',24,24,20)
        self.add_arc('boundary-left',(4,24),(24,24),radius_x=10)
        self.add_arc('boundary-right',(24,24),(44,24),radius_x=10,sweep=False)
        self.add_contour('boundary','boundary-left','boundary-right')
        self.relate('connect','outer','boundary')
        for x in (14,34):self.add_dot('dot-'+str(x),(x,24))
