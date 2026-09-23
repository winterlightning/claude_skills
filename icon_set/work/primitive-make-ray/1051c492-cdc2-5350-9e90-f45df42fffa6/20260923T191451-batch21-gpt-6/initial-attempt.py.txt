"""A four-pane kitchen window rests on a projecting sill.
Construction reference: panels-top-left.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1051c492-cdc2-5350-9e90-f45df42fffa6'
SOURCE_PATH = 'icon_set/work/todo-references/kitchen window_1051c492-cdc2-5350-9e90-f45df42fffa6.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'kitchen-window'
    keyshape = Keyshape.SQUARE
    # Visible ink extremes: (4, 4, 44, 44).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('kitchen', 'window')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: equal panes share central mullion; sill is an 8-unit-high band.
        self.add_polyline('window',(10,34),(10,6),(38,6),(38,34))
        self.add_line('mullion',(24,6),(24,34))
        self.add_line('transom',(10,20),(38,20))
        self.add_polyline('sill',(6,34),(42,34),(42,42),(6,42),closed=True)
        self.relate('connect','window','mullion')
        self.relate('connect','window','transom')
        self.relate('connect','window','sill')
        self.relate('connect','mullion','transom')
        self.relate('connect','mullion','sill')
