'A long vertical arrow points down. VRECT_L gives the shaft its vertical emphasis, extremes 8,4,40,44. Head arms mirror about x24 and share the shaft endpoint. Lucide arrow-down supplies a single shaft and continuous V construction; no detail omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ff48b11-01dd-493a-b53d-b03042d38b5f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angles down_6ff48b11-01dd-493a-b53d-b03042d38b5f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'long-downward-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Long Downward Arrow',)
    keywords = ('arrow', 'down', 'direction', 'vertical', 'pointer', 'move', 'navigation')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[];point=start
            for j,step in enumerate(steps):
                member=f"{name}-{j}"
                if len(step)==2:self.add_line(member,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        tip=(24,44)
        self.add_polyline('head',(8,28),tip,(40,28))
        self.add_line('shaft',(24,4),tip)
        self.relate('connect','head','shaft')
