'Elderly Man with Glasses and Mustache.\nPlan and review: Retained bald circular head, linked round spectacles and two-lobed mustache. Omitted ears and opened the mustache outline to avoid crowding. Small spectacle circles use the existing diameter6 circular-hole exception; no rules changed.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'afe3a8ac-8b02-4b7b-a08f-69ef4ae314dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/great grandfather_afe3a8ac-8b02-4b7b-a08f-69ef4ae314dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bald-head-with-round-glasses-and-mustache'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bald', 'head', 'with', 'round', 'glasses', 'and', 'mustache')

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
        circle('glass-left',17,19,3);circle('glass-right',31,19,3)
        self.add_line('bridge',(20,19),(28,19))
        for s in ('left','right'):self.relate('connect','bridge','glass-'+s)
        curve('mustache',(17,32),((18,30),(22,30),(24,33)),((26,30),(30,30),(31,32)))
