'Coach Blowing Whistle.\nPlan and review: Retained cap, circular face, whistle and left shoulder. Omitted sound rays and shoulder hidden by whistle. Face center (24,16), radius10; jaw bottom26 and shoulder top30 give zero ink gap. A right-facing whistle keeps the source asymmetry.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: human_ref/user.svg: circular jaw and curved shoulders; source right-facing whistle.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '50a65ab3-8633-47fc-af3f-c1fe04ea5d23'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__coach-blowing-whistle/20260927T160834Z-thuan-mac-1/reference/workflow coaching user whistle_50a65ab3-8633-47fc-af3f-c1fe04ea5d23.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'coach-blowing-whistle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('coach', 'blowing', 'whistle')

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
        path('cap',(14,16),[((34,16),10,10,True),(42,16)])
        self.add_arc('jaw',(14,16),(34,16),radius_x=10,sweep=False);self.relate('connect','cap','jaw')
        self.add_line('whistle-neck',(32,24),(39,27))
        self.add_bezier('whistle-round',(39,27),((42,29),(42,35),(40,38)))
        self.add_bezier('whistle-bottom',(40,38),((37,41),(34,39),(33,35)))
        self.add_line('whistle-return',(33,35),(32,24))
        self.add_contour('whistle','whistle-neck','whistle-round','whistle-bottom','whistle-return',closed=True)
        self.relate('connect','jaw','whistle')
        self.add_bezier('body-left',(6,42),((6,34),(16,34),(24,34)))
        self.add_contour('body','body-left')
        self.relate('connect','jaw','body')
