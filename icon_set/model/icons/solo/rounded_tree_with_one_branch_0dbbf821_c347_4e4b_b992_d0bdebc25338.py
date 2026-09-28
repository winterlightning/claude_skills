'A rounded birch crown with one upper lobe and an upright trunk with a right branch. VRECT_L fits tall tree; canopy symmetric about24 and branch intentionally right only. Smooth Bezier crown owns shared lower trunk node. Lucide tree-deciduous teaches a lobed canopy and simple trunk. Retain source arrangement; no extra bark or leaves.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0dbbf821-c347-4e4b-b992-d0bdebc25338'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/birch_0dbbf821-c347-4e4b-b992-d0bdebc25338.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'rounded-tree-with-one-branch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Rounded Tree with One Branch']
    keywords = ['tree', 'birch', 'trunk', 'branch', 'crown', 'nature', 'plant']
    def build(self):
        def path(name,start,steps,closed=False):
            point=start; members=[]
            for i,step in enumerate(steps):
                pid=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(pid,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(pid,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(pid)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True),((x,y-r),r,r,True)],True)
        self.add_bezier('crown-left',(24,34),((15,34),(8,29),(8,22)),((8,17),(14,16),(14,14)),((14,8),(18,4),(24,4)))
        self.add_bezier('crown-right',(24,4),((30,4),(34,8),(34,14)),((34,16),(40,17),(40,22)),((40,29),(33,34),(24,34)))
        self.add_contour('crown','crown-left','crown-right',closed=True)
        self.add_polyline('trunk',(24,18),(24,28),(24,34),(24,44))
        self.add_line('branch',(24,28),(30,22))
        self.relate('connect','trunk','branch')
        self.relate('connect','trunk','crown')
