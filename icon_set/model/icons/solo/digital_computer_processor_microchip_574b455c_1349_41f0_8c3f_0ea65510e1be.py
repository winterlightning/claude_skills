'Digital Computer Processor Microchip.\nPlan and review: Retained blank rounded processor package and all twelve pins, with shared 8-unit repeat spacing.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cpu: rounded package with regularly spaced attached pins, omit internal chip.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '574b455c-1349-41f0-8c3f-0ea65510e1be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/microchip_574b455c-1349-41f0-8c3f-0ea65510e1be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'digital-computer-processor-microchip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('digital', 'computer', 'processor', 'microchip')

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

        path('chip',(16,12),[(24,12),(32,12),((36,16),4,4,True),(36,24),(36,32),((32,36),4,4,True),(24,36),(16,36),((12,32),4,4,True),(12,24),(12,16),((16,12),4,4,True)],True)
        for j,q in enumerate((16,24,32)):
         for side,a,b in [('top',(q,6),(q,12)),('bottom',(q,36),(q,42)),('left',(6,q),(12,q)),('right',(36,q),(42,q))]:
          name=f'{side}-{j}';self.add_line(name,a,b);self.relate('connect',name,'chip')
