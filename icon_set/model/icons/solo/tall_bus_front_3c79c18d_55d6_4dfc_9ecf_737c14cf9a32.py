'A tall front-facing bus has stacked glazing, paired lamps and short wheels. VRECT_L fits its upright silhouette. Body mirrors about x24; lamps and tyres share mirrored positions. Source supplies tall front and lights; Lucide bus-front supplies split horizontal glazing and attached wheel stubs. Omit narrow roof slot corners and tiny bumper seams.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c79c18d-55d6-4dfc-9ecf-737c14cf9a32'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/bus double_3c79c18d-55d6-4dfc-9ecf-737c14cf9a32.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'tall-bus-front'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Double Decker Bus Front View',)
    keywords = ('double', 'decker', 'bus', 'front', 'view')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        path('body',(12,4),[(36,4),((40,8),4,4,True),(40,14),(40,22),(40,36),((36,40),4,4,True),(31,40),(17,40),(12,40),((8,36),4,4,True),(8,22),(8,14),(8,8),((12,4),4,4,True)],True)
        for y in (14,22):
            self.add_line(f'glazing-{y}',(8,y),(40,y));self.relate('connect',f'glazing-{y}','body')
        for x in (17,31):
            self.add_dot(f'lamp-{x}',(x,31))
            self.add_line(f'tyre-{x}',(x,40),(x,44));self.relate('connect',f'tyre-{x}','body')
