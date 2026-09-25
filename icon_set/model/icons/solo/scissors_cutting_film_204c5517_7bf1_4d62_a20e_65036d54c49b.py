'Scissors Cutting Film Strip.\nPlan and review: Retained two scissor loops, crossing blades and cut film-strip sections. Reduced fine film perforations to two large frames and made upper/lower film extents symmetric.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide scissors: two round finger loops and crossing blades; source cutting interaction retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '204c5517-7bf1-4d62-a20e-65036d54c49b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/video edit cut_204c5517-7bf1-4d62-a20e-65036d54c49b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scissors-cutting-film'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('scissors', 'cutting', 'film')

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

        circle('loop-top',10,15,4);circle('loop-bottom',10,33,4)
        self.add_line('blade-down',(13,18),(28,33));self.add_line('blade-up',(13,30),(28,15))
        self.relate('connect','loop-top','blade-down');self.relate('connect','loop-bottom','blade-up');self.relate('connect','blade-up','blade-down')
        path('film-top',(28,16),[(28,6),(42,6),(42,20)])
        path('film-bottom',(28,32),[(28,42),(42,42),(42,28)])
        self.add_line('frame-top',(28,14),(42,14));self.relate('connect','frame-top','film-top')
        self.add_line('frame-bottom',(28,34),(42,34));self.relate('connect','frame-bottom','film-bottom')
        self.relate('connect','blade-up','film-top');self.relate('connect','blade-down','film-bottom')
