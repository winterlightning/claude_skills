from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bfd2ddb1-65f9-4a12-9c60-693529e81c85'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/browser page text_bfd2ddb1-65f9-4a12-9c60-693529e81c85.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'web-browser-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('web', 'browser', 'window')

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
        # Plan: SQUARE extremes6,6 to42,42; rounded browser window with single full-width upper header divider.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-header',(42,10),(42,16))
        self.add_line('right-body',(42,16),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left-body',(6,38),(6,16))
        self.add_line('left-header',(6,16),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('window','top','tr','right-header','right-body','br','bottom','bl','left-body','left-header','tl',closed=True)
        self.add_line('header',(6,16),(42,16))
        self.relate('connect','window','header')
