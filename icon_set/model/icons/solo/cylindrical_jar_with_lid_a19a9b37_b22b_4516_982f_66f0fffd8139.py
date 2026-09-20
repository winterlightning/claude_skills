'Cylindrical Jar with Lid.\nPlan and review: Retained elliptical lid, broad lid band and cylindrical body.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cylinder: elliptical ends and straight cylindrical walls.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a19a9b37-b22b-4516-982f-66f0fffd8139'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lacquerware_a19a9b37-b22b-4516-982f-66f0fffd8139.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cylindrical-jar-with-lid'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cylindrical', 'jar', 'with', 'lid')

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

        path('top',(8,12),[((40,12),16,8,True),((8,12),16,8,True)],True)
        path('body',(8,12),[(8,36),((40,36),16,8,False),(40,12)])
        self.relate('connect','top','body')
        self.add_arc('lid-band',(8,24),(40,24),radius_x=16,radius_y=4,sweep=False);self.relate('connect','lid-band','body')
