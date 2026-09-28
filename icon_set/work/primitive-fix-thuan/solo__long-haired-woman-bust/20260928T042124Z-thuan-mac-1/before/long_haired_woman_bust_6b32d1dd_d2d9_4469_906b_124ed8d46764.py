'Female User Profile.\nPlan and review: Retained long hair reaching shoulders, central fringe, blank circular face and broad curved shoulders. Omitted neckline. Jaw center(24,20), radius8, bottom28; shoulder top32 gives zero ink gap.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: human_ref/user.svg: circular jaw, rounded touching shoulders; source hair.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b32d1dd-d2d9-4469-906b-124ed8d46764'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/girlfriend_6b32d1dd-d2d9-4469-906b-124ed8d46764.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-haired-woman-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('long', 'haired', 'woman', 'bust')

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

        path('hair',(8,40),[(8,20),((40,20),16,16,True),(40,40)])
        self.add_arc('jaw',(16,20),(32,20),radius_x=8,sweep=False)
        curve('fringe',(16,20),((20,20),(22,17),(24,14)),((26,17),(28,20),(32,20)))
        self.relate('connect','jaw','fringe')

        self.add_line('body-left',(8,44),(8,40))
        self.add_arc('body-shoulder-left',(8,40),(20,32),radius_x=12,radius_y=8,sweep=True)
        self.add_line('body-top',(20,32),(28,32))
        self.add_arc('body-shoulder-right',(28,32),(40,40),radius_x=12,radius_y=8,sweep=True)
        self.add_line('body-right',(40,40),(40,44))
        self.add_contour('body','body-left','body-shoulder-left','body-top','body-shoulder-right','body-right')
        self.relate('connect','jaw','body')


        self.add_line('temple-left',(8,20),(16,20));self.add_line('temple-right',(32,20),(40,20))
        for t in ('temple-left','temple-right'):
            for p in ('hair','jaw','fringe'):self.relate('connect',t,p)

        self.relate('connect','hair','body')

SOURCE_REFERENCES = [('537c9790-95ad-4207-bed6-e5d11691c98f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/artist_537c9790-95ad-4207-bed6-e5d11691c98f.svg')]
