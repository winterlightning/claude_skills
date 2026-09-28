'Round Portable Lantern.\nPlan and review: Retained rounded lantern globe, crossbars, upper loop handle and integrated pedestal. Rebuilt the initial globe-on-stand draft to restore portable-lantern identity.\nKeyshape: VRECT_M, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf8dff34-f22d-4976-9ab6-677659af27b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lamp 1_bf8dff34-f22d-4976-9ab6-677659af27b1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-lantern'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('round', 'lantern')

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

        path('globe',(24,15),[((38,29),14,14,True),((32,40),14,14,True),(32,44),(16,44),(16,40),((10,29),14,14,True),((24,15),14,14,True)],True)
        self.add_polyline('vertical',(24,15),(24,29),(24,44));self.add_polyline('horizontal',(10,29),(24,29),(38,29))
        for s in ('vertical','horizontal'):self.relate('connect','globe',s)
        self.relate('connect','vertical','horizontal')
        path('handle',(18,14),[(18,10),((30,10),6,6,True),(30,14)]);self.relate('connect','handle','globe')
