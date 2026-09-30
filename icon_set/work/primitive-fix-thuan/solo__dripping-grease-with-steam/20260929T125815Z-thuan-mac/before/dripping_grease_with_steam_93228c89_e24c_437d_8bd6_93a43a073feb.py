'Dripping Grease with Steam.\nPlan and review: Retained upper bar, droplet and three heat/flow strokes. Upper object identity remains unspecified, as in the brief. Short outer curls flank a straight center mark; no invented vessel or modifier split.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93228c89-e24c-437d-8bd6-93a43a073feb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grease_93228c89-e24c-437d-8bd6-93a43a073feb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dripping-grease-with-steam'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('dripping', 'grease', 'with', 'steam')

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

        box('bar',8,4,40,12,2)
        path('drop',(24,20),[(30,26),((18,26),6,4,True),(24,20)],True)
        self.add_arc('wave-left',(14,39),(14,43),radius_x=2,radius_y=2,sweep=False)
        self.add_line('wave-center',(24,39),(24,44))
        self.add_arc('wave-right',(34,39),(34,43),radius_x=2,radius_y=2,sweep=True)
