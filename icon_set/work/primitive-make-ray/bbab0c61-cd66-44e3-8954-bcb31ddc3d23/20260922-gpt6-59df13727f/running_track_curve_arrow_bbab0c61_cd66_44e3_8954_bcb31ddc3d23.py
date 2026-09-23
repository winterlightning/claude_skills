from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bbab0c61-cd66-44e3-8954-bcb31ddc3d23'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/athletics running 1_bbab0c61-cd66-44e3-8954-bcb31ddc3d23.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'running-track-curve-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('running', 'track', 'curve', 'arrow')

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
        # Plan: HRECT_L extremes 4,8 to 44,40; nested semicircle lanes with shared center and horizontal tangents; right arrow retained.
        self.add_line('outer-top',(44,8),(20,8))
        self.add_arc('outer-turn',(20,8),(20,40),radius_x=16,sweep=False)
        self.add_line('outer-bottom',(20,40),(38,40))
        self.add_contour('outer','outer-top','outer-turn','outer-bottom')
        self.add_line('inner-top',(44,17),(20,17))
        self.add_arc('inner-turn',(20,17),(20,31),radius_x=7,sweep=False)
        self.add_line('inner-bottom',(20,31),(23,31))
        self.add_contour('inner','inner-top','inner-turn','inner-bottom')
        self.add_polyline('arrowhead',(34,25),(44,29),(34,32))
        self.add_line('shaft',(32,29),(44,29))
        self.relate('connect','shaft','arrowhead')
