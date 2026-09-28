'Simple Standing Bird.\nPlan and review: Retained right-facing bird with down-left tail, curved wing, small beak and two legs on a shared baseline. Enlarged body around the wing and used shared tail/wing attachment to preserve wing identity with clear spacing.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide bird: continuous head/breast, pointed tail and one wing seam; intentional right-facing asymmetry.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f48d893-aef4-45f9-a4df-91680e23b5f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fowl_9f48d893-aef4-45f9-a4df-91680e23b5f9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-bird-facing-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('standing', 'bird', 'facing', 'right')

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

        curve('upper',(6,36),((8,32),(12,27),(14,24)),((18,21),(20,20),(20,18)),((20,8),(24,6),(30,6)),((38,6),(38,8),(38,10)))
        path('beak',(38,10),[(42,14),(38,18)]);self.relate('connect','upper','beak')
        curve('lower',(38,18),((40,28),(34,33),(26,33)),((18,30),(14,36),(6,36)))
        self.relate('connect','lower','upper');self.relate('connect','lower','beak')
        curve('wing',(14,24),((24,24),(30,22),(28,16)));self.relate('connect','wing','upper')
        for j,x in enumerate((22,32)):
         self.add_line(f'leg-{j}',(x,33),(x+2,42));self.relate('connect',f'leg-{j}','lower')
        self.add_line('ground',(20,42),(38,42))
        for j in range(2):self.relate('connect',f'leg-{j}','ground')
