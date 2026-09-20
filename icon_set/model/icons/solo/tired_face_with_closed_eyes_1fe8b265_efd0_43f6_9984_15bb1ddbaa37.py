'Sad Face With Closed Eyes.\nPlan and review: Retained two down-curved closed eyes and short frown in a circular face.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fe8b265-efd0-43f6-9984-15bb1ddbaa37'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face tired_1fe8b265-efd0-43f6-9984-15bb1ddbaa37.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tired-face-with-closed-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('tired', 'face', 'with', 'closed', 'eyes')

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

        circle('head',24,24,20)
        for j,x in enumerate((17,31)):self.add_arc(f'eye-{j}',(x-3,20),(x+3,20),radius_x=3,radius_y=2,sweep=False)
        self.add_arc('frown',(20,33),(28,33),radius_x=4,radius_y=3,sweep=True)
