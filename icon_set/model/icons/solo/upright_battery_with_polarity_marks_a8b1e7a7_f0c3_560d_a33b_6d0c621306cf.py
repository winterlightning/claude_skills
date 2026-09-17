"""Battery with Plus and Minus Signs.

Symbol plan: Upright battery with raised terminal and polarity marks. Lucide battery informs rounded body. Drop central division to keep both polarity marks legible.
Keyshape VRECT_M; exact visible bounds (8, 2, 40, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8b1e7a7-f0c3-560d-a33b-6d0c621306cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/fossil energy battery_a8b1e7a7-f0c3-560d-a33b-6d0c621306cf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'upright-battery-with-polarity-marks'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('battery', 'with', 'plus', 'and', 'minus', 'signs')

    def build(self):
        self.rect('body',10,12,28,32,3)
        self.add_polyline('terminal',(18,12),(18,4),(30,4),(30,12))
        self.relate('connect','body','terminal')
        self.graph([('plus-up',(24,21),(24,24)),('plus-down',(24,24),(24,27)),('plus-left',(21,24),(24,24)),('plus-right',(24,24),(27,24))])
        self.add_line('minus',(21,35),(27,35))

    def rect(self,name,x,y,w,h,r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8];part=f'{name}-{i}'
            if start==end: continue
            if i%2:self.add_arc(part,start,end,radius_x=r)
            else:self.add_line(part,start,end)
            names.append(part)
        self.add_contour(name,*names,closed=True)

    def graph(self,edges):
        for name,a,b in edges:self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}:self.relate('connect',name,other)
