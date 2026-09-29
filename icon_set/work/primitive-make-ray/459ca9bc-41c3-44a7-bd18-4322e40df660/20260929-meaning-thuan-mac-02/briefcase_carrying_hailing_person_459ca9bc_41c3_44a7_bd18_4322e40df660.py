"""Restored a raised left arm, torso, lowered right arm and clearly handled briefcase on the right.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: human_ref/full_body_ref.png: head radius4 centered(23,8), torso starts(23,20), exactly4px detached ink gap. Rounded case and open handle preserve the source silhouette.
Keyshape: VRECT_L; bounds checked and any deliberate optical deviation recorded.
Reduction: Cropped torso retained as in the reference; no unrelated legs added."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '459ca9bc-41c3-44a7-bd18-4322e40df660'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__briefcase-carrying-hailing-person/20260929T025914Z-thuan-mac/reference/taxi wave businessman_459ca9bc-41c3-44a7-bd18-4322e40df660.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'briefcase-carrying-hailing-person'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('briefcase', 'carrying', 'hailing', 'person')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Preserve the right-hand open briefcase handle and the left raised hand. The natural asymmetric figure extends beyond the nominal vertical keyshape, with approximately 3px clearance at the case handle and torso. Actual head-to-torso gap is exactly 4px. The case is separated from the torso and its handle opening is visible. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6b9811670f311e7859f524c941ae9a4a4330b8ab4740d659dfcba10cd08f0ac8'}

    def build(self):

        def curve(name,start,c1,c2,end): self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start;ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L':self.add_line(part,point,end)
                elif kind=='C':curve(part,point,args[0],args[1],end)
                elif kind=='A':self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                ids.append(part);point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,True)],True)

        circle('head',23,8,4)
        self.add_line('torso',(23,20),(23,44))
        self.add_polyline('wave',(23,20),(17,20),(9,9))
        self.add_polyline('carrying-arm',(23,20),(31,20),(36,24),(36,27))
        self.relate('connect','torso','wave');self.relate('connect','torso','carrying-arm')
        path('handle',(33,34),[('L',(33,29)),('A',(35,27),2,True),('L',(39,27)),('A',(41,29),2,True),('L',(41,34))])
        box('case',30,34,44,44,2)
        self.relate('connect','handle','case');self.relate('connect','carrying-arm','handle')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
