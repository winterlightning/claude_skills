"""An inverted pentagram enclosed in a circle.

Plan: Outer circle center (24,24), radius20: radial extremes4 and44. Inverted star mirrored about x24, deliberately retains crossings. Integer polygon inside ring; no invented connect declarations at crossings. No useful Lucide match for this interlaced topology.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '815729c9-6c87-5e37-9c96-2f46aa26c6eb'
SOURCE_PATH = 'icon_set/work/todo-references/astrology pentagram_815729c9-6c87-5e37-9c96-2f46aa26c6eb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'astrology-pentagram'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('astrology', 'pentagram')
    def build(self):
        self.circle('ring',24,24,20)
        axis=24
        self.add_polyline('pentagram',(axis-11,10),(axis,40),(axis+11,10),(axis-16,29),(axis+16,29),closed=True)

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
