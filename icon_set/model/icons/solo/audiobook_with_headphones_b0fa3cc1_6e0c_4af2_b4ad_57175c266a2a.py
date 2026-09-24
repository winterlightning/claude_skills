from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0fa3cc1-6e0c-4af2-b4ad-57175c266a2a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/audio book headphones_b0fa3cc1-6e0c-4af2-b4ad-57175c266a2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'audiobook-with-headphones'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('audiobook', 'with', 'headphones')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            part=f'{name}-{i}'; ids.append(part)
            if i%2: self.add_arc(part,pts[i],pts[(i+1)%8],radius_x=r)
            else: self.add_line(part,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: HRECT_L extremes 4,8 to 44,40; central open book nested under a round headphone arch and mirrored outward earcups.
        axis=24
        self.add_arc('headband',(10,22),(38,22),radius_x=14)
        for side,x,sweep in [('left',10,False),('right',38,True)]:
            self.add_arc(side+'-cup',(x,22),(x,38),radius_x=6,radius_y=8,sweep=sweep)
            self.add_line(side+'-inner',(x,38),(x,22))
            self.add_contour(side+'-ear',side+'-cup',side+'-inner',closed=True)
            self.relate('connect','headband',side+'-ear')
        self.add_polyline('book',(15,23),(24,27),(33,23),(33,36),(24,40),(15,36),closed=True)
        self.add_line('fold',(24,27),(24,40))
        self.relate('connect','book','fold')
