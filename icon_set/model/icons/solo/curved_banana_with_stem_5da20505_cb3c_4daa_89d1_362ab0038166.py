'Single Banana Fruit.\nPlan and review: Retained crescent banana and curved upper-right stem. Omitted inner seam because it crowded the narrow fruit body.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide banana: long crescent and seam; source unpeeled upright stem orientation retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5da20505-cb3c-4daa-89d1-362ab0038166'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fruit bhudda hand finger citron 2_5da20505-cb3c-4daa-89d1-362ab0038166.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-banana-with-stem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('curved', 'banana', 'with', 'stem')

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

        curve('banana',(6,34),((24,32),(30,26),(34,16)),((36,8),(42,16),(42,24)),((42,34),(30,42),(20,42)),((12,42),(6,38),(6,34)))
        
        curve('stem',(36,14),((36,10),(36,6),(32,6)));self.relate('connect','stem','banana')
