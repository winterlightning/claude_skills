'Detective in Fedora and Trench Coat.\nPlan and review: Retained notched fedora, broad brim, circular jaw, curved shoulders and V-shaped coat lapels. Omitted extra collar folds. Jaw center(24,14), radius10, bottom24; shoulder top28: zero ink gap.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: human_ref/user.svg: circular jaw and smooth curved shoulders; source fedora and lapels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6aad8940-cfb6-4571-a35f-bfd82d1157b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gumshoe_6aad8940-cfb6-4571-a35f-bfd82d1157b2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'detective-in-fedora-and-trench-coat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('detective', 'in', 'fedora', 'and', 'trench', 'coat')

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

        path('crown',(14,14),[(14,4),(24,6),(34,4),(34,14)])
        self.add_line('brim',(8,14),(40,14));self.relate('connect','crown','brim')
        self.add_arc('jaw',(14,14),(34,14),radius_x=10,sweep=False);self.relate('connect','jaw','brim')
        self.add_line('body-left',(8,44),(8,38));self.add_arc('body-left-shoulder',(8,38),(20,28),radius_x=12,radius_y=10,sweep=True)
        self.add_line('body-top',(20,28),(28,28));self.add_arc('body-right-shoulder',(28,28),(40,38),radius_x=12,radius_y=10,sweep=True);self.add_line('body-right',(40,38),(40,44))
        self.add_contour('body','body-left','body-left-shoulder','body-top','body-right-shoulder','body-right');self.relate('connect','jaw','body')
        path('lapel',(12,32),[(24,44),(36,32)]);self.relate('connect','lapel','body')
