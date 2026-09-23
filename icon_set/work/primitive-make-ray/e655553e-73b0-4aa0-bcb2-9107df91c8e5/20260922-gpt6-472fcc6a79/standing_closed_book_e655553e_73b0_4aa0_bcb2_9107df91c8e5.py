from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e655553e-73b0-4aa0-bcb2-9107df91c8e5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/book library shelf 1_e655553e-73b0-4aa0-bcb2-9107df91c8e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-closed-book'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('standing', 'closed', 'book')

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
        # Plan: VRECT_L extremes8,4 to40,44; upright cover and round lower-left binding with horizontal page edge.
        self.add_line('spine',(8,38),(8,9))
        self.add_arc('tl',(8,9),(13,4),radius_x=5)
        self.add_line('top',(13,4),(35,4))
        self.add_arc('tr',(35,4),(40,9),radius_x=5)
        self.add_line('right-top',(40,9),(40,32))
        self.add_line('right-bottom',(40,32),(40,44))
        self.add_line('bottom',(40,44),(14,44))
        self.add_arc('binding-bottom',(14,44),(8,38),radius_x=6)
        self.add_contour('cover','spine','tl','top','tr','right-top','right-bottom','bottom','binding-bottom',closed=True)
        self.add_arc('binding-top',(8,38),(14,32),radius_x=6)
        self.add_line('page-edge',(14,32),(40,32))
        self.add_contour('pages','binding-top','page-edge')
        self.relate('connect','cover','pages')
