'Simple House with Arched Door.\nPlan and review: Retained house silhouette, two upper window marks and arched entrance. Reduced square window openings to small marks and omitted roof baseline for clearance.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide house: peaked outline, attached entrance; source paired upper windows retained as marks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9fe195a-8b21-4c7d-a6aa-a442af174996'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/town_a9fe195a-8b21-4c7d-a6aa-a442af174996.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-arched-door-reference-a9fe195a'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('house', 'with', 'arched', 'door', 'reference', 'a9fe195a')

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

        path('house',(6,22),[(24,6),(42,22),(42,42),(6,42),(6,22)],True)
        for j,x in enumerate((16,32)):self.add_dot(f'window-{j}',(x,24))
        path('door',(20,42),[(20,35),((28,35),4,4,True),(28,42)]);self.relate('connect','door','house')
