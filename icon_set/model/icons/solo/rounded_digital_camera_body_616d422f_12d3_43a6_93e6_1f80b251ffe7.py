'A front-facing camera has a rounded body, raised top housing and circular lens. HRECT_L preserves its wide silhouette. The shell mirrors about x24 and owns a centred lens; radius and lens height distinguish this source. Source supplies its plain body and lens; Lucide camera supplies continuous shoulder transitions and one unadorned lens. No additional buttons introduced.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '616d422f-12d3-43a6-93e6-1f80b251ffe7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/camera settings focus_616d422f-12d3-43a6-93e6-1f80b251ffe7.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'rounded-digital-camera-body'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Digital Photography Camera',)
    keywords = ('digital', 'photography', 'camera')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        path('shell',(8,16),[(13,16),(18,8),(30,8),(35,16),(40,16),((44,20),4,4,True),(44,36),((40,40),4,4,True),(8,40),((4,36),4,4,True),(4,20),((8,16),4,4,True)],True)
        circle('lens',24,25,6)
