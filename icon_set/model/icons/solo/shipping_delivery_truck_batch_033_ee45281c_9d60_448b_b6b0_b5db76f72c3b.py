"""Shipping Delivery Truck — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee45281c-9d60-448b-b6b0-b5db76f72c3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'shipping-delivery-truck-batch-033'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('shipping-delivery-truck',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Truck silhouette with sloping cab, cargo division and two equal wheels sharing top attachment nodes; extrema (4,10)-(44,38).

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x0,y0,x1,y1,r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8];eid=f'{name}-{i}';ids.append(eid)
                if i%2:self.add_arc(eid,p,q,radius_x=r)
                else:self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        self.add_polyline('body',(4,26),(4,10),(28,10),(28,18),(36,18),(44,26),(36,26),(28,26),(12,26),(4,26))
        self.add_line('cab-divider',(28,18),(28,26));self.relate('connect','body','cab-divider')
        for x in (12,36):
            self.add_arc(f'wheel-{x}-r',(x,26),(x,38),radius_x=6)
            self.add_arc(f'wheel-{x}-l',(x,38),(x,26),radius_x=6)
            self.add_contour(f'wheel-{x}',f'wheel-{x}-r',f'wheel-{x}-l',closed=True)
            self.relate('connect','body',f'wheel-{x}')
