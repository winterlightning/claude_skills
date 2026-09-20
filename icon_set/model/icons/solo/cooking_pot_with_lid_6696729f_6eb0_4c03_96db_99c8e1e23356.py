'Cooking Pot with Lid.\nPlan and review: Retained cylindrical vessel, elliptical lid and attached knob; reduced the knob to a stem.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cooking-pot and cylinder: simple lid above cylindrical vessel.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6696729f-6eb0-4c03-96db-99c8e1e23356'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lid_6696729f-6eb0-4c03-96db-99c8e1e23356.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cooking-pot-with-lid'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cooking', 'pot', 'with', 'lid')

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

        path('lid',(4,24),[((44,24),20,6,True),((4,24),20,6,True)],True)
        path('body',(4,24),[(4,34),((44,34),20,6,False),(44,24)]);self.relate('connect','lid','body')
        self.add_line('knob',(24,8),(24,18));self.relate('connect','knob','lid')
