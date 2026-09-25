'Decorative Lace Fabric.\nPlan and review: Retained fabric panel, top band and scalloped hem. Reduced four scallops to three; replaced three decorative curls with two circular eyelet marks.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8172d24e-cc5a-4f01-8fdb-f4872e411dc9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lace_8172d24e-cc5a-4f01-8fdb-f4872e411dc9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'decorative-lace-fabric'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('decorative', 'lace', 'fabric')

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

        path('fabric',(6,34),[(6,6),(42,6),(42,34),((30,34),6,8,True),((18,34),6,8,True),((6,34),6,8,True)],True)
        self.add_line('band',(6,14),(42,14));self.relate('connect','band','fabric')
        for j,x in enumerate((17,31)):circle(f'eyelet-{j}',x,24,2)
