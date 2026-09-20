'Diagonal Magic Wand Tool.\nPlan and review: Retained rounded diagonal wand and grip divider. Rebuilt rounded ends at exact SQUARE extrema.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide wand: rounded diagonal shaft; omit unrelated sparkles absent in original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79f706ff-d747-4b33-b66f-b569d493a1f3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/wand_79f706ff-d747-4b33-b66f-b569d493a1f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-magic-wand-tool'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'magic', 'wand', 'tool')

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

        curve('upper-cap',(30,10),((32,8),(34,6),(36,6)),((40,6),(42,8),(42,12)),((42,14),(40,16),(38,18)))
        self.add_line('right-edge',(38,18),(18,38))
        curve('lower-cap',(18,38),((16,40),(14,42),(12,42)),((8,42),(6,40),(6,36)),((6,34),(8,32),(10,30)))
        self.add_line('left-edge',(10,30),(30,10));self.add_contour('wand','upper-cap','right-edge','lower-cap','left-edge',closed=True)
        self.add_line('grip',(18,22),(26,30));self.relate('connect','grip','wand')
