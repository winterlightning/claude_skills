"""diagonal-broom-with-curving-bristles.
Plan: Diagonal broom handle attached to a smooth fanning head; three spaced curved/straight bristle strokes follow a shared diagonal direction.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide brush-cleaning: common brush silhouette and sparse bristle marks.
Omissions: Two fine bristle strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '63b13e7a-cfd8-40db-80b6-da30f17f8995'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleaning broom_63b13e7a-cfd8-40db-80b6-da30f17f8995.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'diagonal-broom-with-curving-bristles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('cleaning', 'broom')

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

        self.add_line('handle',(6,6),(22,22))
        curve('outer',(26,42),((17,34),(15,28),(22,22)),((28,16),(33,23),(42,32)))
        self.relate('connect','handle','outer')
        self.add_line('bristle',(28,30),(38,40))
