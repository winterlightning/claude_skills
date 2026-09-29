"""Restored a raised left arm, torso, lowered right arm and clearly handled briefcase on the right.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: human_ref/full_body_ref.png: head radius 4 and continuous limbs; head (25,8) and torso start (25,20) have exactly 4px ink gap. Lucide id-card rounded rectangle construction informs the briefcase.
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

        circle('head',25,8,4)
        self.add_line('torso',(25,20),(25,44))
        self.add_polyline('wave',(25,20),(18,20),(10,9))
        self.add_polyline('carrying-arm',(25,20),(33,20),(36,24),(36,29))
        self.relate('connect','torso','wave');self.relate('connect','torso','carrying-arm')
        path('handle',(31,33),[('L',(31,31)),('A',(33,29),2,True),('L',(37,29)),('A',(39,31),2,True),('L',(39,33))])
        box('case',28,33,42,44,2)
        self.relate('connect','handle','case');self.relate('connect','carrying-arm','handle')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 