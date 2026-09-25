'Expandable Accordion Bellows.\nPlan and review: Retained accordion end panels and concertina folds. Reduced the fold count to four equally spaced dividers.\nKeyshape: HRECT_M, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69a16a1d-326d-4d41-8176-0941b0d6011f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/accordion_69a16a1d-326d-4d41-8176-0941b0d6011f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'accordion-expanded-bellows'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('accordion', 'expanded', 'bellows')

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

        path('outline',(8,10),[(12,10),(20,14),(28,10),(36,14),(40,14),((44,18),4,4,True),(44,30),((40,34),4,4,True),(36,34),(28,38),(20,34),(12,38),(8,38),((4,34),4,4,True),(4,14),((8,10),4,4,True)],True)
        for j,(x,t,b) in enumerate(((12,10,38),(20,14,34),(28,10,38),(36,14,34))):
         self.add_line(f'fold-{j}',(x,t),(x,b));self.relate('connect','outline',f'fold-{j}')
