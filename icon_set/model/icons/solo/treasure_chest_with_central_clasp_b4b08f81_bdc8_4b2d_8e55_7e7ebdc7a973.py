'Simple Treasure Chest.\nPlan and review: Retained rounded chest, shallow lid seam and central rounded clasp. Omitted keyhole and two vertical lid bands to protect spacing.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4b08f81-bdc8-4b2d-8e55-7e7ebdc7a973'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fantasy medieval loot box treasure chest reward 3_b4b08f81-bdc8-4b2d-8e55-7e7ebdc7a973.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'treasure-chest-with-central-clasp'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('treasure', 'chest', 'with', 'central', 'clasp')

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

        box('chest',4,8,44,40,5)
        path('seam',(4,21),[(18,21),(18,25),((30,25),6,6,False),(30,21),(44,21)]);self.relate('connect','seam','chest')
