from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64ed5636-8e1f-4fbd-8a7a-ba14ed99b301'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/auto setting column width_64ed5636-8e1f-4fbd-8a7a-ba14ed99b301.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-column-width-resizing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('horizontal', 'column', 'width', 'resizing')

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
        # Plan: SQUARE extremes 6,6 to 42,42; equal two-cell columns below mirrored width arrow, with ten units vertical clearance.
        for index,x in enumerate((6,29)):
            self.add_polyline(f'column-{index}',(x,24),(x+13,24),(x+13,33),(x+13,42),(x,42),(x,33),closed=True)
            self.add_line(f'divider-{index}',(x,33),(x+13,33))
            self.relate('connect',f'column-{index}',f'divider-{index}')
        self.add_line('width',(6,10),(42,10))
        for side in (0,1):
            def p(x,y): return (48-x if side else x,y)
            self.add_polyline(f'arrow-{side}',p(10,6),p(6,10),p(10,14))
            self.relate('connect','width',f'arrow-{side}')
