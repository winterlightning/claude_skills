"""Revision of paired-cherries. The rejected cherries looked like tiny ringed dots. Enlarged both equal fruits and gave their two stems a broader arch like the original.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""Pair of Cherries.
Symbol plan: Two equal cherry circles and converging stems. Bounds (4,8)-(44,40).
Construction reference: Supplied cherries; Lucide cherry rounded fruits and shared stem junction.
Reduction: Small top notches omitted; straight and curved stem distinction retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9112d945-93a9-56ad-a055-c776cbd4df3b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__paired-cherries/20260927T074149Z-thuan-mac-1/reference/cherry_9112d945-93a9-56ad-a055-c776cbd4df3b.svg'
AUTHOR = 'gpt-6'

class PairedCherries(Solo48):
    icon_id = 'paired-cherries'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('paired', 'cherries')

    def build(self):
        for name,x in [('left',12),('right',36)]: self.loop(name,x,32,8)
        join=(24,8)
        self.add_line('left-stem',(12,24),join)
        self.add_bezier('right-stem',join,((33,10),(36,17),(36,24)))
        for stem,fruit in [('left-stem','left'),('right-stem','right')]:
            self.relate('connect',stem,fruit)
        self.relate('connect','left-stem','right-stem')

    def path(self, name, start, commands, closed=False):
        members=[]
        for j,c in enumerate(commands):
            tag=f'{name}-{j}'
            if len(c)==2:self.add_line(tag,start,c);start=c
            else:self.add_bezier(tag,start,c);start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def loop(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-r',(x,y-ry),(x,y+ry),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-l',(x,y+ry),(x,y-ry),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-r',name+'-l',closed=True)

    def steam(self,x,top,bottom,name):
        mid=(top+bottom)//2
        self.add_bezier(name,(x+1,top),((x-2,top+2),(x-2,mid),(x,mid)),((x+2,mid),(x+2,bottom-2),(x-1,bottom)))
