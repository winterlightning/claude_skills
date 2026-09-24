'Closed Hardcover Book.\nPlan and review: Retained rounded spine, blank cover and bottom page band; omitted secondary spine seam.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide book: rounded spine and single bottom page rule.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50c84aaa-af44-4a3d-9303-9dbfdf04c956'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hardcover_50c84aaa-af44-4a3d-9303-9dbfdf04c956.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-hardcover-book-source-50c84aaa'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('closed', 'hardcover', 'book', 'source', '50c84aaa')

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

        path('cover',(40,36),[(40,4),(16,4),((8,12),8,8,False),(8,40),((12,44),4,4,False),(40,44)])
        self.add_line('pages',(8,36),(40,36));self.relate('connect','cover','pages')
