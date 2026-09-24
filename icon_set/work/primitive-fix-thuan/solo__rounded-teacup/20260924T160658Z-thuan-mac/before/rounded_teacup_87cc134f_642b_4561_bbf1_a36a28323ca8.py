'Simple Hot Beverage Cup.\nPlan and review: Retained broad rounded cup, straight rim and right loop handle. No steam or contents invented.\nKeyshape: HRECT_M, exact SOLO48 envelope.\nConstruction reference: Lucide coffee: attached loop handle, open interior and simple cup body.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87cc134f-642b-4561-bbf1-a36a28323ca8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tea_87cc134f-642b-4561-bbf1-a36a28323ca8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-teacup'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rounded', 'teacup')

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

        path('cup',(4,10),[(32,10),(32,24),((18,38),14,14,True),((4,24),14,14,True),(4,10)],True)
        path('handle',(32,14),[((32,30),12,8,True)]);self.relate('connect','handle','cup')
