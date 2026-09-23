from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9ee58df5-c0c8-43b8-ac76-5d6d676e8615'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/booklet_9ee58df5-c0c8-43b8-ac76-5d6d676e8615.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-paper-booklet'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('open', 'paper', 'booklet')

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
        # Plan: VRECT_M extremes10,4 to38,44; front booklet cover with raised angled back page joined at fold and top-right shoulder.
        self.add_line('front-top',(10,16),(34,16))
        self.add_arc('front-tr',(34,16),(38,20),radius_x=4)
        self.add_line('front-right',(38,20),(38,40))
        self.add_arc('front-br',(38,40),(34,44),radius_x=4)
        self.add_line('front-bottom',(34,44),(14,44))
        self.add_arc('front-bl',(14,44),(10,40),radius_x=4)
        self.add_line('front-left',(10,40),(10,16))
        self.add_contour('front','front-top','front-tr','front-right','front-br','front-bottom','front-bl','front-left',closed=True)
        self.add_polyline('back-page',(10,16),(30,4),(34,8),(34,16))
        self.relate('connect','front','back-page')
