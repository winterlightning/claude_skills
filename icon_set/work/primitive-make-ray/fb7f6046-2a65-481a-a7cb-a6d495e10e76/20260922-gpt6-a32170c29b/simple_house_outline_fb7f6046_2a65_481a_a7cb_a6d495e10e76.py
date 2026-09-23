from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fb7f6046-2a65-481a-a7cb-a6d495e10e76'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/attic_fb7f6046-2a65-481a-a7cb-a6d495e10e76.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-house-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('simple', 'house', 'outline')

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
        # Plan: SQUARE extremes 6,6 to 42,42; mirrored pitched roof with projecting eaves and tangent round bottom corners.
        axis=24
        roof=[(12,24),(6,24),(axis,6),(42,24),(36,24)]
        for i in range(4): self.add_line(f'roof-{i+1}',roof[i],roof[i+1])
        self.add_line('right-wall',(36,24),(36,38))
        self.add_arc('right-foot',(36,38),(32,42),radius_x=4)
        self.add_line('floor',(32,42),(16,42))
        self.add_arc('left-foot',(16,42),(12,38),radius_x=4)
        self.add_line('left-wall',(12,38),(12,24))
        self.add_contour('outline','roof-1','roof-2','roof-3','roof-4','right-wall','right-foot','floor','left-foot','left-wall',closed=True)
