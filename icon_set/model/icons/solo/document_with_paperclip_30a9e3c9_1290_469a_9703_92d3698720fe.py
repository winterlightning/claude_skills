'Document with Paperclip.\nPlan and review: Retained blank rounded sheet and paperclip hooked over upper left, with open inner end.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide paperclip: open nested loop; document remains blank.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30a9e3c9-1290-469a-9703-92d3698720fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/attached file_30a9e3c9-1290-469a-9703-92d3698720fe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'document-with-paperclip'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('document', 'with', 'paperclip')

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

        path('sheet',(24,12),[(36,12),((40,16),4,4,True),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,12)])
        path('clip',(8,12),[((24,12),8,8,True),(24,24),((16,24),4,4,True),(16,14)])
        self.relate('connect','sheet','clip')
