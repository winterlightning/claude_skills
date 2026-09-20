'Simple Steamboat with Smoke.\nPlan and review: Retained rounded hull, rectangular cabin, chimney and separate smoke wisp. Omitted small cabin arch and repositioned smoke to upper left for clearance.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide ship: tiered deckhouse; source chimney and smoke distinguish steam vessel.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70696fb3-4a4b-4859-a923-a7b2f6c17379'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steamboat_70696fb3-4a4b-4859-a923-a7b2f6c17379.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steamboat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('steamboat',)

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

        path('hull',(6,32),[(42,32),((32,42),10,10,True),(16,42),((6,32),10,10,True)],True)
        path('cabin',(14,32),[(14,24),(34,24),(34,32)]);self.relate('connect','cabin','hull')
        path('stack',(24,24),[(24,16),(34,16),(34,24)]);self.relate('connect','stack','cabin')
        curve('smoke',(10,12),((10,8),(16,8),(16,8)),((20,8),(20,6),(20,6)))
