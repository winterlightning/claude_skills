"""A toothed blade rises through a table on two legs and a brace; hub and doubled leg walls omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fdf751a4-9ff0-4914-a53d-36f32fa34dc8'
SOURCE_PATH = 'pictographic-primitives/tools/sawmill table_fdf751a4-9ff0-4914-a53d-36f32fa34dc8.svg'
AUTHOR = 'gpt-6'

class TableSaw(Solo48):
    icon_id = 'table-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('table saw', 'saw', 'blade', 'workbench', 'woodworking', 'sawmill', 'cutting', 'power tool')

    def build(self) -> None:

        def box(n,x,y,w,h,r=0):
            if not r:
                self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                a,b=pts[j],pts[(j+1)%8]
                if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
                else:self.add_line(n+str(j),a,b)
            self.add_contour(n,*[n+str(j) for j in range(8)],closed=True)

        box('table',6,22,36,8)
        self.add_polyline('blade',(12,22),(12,14),(18,14),(16,8),(24,12),(26,6),(32,12),(36,10),(34,22))
        self.relate('connect','blade','table')
        for n,x in [('left',10),('right',38)]:
            self.add_line(n+'-leg',(x,30),(x,42))
            self.relate('connect',n+'-leg','table')
        self.add_line('brace',(10,38),(38,38))
        self.relate('connect','brace','left-leg')
        self.relate('connect','brace','right-leg')
