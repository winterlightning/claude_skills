"""The word AUTO in narrow rounded uppercase lettering.

Plan: Four hand-authored letters share top10 and baseline38. HRECT_M extremes(4,10)-(44,38). U and O use circular tangent ends; A and T retain deliberate corners. Width budget cannot accommodate four letters and all SOLO48 clearances. No useful Lucide match for this wordmark.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f89489d3-928e-4d8e-8a13-9ff760315c90'
SOURCE_PATH = 'pictographic-primitives/transportation/automatic drive gear_f89489d3-928e-4d8e-8a13-9ff760315c90.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'automatic-drive-gear'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('automatic', 'drive', 'gear')
    def build(self):
        self.add_polyline('a',(4,38),(4,24),(4,10),(12,10),(12,24),(12,34))
        self.add_line('a-bar',(4,24),(12,24));self.relate('connect','a','a-bar')
        self.add_arc('u-bottom',(12,34),(20,34),radius_x=4,sweep=False)
        self.add_polyline('u-right',(20,34),(20,10),(28,10),(36,10))
        self.relate('connect','a','u-bottom');self.relate('connect','u-bottom','u-right')
        self.add_line('t-stem',(28,10),(28,38));self.relate('connect','u-right','t-stem')
        self.add_polyline('o-left',(36,10),(36,38))
        self.add_arc('o-bowl',(36,10),(36,38),radius_x=8,radius_y=14)
        self.relate('connect','o-left','o-bowl');self.relate('connect','u-right','o-bowl');self.relate('connect','u-right','o-left')


    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def roundrect(self,name,x0,y0,x1,y1,r):
        nodes=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            else:self.add_line(f'{name}-{i}',a,b)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)
