"""Restored two distinct people: a reclining base supports a folded inverted flyer, with two circular heads and an explicit support contact.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: human_ref/full_body_ref.png: circular heads and coherent limb strokes. No useful exact Lucide acro-yoga reference. Base head (10,38), r4, torso starts (22,38); flyer head (36,23), r3, torso starts (36,12): both head-to-torso ink gaps exactly 4.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Outlined filled-body source reduced to two coherent figures; folded pose, both heads and support contact retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '672c58c9-cf49-5d74-ba11-e6398667c047'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-folded-balance/20260929T025914Z-thuan-mac/reference/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'acro-yoga-folded-balance'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('acro', 'yoga', 'folded', 'balance')

    exception = {'reason': 'User explicitly delegated visual-exception decisions to gpt-6, conditional on UI/UX quality. Keep the folded flyer and reclining base as two recognizable figures. The real supporting arm/leg contact and nearby flyer head require local sub-4px clearance. Both heads retain exactly 4px ink clearance to their own torso junctions. Two heads and the supporting pose are legible at 48px. Reviewed at native 48px and enlarged in light and dark; uniform 4px strokes retained. Automatic findings are preserved.', 'approved_by': 'user: delegated decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ab137c5146dfaf4bc579ac1005b2b078e8c6a3c0fef23a3009d48a390fa8b8a1'}

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

        circle('base-head',10,38,4)
        self.add_line('base-torso',(22,38),(35,38))
        self.add_polyline('base-legs',(35,38),(42,38),(42,30))
        self.add_line('support-arm',(25,38),(25,25))
        self.relate('connect','base-torso','base-legs')
        self.relate('connect','base-torso','support-arm')
        circle('flyer-head',36,23,3)
        curve('flyer-torso',(36,12),(36,6),(33,6),(28,6))
        self.add_polyline('folded-legs',(28,6),(10,18),(25,18),(25,25))
        self.relate('connect','flyer-torso','folded-legs')
        self.relate('connect','folded-legs','support-arm')
        self.mark_human_figure('base',head='base-head',torso='base-torso',torso_junction='start')
        self.mark_human_figure('flyer',head='flyer-head',torso='flyer-torso',torso_junction='start')
 