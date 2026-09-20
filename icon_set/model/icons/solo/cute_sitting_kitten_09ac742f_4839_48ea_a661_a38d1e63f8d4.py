'Cute Sitting Kitten.\nPlan and review: Retained pointed ears, rounded head, seated body and two foreleg divisions. Omitted tiny nose detail.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cat: pointed ears and rounded face; source upright body and paw divisions retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09ac742f-4839-48ea-a661-a38d1e63f8d4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kitty_09ac742f-4839-48ea-a661-a38d1e63f8d4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cute-sitting-kitten'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cute', 'sitting', 'kitten')

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

        path('head',(8,18),[(8,4),(18,10),(30,10),(40,4),(40,18),((8,18),16,12,True)],True)
        curve('body',(14,29),((10,34),(10,40),(14,44)))
        curve('body-right',(34,29),((38,34),(38,40),(34,44)))
        self.add_line('base',(14,44),(34,44));self.relate('connect','body','base');self.relate('connect','body-right','base');self.relate('connect','head','body');self.relate('connect','head','body-right')
        for j,x in enumerate((20,28)): self.add_line(f'paw-{j}',(x,36),(x,44));self.relate('connect',f'paw-{j}','base')
        self.add_dot('eye-left',(17,19));self.add_dot('eye-right',(31,19))
