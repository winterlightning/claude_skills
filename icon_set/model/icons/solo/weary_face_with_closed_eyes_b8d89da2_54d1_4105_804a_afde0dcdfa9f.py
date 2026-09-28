'Sad Weary Expression Emoji.\nPlan and review: Retained raised inner brows, closed-eye strokes and frown. Reduced brow spans for face-rim clearance.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8d89da2-54d1-4105-804a-afde0dcdfa9f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face weary_b8d89da2-54d1-4105-804a-afde0dcdfa9f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'weary-face-with-closed-eyes'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('weary', 'face', 'with', 'closed', 'eyes')

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

        circle('head',24,24,20)
        self.add_line('brow-left',(17,15),(20,14));self.add_line('brow-right',(28,14),(31,15))
        self.add_line('eye-left',(16,24),(19,24));self.add_line('eye-right',(29,24),(32,24))
        self.add_arc('frown',(20,34),(28,34),radius_x=4,radius_y=2,sweep=True)
