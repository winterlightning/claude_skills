'Elderly Man with Glasses and Mustache.\nPlan and review: UNRESOLVED: enlarged circular head and wider spectacles still fail head/glasses, jaw/frown and glasses/frown MIC; curved shoulder/jaw spacing also requires review. Preserved the observed downturned arc as a frown rather than inventing a mustache. Two layouts were attempted. This draft is not approved.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: human_ref/user.svg: circular head, curved touching shoulders.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e10b85b-424e-4558-b38e-c8c3b76d9e52'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grandpa_2e10b85b-424e-4558-b38e-c8c3b76d9e52.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bespectacled-bust-with-downturned-facial-arc'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bespectacled', 'bust', 'with', 'downturned', 'facial', 'arc')

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

        path('head',(8,20),[((40,20),16,16,True)])
        self.add_arc('jaw',(8,20),(40,20),radius_x=16,sweep=False);self.relate('connect','head','jaw')
        box('glasses-left',10,12,20,20,3);box('glasses-right',28,12,38,20,3)
        self.add_line('bridge',(20,16),(28,16))
        for s in ('left','right'):self.relate('connect','bridge','glasses-'+s)
        curve('frown',(20,28),((20,24),(28,24),(28,28)))
        self.add_arc('body-left',(8,44),(20,40),radius_x=12,radius_y=4,sweep=True)
        self.add_line('body-top',(20,40),(28,40))
        self.add_arc('body-right',(28,40),(40,44),radius_x=12,radius_y=4,sweep=True)
        self.add_contour('body','body-left','body-top','body-right');self.relate('connect','jaw','body')
