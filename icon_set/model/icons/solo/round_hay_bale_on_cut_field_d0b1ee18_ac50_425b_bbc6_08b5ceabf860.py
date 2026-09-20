'Rolled Hay Bale in Field.\nPlan and review: Retained cylindrical hay bale with distinct circular front and three cut stalks. Omitted the second roll seam; simplified the core to a dot. Angled side connections preserve the cylinder while clearing the front rim.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0b1ee18-ac50-425b-bbc6-08b5ceabf860'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/farming hay_d0b1ee18-ac50-425b-bbc6-08b5ceabf860.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-hay-bale-on-cut-field'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('round', 'hay', 'bale', 'on', 'cut', 'field')

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

        path('roll',(14,8),[((20,10),10,10,True),((24,18),10,10,True),((20,26),10,10,True),((14,28),10,10,True),((4,18),10,10,True),((14,8),10,10,True)],True)
        self.add_dot('core',(14,18))
        path('bale',(20,10),[(34,8),((44,18),10,10,True),((34,28),10,10,True),(20,26)]);self.relate('connect','bale','roll')
        for j,x in enumerate((8,24,40)):path(f'stalk-{j}',(x-3,37),[(x,40),(x+3,37)])
