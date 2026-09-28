'Simple Round Food Bowl.\nPlan and review: Retained broad oval rim and deep rounded empty bowl; no foot, handle or contents added.\nKeyshape: HRECT_M, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f74b4ddd-c576-4413-b6c0-33a9bb6e16fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bowl_f74b4ddd-c576-4413-b6c0-33a9bb6e16fe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-round-food-bowl'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('simple', 'round', 'food', 'bowl')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        path('rim',(4,16),[((44,16),20,6,True),((4,16),20,6,True)],True)
        curve('bowl',(4,16),((4,32),(12,38),(24,38)),((36,38),(44,32),(44,16)));self.relate('connect','bowl','rim')
