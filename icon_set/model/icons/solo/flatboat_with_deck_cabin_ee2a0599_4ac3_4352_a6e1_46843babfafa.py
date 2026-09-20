'Simple Cargo Boat Vessel.\nPlan and review: Retained broad low hull and plain centered deck cabin. Shared cabin/deck anchors.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide ship: joined deckhouse and hull; source low profile retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee2a0599-4ac3-4352-a6e1-46843babfafa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flatboat_ee2a0599-4ac3-4352-a6e1-46843babfafa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flatboat-with-deck-cabin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('flatboat', 'with', 'deck', 'cabin')

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

        path('hull',(4,24),[(44,24),(40,34),((34,40),6,6,True),(14,40),((8,34),6,6,True),(4,24)],True)
        path('cabin',(16,24),[(16,8),(32,8),(32,24)]);self.relate('connect','hull','cabin')
