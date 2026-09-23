from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b55ec75b-a606-4e27-845e-2f640329c00f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/broken tab remove_b55ec75b-a606-4e27-845e-2f640329c00f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'remove-broken-tab-section'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('remove', 'broken', 'tab', 'section')

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
        # Plan: HRECT_M extremes4,10 to44,38; two separated tab pieces share translated zigzag fracture; X remains in right fragment.
        self.add_line('left-top',(8,10),(20,10))
        self.add_line('left-break-upper',(20,10),(14,24))
        self.add_line('left-break-lower',(14,24),(20,38))
        self.add_line('left-bottom',(20,38),(8,38))
        self.add_arc('left-bl',(8,38),(4,34),radius_x=4)
        self.add_line('left-wall',(4,34),(4,14))
        self.add_arc('left-tl',(4,14),(8,10),radius_x=4)
        self.add_contour('main','left-top','left-break-upper','left-break-lower','left-bottom','left-bl','left-wall','left-tl',closed=True)
        self.add_line('right-top',(30,10),(40,10))
        self.add_arc('right-tr',(40,10),(44,14),radius_x=4)
        self.add_line('right-wall',(44,14),(44,34))
        self.add_arc('right-br',(44,34),(40,38),radius_x=4)
        self.add_line('right-bottom',(40,38),(30,38))
        self.add_line('right-break-lower',(30,38),(24,24))
        self.add_line('right-break-upper',(24,24),(30,10))
        self.add_contour('fragment','right-top','right-tr','right-wall','right-br','right-bottom','right-break-lower','right-break-upper',closed=True)
        self.add_polyline('cross-a',(30,20),(34,24),(38,28))
        self.add_polyline('cross-b',(30,28),(34,24),(38,20))
        self.relate('connect','cross-a','cross-b')
