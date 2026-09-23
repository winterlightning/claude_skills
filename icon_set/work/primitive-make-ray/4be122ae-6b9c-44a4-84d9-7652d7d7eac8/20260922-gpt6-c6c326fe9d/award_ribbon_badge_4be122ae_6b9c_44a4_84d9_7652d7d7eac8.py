from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4be122ae-6b9c-44a4-84d9-7652d7d7eac8'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/award_4be122ae-6b9c-44a4-84d9-7652d7d7eac8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'award-ribbon-badge'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('award', 'ribbon', 'badge')

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
        # Plan: VRECT_L extremes 8,4 to 40,44; circular medal with exact 6-8-10 attachment points and mirrored swallowtail ribbons.
        axis=24
        left=(16,20); right=(32,20)
        self.add_arc('medal-top',left,right,radius_x=10,large_arc=True)
        self.add_arc('medal-bottom',right,left,radius_x=10)
        self.add_contour('medal','medal-top','medal-bottom',closed=True)
        left_tail=[left,(8,38),(15,36),(18,44),(24,30)]
        tail=left_tail+[(48-x,y) for x,y in reversed(left_tail[:-1])]
        self.add_polyline('ribbons',*tail)
        self.relate('connect','ribbons','medal')
