'Seedling with Three Leaves.\nPlan and review: Retained all three leaves and left-above-right arrangement. Shortened top leaf and moved side leaves down for clearance.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide sprout: coherent pointed leaves and attached stem; source three-leaf ordering retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c60a0bd7-7e91-458f-b755-644d0944bed8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stalk_c60a0bd7-7e91-458f-b755-644d0944bed8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-leaf-stalk'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('three', 'leaf', 'stalk')

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

        self.add_polyline('stem',(24,12),(24,32),(24,42),(24,44))
        curve('leaf-top',(28,4),((18,4),(18,10),(24,12)),((30,10),(32,8),(28,4)))
        curve('leaf-left',(8,22),((18,22),(22,26),(24,32)),((14,32),(8,28),(8,22)))
        curve('leaf-right',(40,32),((30,32),(26,36),(24,42)),((34,42),(40,38),(40,32)))
        for s in ('leaf-top','leaf-left','leaf-right'):self.relate('connect','stem',s)
