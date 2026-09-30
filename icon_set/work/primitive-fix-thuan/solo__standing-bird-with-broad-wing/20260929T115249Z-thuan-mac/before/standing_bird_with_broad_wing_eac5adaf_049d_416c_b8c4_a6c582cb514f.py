'Simple Standing Bird.\nPlan and review: Retained right-facing bird with broad left-pointed wing, beak and two legs sharing a baseline. Integrated outer wing into the body silhouette and kept its inner curved seam.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide bird: curved head/body and broad inner wing; source horizontal wing retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eac5adaf-049d-416c-b8c4-a6c582cb514f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gamebird_eac5adaf-049d-416c-b8c4-a6c582cb514f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-bird-with-broad-wing'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('standing', 'bird', 'with', 'broad', 'wing')

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

        curve('upper',(6,24),((12,16),(20,10),(26,12)),((26,8),(28,6),(32,6)),((36,6),(38,8),(38,10)))
        path('beak',(38,10),[(42,14),(38,18)]);self.relate('connect','beak','upper')
        curve('lower',(38,18),((40,26),(34,33),(26,33)),((18,33),(12,30),(6,24)))
        self.relate('connect','lower','upper');self.relate('connect','lower','beak')
        curve('wing',(26,12),((34,22),(24,26),(6,24)));self.relate('connect','wing','upper');self.relate('connect','wing','lower')
        for j,x in enumerate((22,32)):
         self.add_line(f'leg-{j}',(x,33),(x,42));self.relate('connect',f'leg-{j}','lower')
        self.add_line('ground',(20,42),(38,42))
        for j in range(2):self.relate('connect',f'leg-{j}','ground')
