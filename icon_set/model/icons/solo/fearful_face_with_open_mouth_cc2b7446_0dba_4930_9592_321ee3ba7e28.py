'Fearful Expression Face.\nPlan and review: Retained raised inner brows, paired eyes and open fearful mouth. Reduced large eye circles to dots; used a small circular mouth to preserve spacing.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc2b7446-0dba-4930-9592-321ee3ba7e28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face fearful_cc2b7446-0dba-4930-9592-321ee3ba7e28.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fearful-face-with-open-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('fearful', 'face', 'with', 'open', 'mouth')

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
        self.add_line('brow-left',(16,16),(20,14));self.add_line('brow-right',(28,14),(32,16))
        self.add_dot('eye-left',(16,24));self.add_dot('eye-right',(32,24))
        circle('mouth',24,33,2)
