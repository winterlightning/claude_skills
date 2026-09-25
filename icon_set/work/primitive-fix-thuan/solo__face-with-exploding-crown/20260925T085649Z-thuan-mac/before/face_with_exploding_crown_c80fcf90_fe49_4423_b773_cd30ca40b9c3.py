'Exploding Head Face.\nPlan and review: Retained integrated exploding crown, dot eyes and open surprised mouth. Omitted eyebrow frill and simplified burst tips; enlarged the lower face to fit the mouth.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c80fcf90-fe49-4423-b773-cd30ca40b9c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face explode_c80fcf90-fe49-4423-b773-cd30ca40b9c3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'face-with-exploding-crown'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('face', 'with', 'exploding', 'crown')

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

        path('face',(8,28),[((40,28),16,16,False),(40,14),(30,14),(34,6),(28,10),(24,4),(20,10),(14,6),(18,14),(8,14),(8,28)],True)
        self.add_dot('eye-left',(17,25));self.add_dot('eye-right',(31,25));circle('mouth',24,33,2)
