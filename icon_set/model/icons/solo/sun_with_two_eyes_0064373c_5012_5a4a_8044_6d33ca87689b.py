'Smiling Sun Face. Plan and review: Eight cardinal/diagonal rays and two eye dots retained. Rays touch the rim; short source eye lines become dots. Keyshape SQUARE centerline envelope (6,6)-(42,42). Chosen to fit the complete subject silhouette. Reference: Lucide sun original and atomic-debug: round center and radial rays.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0064373c-5012-5a4a-8044-6d33ca87689b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/mario shine sprite_0064373c-5012-5a4a-8044-6d33ca87689b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-with-two-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('sun', 'with', 'two', 'eyes')

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

        path('sun',(24,11),[((37,24),13,13,True),((24,37),13,13,True),((11,24),13,13,True),((24,11),13,13,True)],True)
        for name,a,b in [('n',(24,11),(24,6)),('s',(24,37),(24,42)),('w',(11,24),(6,24)),('e',(37,24),(42,24)),('nw',(15,15),(10,10)),('ne',(33,15),(38,10)),('sw',(15,33),(10,38)),('se',(33,33),(38,38))]:
         self.add_line(name,a,b);self.relate('connect','sun',name)
        self.add_dot('eye-l',(20,24));self.add_dot('eye-r',(28,24))
