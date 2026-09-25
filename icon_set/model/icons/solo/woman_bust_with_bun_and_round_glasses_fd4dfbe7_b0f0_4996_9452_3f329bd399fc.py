'Elderly Woman with Bun and Glasses.\nPlan and review: Retained top bun, round linked spectacles, circular jaw and curved shoulders. Omitted ears, hair-part seam and neckline. Spectacles meet the face at their outer extrema. Jaw center(24,22), radius12, bottom34; shoulder top38 gives zero ink gap.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: human_ref/user.svg: circular jaw and touching curved shoulders.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd4dfbe7-b0f0-4996-9452-3f329bd399fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grandma_fd4dfbe7-b0f0-4996-9452-3f329bd399fc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-bust-with-bun-and-round-glasses'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('woman', 'bust', 'with', 'bun', 'and', 'round', 'glasses')

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

        path('hair',(12,22),[((18,12),6,10,True),((30,12),6,8,True),((36,22),6,10,True)])
        self.add_arc('jaw',(12,22),(36,22),radius_x=12,sweep=False);self.relate('connect','hair','jaw')
        circle('glass-left',16,22,4);circle('glass-right',32,22,4)
        self.add_line('bridge',(20,22),(28,22))
        for s in ('left','right'):
         self.relate('connect','bridge','glass-'+s);self.relate('connect','jaw','glass-'+s);self.relate('connect','hair','glass-'+s)
        self.add_arc('body-left',(8,44),(16,38),radius_x=8,radius_y=6,sweep=True)
        self.add_line('body-top',(16,38),(32,38))
        self.add_arc('body-right',(32,38),(40,44),radius_x=8,radius_y=6,sweep=True)
        self.add_contour('body','body-left','body-top','body-right');self.relate('connect','jaw','body')
