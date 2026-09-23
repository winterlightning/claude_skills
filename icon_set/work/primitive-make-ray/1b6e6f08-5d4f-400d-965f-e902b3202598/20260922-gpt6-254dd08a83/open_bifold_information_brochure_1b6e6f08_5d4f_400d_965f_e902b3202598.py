from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1b6e6f08-5d4f-400d-965f-e902b3202598'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/brochure_1b6e6f08-5d4f-400d-965f-e902b3202598.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-bifold-information-brochure'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('open', 'bifold', 'information', 'brochure')

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
        # Plan: SQUARE extremes6,6 to42,42; mirrored sloping page edges share central fold; two text marks remain on left page only.
        axis=24
        self.add_polyline('pages',(6,6),(axis,10),(42,6),(42,38),(axis,42),(6,38),closed=True)
        self.add_line('fold',(axis,10),(axis,42))
        self.relate('connect','pages','fold')
        for i in range(2): self.add_line(f'text-{i}',(14,20+9*i),(16,21+9*i))
