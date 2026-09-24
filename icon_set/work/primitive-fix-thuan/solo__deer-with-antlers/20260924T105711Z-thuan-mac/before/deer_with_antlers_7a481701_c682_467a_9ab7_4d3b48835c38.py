'Deer with Antlers.\nPlan and review: Retained right-facing deer, long neck, muzzle, antlers and leg cues. Simplified branching antlers and omitted small ear/hidden leg details.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a481701-c682-467a-9ab7-4d3b48835c38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fawn_7a481701-c682-467a-9ab7-4d3b48835c38.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'deer-with-antlers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('deer', 'with', 'antlers')

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

        path('back',(6,42),[(6,28),((14,22),8,6,True),(24,22),(28,14),(34,14),(42,18),(42,26),(34,26),(32,42)])
        path('belly',(6,32),[(16,32),(26,32),(32,42)]);self.relate('connect','back','belly')
        self.add_line('rear-leg',(16,32),(16,42));self.relate('connect','belly','rear-leg')
        path('antler-left',(28,14),[(24,10),(20,6)]);self.relate('connect','back','antler-left')
        path('antler-right',(34,14),[(34,6),(40,6)]);self.relate('connect','back','antler-right')
