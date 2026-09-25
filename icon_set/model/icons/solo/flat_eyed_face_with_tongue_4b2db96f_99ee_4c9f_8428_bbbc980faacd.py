'Face With Stuck Out Tongue.\nPlan and review: Retained round face, horizontal eyes and broad hanging tongue. Omitted central tongue crease to protect its opening.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b2db96f-99ee-4c9f-8428-bbbc980faacd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face tongue money_4b2db96f-99ee-4c9f-8428-bbbc980faacd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flat-eyed-face-with-tongue'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('flat', 'eyed', 'face', 'with', 'tongue')

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
        self.add_line('eye-left',(15,17),(19,17));self.add_line('eye-right',(29,17),(33,17))
        path('tongue',(19,26),[(29,26),(29,30),((19,30),5,5,True),(19,26)],True)
