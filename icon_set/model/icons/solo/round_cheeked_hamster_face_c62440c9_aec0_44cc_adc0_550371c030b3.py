'Simple Hamster Face Icon.\nPlan and review: Retained rounded ears and cheeks, small paired eyes and nose/mouth. Simplified triangular nose to a dot joined to short mouth strokes.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c62440c9-aec0-44cc-adc0-550371c030b3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hamster_c62440c9-aec0-44cc-adc0-550371c030b3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-cheeked-hamster-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('round', 'cheeked', 'hamster', 'face')

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

        curve('outline',(16,12),((14,4),(6,4),(6,12)),((6,16),(8,18),(10,18)),((6,26),(6,30),(6,32)),((6,40),(16,42),(24,42)),((32,42),(42,40),(42,32)),((42,30),(42,26),(38,18)),((40,18),(42,16),(42,12)),((42,4),(34,4),(32,12)),((28,10),(20,10),(16,12)))
        self.add_dot('eye-left',(17,23));self.add_dot('eye-right',(31,23))
        self.add_dot('nose',(24,31))
        path('mouth',(21,33),[(24,31),(27,33)]);self.relate('connect','mouth','nose')
