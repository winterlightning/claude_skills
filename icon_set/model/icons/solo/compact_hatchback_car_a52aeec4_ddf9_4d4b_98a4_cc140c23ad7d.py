'Compact Hatchback Car.\nPlan and review: Retained hatchback silhouette and two wheels. Omitted window divisions; wheels join the body at exact side endpoints.\nKeyshape: HRECT_M, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide car: one body silhouette and two outlined wheels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a52aeec4-ddf9-4d4b-98a4-cc140c23ad7d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hatchback_a52aeec4-ddf9-4d4b-98a4-cc140c23ad7d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'compact-hatchback-car'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('compact', 'hatchback', 'car')

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

        curve('rear',(8,34),((4,34),(4,30),(4,26)))
        path('body',(4,26),[(4,24),((10,10),6,14,True),(24,10),(34,22),(40,22),((44,26),4,4,True)])
        curve('front',(44,26),((44,30),(44,34),(40,34)))
        self.add_contour('shell','rear','body-0','body-1','body-2','body-3','body-4','body-5','front')
        self.contours=[c for c in self.contours if c.contour_id!='body']
        self.add_line('sill',(16,34),(32,34))
        circle('rear-wheel',12,34,4);circle('front-wheel',36,34,4)
        for wheel in ('rear-wheel','front-wheel'):
         self.relate('connect','shell',wheel);self.relate('connect','sill',wheel)
