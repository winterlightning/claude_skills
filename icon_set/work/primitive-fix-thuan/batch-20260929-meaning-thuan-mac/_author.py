"""Fresh primitive-make-ray meaning repairs; input identity stored per specification."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
AUTHOR='gpt-6'
SOURCE_ICON_ID = {'acro-yoga-folded-balance': '672c58c9-cf49-5d74-ba11-e6398667c047', 'adult-child-high-five-hands': 'b88757c2-b1ab-49df-9283-b755a2874066', 'airplane-rising-above-ground-line': '28bc625b-2596-540d-91c3-fb5e36336a56', 'baby-bottle-with-handles': '46fff59c-84bf-4526-bd9b-33201133c81c', 'box-delivery-truck': '0070eae2-79f7-4131-b3be-164ea822745d', 'briefcase-carrying-hailing-person': '459ca9bc-41c3-44a7-bd18-4322e40df660', 'broccoli-and-carrot': '1833535f-220e-490a-9e51-7058a14ac9db', 'browser-user-profile': '3a3e4d85-115c-4ccb-82d1-46fd45222b3a', 'canoe': '2f08daf6-071b-5ac7-9717-2239ffbb2925', 'hand-holding-wrench': '80b7765d-72c2-4b01-b0bf-6a084aa9bc97', 'hand-massaging-foot-8ab52d55': '8ab52d55-ae52-4c12-82e0-c8e7e2dc8409', 'hand-massaging-scalp-17e8bc26': '17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec', 'hand-over-heat': 'e2391138-4aaf-4587-83d5-f636e7ba5379', 'hand-playing-pad-controller': '2e9ddede-2e59-4491-8fa8-b1f79514c010', 'hand-playing-yoyo': '28a605e6-a545-47ed-ae21-f45557bb8374', 'hand-pointing-down-batch-024-04': '5a80cb54-e04f-5e41-ba53-6892a6852f05', 'hand-stealing-identity-card-solo-b005-06': '3ba267b5-9ca9-4999-a24d-b73d45e0c937', 'handcuffs-with-arched-connector': '404190ff-389e-4a15-a7fe-4b448b432ffd', 'handcuffs-with-curved-link': 'ad5f17ec-d6f2-402a-8907-dbd8532598e6', 'handled-comb-on-diagonal': 'dafdca17-4d27-4cd9-935d-01a08f4e53e2'}
SOURCE_PATH = {'acro-yoga-folded-balance': 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-folded-balance/20260929T025914Z-thuan-mac/reference/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg', 'adult-child-high-five-hands': 'icon_set/work/primitive-fix-thuan/solo__adult-child-high-five-hands/20260929T025914Z-thuan-mac/reference/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg', 'airplane-rising-above-ground-line': 'icon_set/work/primitive-fix-thuan/solo__airplane-rising-above-ground-line/20260929T025914Z-thuan-mac/reference/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg', 'baby-bottle-with-handles': 'icon_set/work/primitive-fix-thuan/solo__baby-bottle-with-handles/20260929T025914Z-thuan-mac/reference/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg', 'box-delivery-truck': 'icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260929T025914Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg', 'briefcase-carrying-hailing-person': 'icon_set/work/primitive-fix-thuan/solo__briefcase-carrying-hailing-person/20260929T025914Z-thuan-mac/reference/taxi wave businessman_459ca9bc-41c3-44a7-bd18-4322e40df660.svg', 'broccoli-and-carrot': 'icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260929T025914Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg', 'browser-user-profile': 'icon_set/work/primitive-fix-thuan/solo__browser-user-profile/20260929T025914Z-thuan-mac/reference/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg', 'canoe': 'icon_set/work/primitive-fix-thuan/solo__canoe/20260929T025914Z-thuan-mac/reference/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg', 'hand-holding-wrench': 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wrench/20260929T025914Z-thuan-mac/reference/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg', 'hand-massaging-foot-8ab52d55': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-foot-8ab52d55/20260929T025914Z-thuan-mac/reference/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg', 'hand-massaging-scalp-17e8bc26': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-scalp-17e8bc26/20260929T025914Z-thuan-mac/reference/massage head_17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec.svg', 'hand-over-heat': 'icon_set/work/primitive-fix-thuan/solo__hand-over-heat/20260929T025914Z-thuan-mac/reference/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg', 'hand-playing-pad-controller': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-pad-controller/20260929T025914Z-thuan-mac/reference/modern music mix touch_2e9ddede-2e59-4491-8fa8-b1f79514c010.svg', 'hand-playing-yoyo': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-yoyo/20260929T025914Z-thuan-mac/reference/playing yoyo_28a605e6-a545-47ed-ae21-f45557bb8374.svg', 'hand-pointing-down-batch-024-04': 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-down-batch-024-04/20260929T025914Z-thuan-mac/reference/hand pointer bottom_5a80cb54-e04f-5e41-ba53-6892a6852f05.svg', 'hand-stealing-identity-card-solo-b005-06': 'icon_set/work/primitive-fix-thuan/solo__hand-stealing-identity-card-solo-b005-06/20260929T025914Z-thuan-mac/reference/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg', 'handcuffs-with-arched-connector': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-arched-connector/20260929T025914Z-thuan-mac/reference/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg', 'handcuffs-with-curved-link': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-curved-link/20260929T025914Z-thuan-mac/reference/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg', 'handled-comb-on-diagonal': 'icon_set/work/primitive-fix-thuan/solo__handled-comb-on-diagonal/20260929T025914Z-thuan-mac/reference/hair dress comb_dafdca17-4d27-4cd9-935d-01a08f4e53e2.svg'}
BATCH=Path(__file__).parent
SPECS={}
def spec(key,before,change,ref,body,shape='SQUARE',omissions='Minor source contour irregularities simplified.'):
    SPECS[key]=dict(before=before,change=change,refs=ref,body=body,keyshape=shape,omissions=omissions)

spec('acro-yoga-folded-balance',
 'The rejected drawing has only one head and a generic inverted stick shape, losing the two-person folded acro-yoga pose.',
 'Restored two distinct people: a reclining base supports a folded inverted flyer, with two circular heads and an explicit support contact.',
 'human_ref/full_body_ref.png: circular heads and coherent limb strokes. No useful exact Lucide acro-yoga reference. Base head (10,38), r4, torso starts (22,38); flyer head (36,23), r3, torso starts (36,12): both head-to-torso ink gaps exactly 4.',
 """
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
 """,omissions='Outlined filled-body source reduced to two coherent figures; folded pose, both heads and support contact retained.')

spec('adult-child-high-five-hands',
 'The rejected image substitutes two full stick people for the reference close-up of a large and small hand touching.',
 'Restored overlapping hands of different sizes, diagonal fingers, a raised rear thumb and a smaller foreground palm.',
 'Lucide hand: rounded fingers and a coherent palm outline. Original defines two overlapping hands and relative size.',
 """
        path('rear-hand',(42,40),[('L',(38,35)),('C',(38,24),(39,31),(39,28)),('L',(36,12)),('C',(30,12),(35,7),(30,7)),('L',(29,23)),('L',(15,8)),('C',(10,12),(11,3),(6,8)),('L',(19,21))])
        path('rear-fingers',(10,12),[('C',(7,18),(5,10),(3,15)),('L',(13,24))])
        path('rear-little',(7,18),[('C',(8,28),(1,18),(4,24))])
        path('small-hand',(13,42),[('C',(6,34),(8,42),(6,39)),('C',(9,27),(6,31),(7,29)),('L',(21,15)),('C',(25,19),(25,12),(28,16)),('L',(18,26)),('L',(28,18)),('C',(32,22),(32,15),(35,19)),('L',(24,30)),('L',(32,24)),('C',(36,28),(36,21),(39,25)),('L',(26,36)),('L',(29,35)),('C',(31,40),(33,33),(35,38)),('L',(21,42)),('C',(13,42),(18,44),(15,43))],True)
 """,omissions='Four-finger silhouettes reduced to three visible foreground fingers and two partial rear fingers to preserve separation.')

spec('airplane-rising-above-ground-line',
 'The rejected airplane reverses the defining wing into an upper zigzag; the reference has a long downward main wing and a shallow rising fuselage.',
 'Restored the downward swept wing, small tail fin, rounded nose and rising fuselage above a ground line.',
 'Lucide plane-takeoff: rounded fuselage and ground line; original owns the downward main wing.',
 """
        path('plane',(6,17),[('L',(11,17)),('L',(16,22)),('L',(35,14)),('C',(42,17),(39,12),(42,13)),('C',(39,21),(42,19),(41,20)),('L',(29,25)),('L',(24,35)),('L',(19,37)),('L',(21,27)),('L',(14,30)),('C',(10,28),(12,31),(11,30)),('L',(6,17))],True)
        self.add_line('ground',(6,42),(42,42))
 """,omissions='Small tail/body corner irregularities simplified; wing direction retained.')

spec('baby-bottle-with-handles',
 'The rejected upright bottle has open dangling strokes instead of the original closed side handles and loses the diagonal feeding-bottle silhouette.',
 'Restored a diagonal bottle with a rounded body, two closed loop handles, broad collar and shaped nipple.',
 'Lucide baby informs simple rounded baby-product shapes; supplied original defines nipple, collar and handles.',
 """
        path('bottle',(11,24),[('L',(25,10)),('L',(38,23)),('L',(24,37)),('C',(17,42),(21,40),(20,42)),('C',(13,40),(15,42),(14,41)),('L',(8,35)),('C',(8,28),(5,32),(6,30)),('L',(11,24))],True)
        path('collar',(25,10),[('C',(29,6),(23,7),(26,4)),('L',(42,19)),('C',(38,23),(45,22),(41,26)),('L',(25,10))],True)
        path('nipple',(29,6),[('C',(35,6),(31,7),(33,7)),('C',(42,13),(41,0),(48,7)),('C',(42,19),(42,15),(41,17))])
        path('left-handle',(11,24),[('C',(7,13),(5,24),(4,17)),('C',(17,13),(10,10),(14,10))])
        path('right-handle',(31,30),[('C',(35,40),(38,30),(39,36)),('C',(24,37),(31,43),(27,40))])
        self.relate('connect','bottle','collar')
        self.relate('connect','collar','nipple')
        self.relate('connect','bottle','left-handle')
        self.relate('connect','bottle','right-handle')
 """)

spec('box-delivery-truck',
 'The rejected truck has an undivided cab with no windshield boundary, making the delivery vehicle read as a blocky cart.',
 'Restored a separate tall cargo box, sloped cab with a windshield division, and two equal round wheels with clear hubs.',
 'Lucide truck: cargo/cab hierarchy and wheel-aligned baseline. Source defines windshield separator.',
 """
        path('cargo',(6,34),[('L',(4,34)),('L',(4,10)),('A',(6,8),2,True),('L',(26,8)),('A',(28,10),2,True),('L',(28,34)),('L',(18,34))])
        path('cab',(28,13),[('L',(35,13)),('L',(44,24)),('L',(44,34)),('L',(42,34))])
        self.add_line('windshield',(28,24),(44,24))
        self.add_line('underbody',(28,34),(30,34))
        circle('rear-wheel',12,34,6);circle('front-wheel',36,34,6)
        for a,b in [('cargo','cab'),('cab','windshield'),('cargo','windshield'),('cargo','underbody'),('underbody','front-wheel'),('cargo','rear-wheel'),('cab','front-wheel')]:self.relate('connect',a,b)
 """,shape='HRECT_L')

spec('briefcase-carrying-hailing-person',
 'The rejected stick figure raises the opposite arm and hangs a tiny detached box; the reference is a cropped businessman with a clear handled briefcase and raised left hand.',
 'Restored a raised left arm, torso, lowered right arm and clearly handled briefcase on the right.',
 'human_ref/full_body_ref.png: head radius 4 and continuous limbs; head (25,8) and torso start (25,20) have exactly 4px ink gap. Lucide id-card rounded rectangle construction informs the briefcase.',
 """
        circle('head',25,8,4)
        self.add_line('torso',(25,20),(25,44))
        self.add_polyline('wave',(25,20),(18,20),(10,9))
        self.add_polyline('carrying-arm',(25,20),(33,20),(36,24),(36,29))
        self.relate('connect','torso','wave');self.relate('connect','torso','carrying-arm')
        path('handle',(31,33),[('L',(31,31)),('A',(33,29),2,True),('L',(37,29)),('A',(39,31),2,True),('L',(39,33))])
        box('case',28,33,42,44,2)
        self.relate('connect','handle','case');self.relate('connect','carrying-arm','handle')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 """,shape='VRECT_L',omissions='Cropped torso retained as in the reference; no unrelated legs added.')

spec('broccoli-and-carrot',
 'The rejected image places a vertical narrow carrot beside a stump-like broccoli, losing the reference diagonal carrot and branched stalk.',
 'Restored a tilted carrot with a short surface notch, a three-stroke leafy top, and a branching broccoli stalk below rounded florets.',
 'Lucide carrot: tapered diagonal root and top leaves; supplied reference defines broccoli lobes and arrangement.',
 """
        path('florets',(8,23),[('C',(6,14),(3,23),(3,17)),('C',(13,10),(6,10),(9,9)),('C',(23,10),(15,3),(21,3)),('C',(29,16),(27,9),(30,12)),('C',(23,22),(31,21),(26,23)),('C',(15,24),(21,26),(18,25)),('C',(8,23),(12,27),(9,26))],True)
        path('stalk',(10,25),[('L',(15,35)),('L',(22,35)),('L',(22,24))])
        self.add_line('branch',(17,29),(22,24))
        path('carrot',(27,24),[('C',(40,32),(31,17),(42,22)),('C',(26,42),(36,37),(30,41)),('C',(23,38),(22,43),(22,40)),('C',(27,24),(23,33),(25,27))],True)
        self.add_line('carrot-mark',(27,27),(31,30))
        self.add_polyline('greens',(36,22),(36,15),(41,13))
        self.add_line('leaf',(36,22),(44,20))
        self.relate('connect','carrot-mark','carrot');self.relate('connect','greens','leaf')
 """,omissions='Fine floret bumps reduced to four lobes and carrot grooves to one notch.')

spec('browser-user-profile',
 'The rejected horizontal frame has disconnected header strokes and resembles a generic display rather than a browser; feedback specifically asks for Browser.',
 'Restored a full-width browser toolbar with two control dots and a separate centered person symbol below it.',
 'Lucide panels-top-left: continuous toolbar divider. human_ref/user.svg: circular head and broad open shoulder arch; head (24,25), radius3, shoulders begin y36, exact detached 4px ink gap.',
 """
        box('browser',6,6,42,42,4)
        self.add_line('toolbar',(6,16),(42,16))
        self.relate('connect','browser','toolbar')
        self.add_dot('control-a',(14,11));self.add_dot('control-b',(22,11))
        circle('head',24,25,3)
        path('shoulders',(15,40),[('C',(24,36),(16,37),(19,36)),('C',(33,40),(29,36),(32,37))])
 """,omissions='Browser controls reduced to two dots; profile remains detached from the outer frame.')

spec('canoe',
 'The rejected canoe has vertical horns and two internal braces, resembling a basket; the original is a low empty hull with a curved gunwale.',
 'Restored the shallow wide canoe hull and one smooth curved gunwale, removing the unrelated braces.',
 'No useful exact local Lucide canoe match; source supplies shallow hull, raised bow/stern and smooth gunwale.',
 """
        path('hull',(4,10),[('C',(24,17),(10,16),(17,17)),('C',(44,10),(31,17),(38,16)),('L',(44,29)),('C',(35,38),(44,36),(41,38)),('L',(13,38)),('C',(4,29),(7,38),(4,36)),('L',(4,10))],True)
 """,shape='HRECT_M',omissions='Removed all invented hull furniture; preserves the empty canoe shown in the original.')

spec('hand-holding-wrench',
 'The rejected drawing reduces the hand to crossed bars and changes the wrench jaw into a circular hook, losing the gripping action.',
 'Restored an open wrench jaw, diagonal handle, three rounded gripping fingers, and a thumb/palm wrapping around the tool.',
 'Lucide wrench: open angular jaw and tapered handle. Lucide hand-grab: stepped rounded fingers and coherent palm.',
 """
        path('wrench-head',(23,20),[('C',(36,6),(20,11),(27,3)),('L',(31,11)),('L',(36,16)),('L',(42,10)),('C',(30,24),(46,22),(38,29))])
        path('handle',(30,24),[('L',(13,42)),('C',(7,36),(8,47),(3,41)),('L',(12,31))])
        path('finger-top',(14,22),[('C',(19,17),(10,18),(15,13)),('L',(24,22)),('C',(19,27),(28,27),(23,31)),('L',(14,22))],True)
        path('finger-mid',(10,27),[('C',(14,22),(6,23),(9,19))])
        path('finger-low',(7,32),[('C',(10,27),(3,29),(5,24)),('L',(16,33))])
        path('palm',(37,42),[('C',(32,34),(33,39),(31,37)),('C',(34,27),(32,31),(35,30)),('L',(26,19))])
        self.add_line('wrist',(18,37),(23,42))
 """,omissions='Four source fingers reduced to three readable gripping arcs; tool mouth retained.')

spec('hand-massaging-foot-8ab52d55',
 'The rejected image resembles a fist facing a pointing hand: it lacks the rounded heel, large toe and a wrapping massage grip.',
 'Restored a sole with unequal rounded toes, heel and arch, plus a thumb pressing the sole and fingers wrapping around the foot.',
 'Lucide hand and hand-grab: rounded fingertip sequence and continuous grip; original supplies foot anatomy and massage contact.',
 """
        path('foot',(20,38),[('C',(7,35),(13,44),(7,41)),('C',(6,18),(5,30),(6,23)),('L',(6,10)),('C',(15,10),(3,1),(17,1)),('L',(15,13))])
        path('toes',(15,8),[('C',(21,11),(17,4),(22,6)),('C',(27,14),(23,7),(28,9)),('C',(31,18),(29,11),(33,13))])
        curve('arch',(11,28),(11,23),(14,20),(18,19))
        path('massage-hand',(30,44),[('L',(29,39)),('L',(19,28)),('C',(23,24),(16,24),(20,21)),('L',(29,31)),('L',(33,22)),('L',(30,20)),('C',(33,16),(26,17),(29,14)),('L',(39,19)),('C',(44,28),(43,20),(45,24)),('L',(40,38)),('L',(40,44))])
        self.add_line('finger-crease',(38,20),(37,27))
 """,omissions='Four toe bumps retained rather than five cramped marks; one arch crease and one finger crease.')

spec('hand-massaging-scalp-17e8bc26',
 'The rejected head profile is blocky and the oversized hand merges into an unclear zigzag, hiding the scalp massage.',
 'Restored a rounded side-profile head with forehead, nose, chin and neck, and a hand descending from above with separated finger tips on the scalp.',
 'human_ref/user.svg supplies circular head vocabulary; source is an anatomical side profile rather than a detached avatar. Lucide hand: rounded fingers.',
 """
        path('head',(27,14),[('C',(10,22),(17,8),(9,11)),('L',(6,28)),('L',(10,28)),('L',(10,33)),('C',(17,37),(10,37),(13,37)),('L',(19,37)),('L',(19,42))])
        path('neck',(32,42),[('L',(32,35)),('L',(36,30))])
        path('hand',(30,6),[('L',(27,12)),('L',(19,11)),('C',(18,17),(13,10),(13,16)),('L',(26,19)),('L',(23,27)),('C',(28,30),(21,31),(26,34)),('L',(32,22))])
        path('fingers',(32,22),[('L',(30,30)),('C',(35,32),(29,34),(33,36)),('C',(40,24),(38,31),(40,28)),('L',(38,16)),('L',(42,6))])
 """,omissions='Three hand fingers reduced to two open fingertip lobes and a thumb to avoid an unreadable comb of strokes.')

spec('hand-over-heat',
 'The rejected hand has a squared-off palm and heat is shown as three tiny squiggles; the reference is a horizontal palm held above rising heat.',
 'Restored a gently curved horizontal hand and wrist above two tall flowing heat waves, preserving the sensing-heat gesture.',
 'Lucide hand: coherent palm/thumb contour; source owns side-on horizontal hand and heat waves.',
 """
        path('hand-top',(36,8),[('L',(26,8)),('C',(17,11),(23,8),(20,10)),('L',(7,17)),('C',(10,24),(1,20),(4,27)),('L',(22,18)),('L',(29,18))])
        path('palm',(19,20),[('C',(24,26),(20,25),(21,26)),('L',(33,26)),('C',(39,22),(36,26),(38,24)),('L',(44,14))])
        for name,x in [('left',14),('right',29)]:
            curve(name,(x,32),(x-4,37),(x+4,39),(x,44))
 """,omissions='Three short heat marks replaced with two longer recognizable rising waves.')

spec('hand-playing-pad-controller',
 'The rejected pad is an F-shaped fragment rather than a grid, and the hand does not clearly press a pad.',
 'Restored a rounded 2-column pad grid, a raised index finger pressing its right pad, a rounded palm and an open musical note.',
 'Lucide panels-top-left: regular panel grid; hand: raised index and thumb; music-2: circular note head and upright stem.',
 """
        path('controller',(24,10),[('L',(9,10)),('A',(6,13),3,False),('L',(6,34)),('A',(9,37),3,False),('L',(14,37))])
        self.add_line('grid-vertical',(16,10),(16,31))
        self.add_line('grid-upper',(6,20),(24,20))
        self.add_line('grid-lower',(6,29),(16,29))
        self.relate('connect','controller','grid-vertical');self.relate('connect','controller','grid-upper');self.relate('connect','controller','grid-lower')
        self.relate('connect','grid-vertical','grid-upper');self.relate('connect','grid-vertical','grid-lower')
        path('hand',(24,42),[('L',(17,33)),('C',(21,29),(13,29),(17,25)),('L',(27,35)),('L',(27,23)),('C',(33,23),(27,18),(33,18)),('L',(33,31)),('L',(37,31)),('A',(42,36),5,True),('L',(42,42))])
        circle('note',37,13,3)
        self.add_polyline('stem',(40,13),(40,6),(44,8))
        self.relate('connect','note','stem')
 """,omissions='Dense source pad matrix reduced to 2 columns and 3 rows; paired notes reduced to one open note.')

spec('hand-playing-yoyo',
 'The rejected fingers are disconnected horizontal bars; the string intersects the palm ambiguously and the yoyo loses its center axle.',
 'Restored a side-on pinching hand, one clean slanting string, a circular yoyo with axle, and one motion arc.',
 'Lucide hand: continuous fingertip-to-palm flow. Source defines taut string, axle circle and swinging motion.',
 """
        path('hand-top',(42,6),[('L',(32,6)),('C',(22,6),(27,6),(25,4)),('L',(9,11)),('C',(11,18),(3,13),(5,21)),('L',(21,14)),('C',(29,15),(24,14),(26,16)),('L',(33,14))])
        path('hand-bottom',(16,16),[('L',(19,21)),('L',(29,23)),('C',(35,21),(32,23),(33,22)),('L',(38,19)),('L',(42,19))])
        self.add_line('string',(19,21),(25,32))
        circle('yoyo',32,36,8);circle('axle',32,36,2)
        curve('motion',(13,31),(8,34),(8,40),(13,43))
        self.relate('connect','hand-bottom','string')
 """,omissions='Two motion arcs reduced to one; axle retained as a small circular hole.')

spec('hand-pointing-down-batch-024-04',
 'The rejected contour has a large square upper-left kink and a swollen thumb, weakening the down-pointing hand silhouette.',
 'Restored a rounded palm, a long distinct downward index, three folded finger lobes and a short angled thumb.',
 'Lucide hand: shared fingertip radii and continuous palm. Original determines the downward pointing direction.',
 """
        path('hand',(15,24),[('L',(15,39)),('C',(23,39),(15,45),(23,45)),('L',(23,28)),('C',(29,29),(23,34),(29,34)),('L',(29,25)),('C',(35,26),(29,31),(35,31)),('L',(35,23)),('C',(41,24),(35,29),(41,29)),('L',(41,17)),('C',(28,6),(41,8),(36,6)),('L',(23,6)),('C',(16,10),(20,6),(18,8)),('L',(7,20)),('C',(11,26),(3,25),(7,29)),('L',(15,22))])
 """,omissions='No identifying parts omitted; thumb contour and fingertip lobes rebuilt with coherent curves.')

spec('hand-stealing-identity-card-solo-b005-06',
 'The rejected hand is three vertical prongs on a frame, not a hand pinching an identity card; the card avatar touches the border.',
 'Restored a hand reaching diagonally from the upper right to pinch the card edge, with a clear thumb and a separate identity portrait.',
 'Lucide id-card: rounded card and portrait hierarchy; hand-grab: grip outline. human_ref/user.svg supplies head/shoulder proportions; head (17,27),r3 and shoulder top38 have 4px ink gap.',
 """
        path('card',(27,18),[('L',(9,18)),('A',(6,21),3,False),('L',(6,39)),('A',(9,42),3,False),('L',(33,42)),('A',(36,39),3,False),('L',(36,24))])
        circle('head',17,27,3)
        curve('shoulders',(10,40),(11,37),(23,37),(24,40))
        path('hand-top',(42,6),[('L',(36,10)),('L',(28,10)),('C',(24,12),(26,10),(25,11)),('L',(18,18))])
        path('pinch',(31,16),[('L',(26,22)),('C',(30,27),(22,26),(27,30)),('L',(37,21)),('L',(42,19))])
 """,omissions='Card text omitted, preserving the portrait and the stealing/pinching gesture.')

spec('handcuffs-with-arched-connector',
 'The rejected cuffs are teardrop outlines without inner wrist holes; their arched connection makes the image read like headphones.',
 'Restored two circular cuff bodies with separate wrist openings, flat lock housings and a narrow high arched connector.',
 'Lucide link: separate connected loops; original owns the two cuff housings and tall connector.',
 """
        for name,x in [('left',13),('right',35)]:
            path(name,(x-4,23),[('L',(x-4,20)),('L',(x+4,20)),('L',(x+4,23)),('C',(x+8,32),(x+7,25),(x+8,28)),('C',(x,42),(x+8,38),(x+5,42)),('C',(x-8,32),(x-5,42),(x-8,38)),('C',(x-4,23),(x-8,28),(x-7,25))],True)
            circle(name+'-opening',x,32,4)
        path('connector',(13,20),[('L',(13,16)),('C',(24,6),(13,10),(17,6)),('C',(35,16),(31,6),(35,10)),('L',(35,20))])
        self.relate('connect','connector','left');self.relate('connect','connector','right')
 """,omissions='Lock rivets omitted; circular openings and rectangular housings retained.')

spec('handcuffs-with-curved-link',
 'The rejected drawing has two single-stroke rings and no locking housings, reading as a generic chain link rather than handcuffs.',
 'Restored two double-ring cuffs at staggered heights, rectangular locking collars, and a long curved connecting link.',
 'Lucide link: curved connection between loop structures; source defines staggered cuff placement and broad loop connector.',
 """
        circle('left-outer',13,34,9);circle('left-inner',13,34,4)
        circle('right-outer',35,22,9);circle('right-inner',35,22,4)
        path('left-lock',(9,26),[('L',(9,22)),('A',(11,20),2,True),('L',(17,20)),('A',(19,22),2,True),('L',(19,27))])
        path('right-lock',(28,16),[('L',(25,13)),('L',(31,8)),('L',(35,13))])
        path('link',(13,20),[('C',(5,9),(10,16),(3,15)),('C',(17,6),(7,4),(11,3)),('C',(27,11),(21,6),(24,8))])
 """,omissions='Tiny locking rivets omitted; both inner cuff holes and lock collars retained.')

spec('handled-comb-on-diagonal',
 'The rejected comb has only three thick teeth and a curled unconnected tip, reading as a rake rather than the reference handled comb.',
 'Restored a continuous diagonal spine, smooth handle and five evenly spaced comb teeth with a squared terminal tooth.',
 'No useful exact local Lucide comb match; source supplies a diagonal continuous spine and regular tooth series.',
 """
        path('spine',(16,31),[('L',(10,37)),('C',(5,32),(6,42),(1,37)),('L',(29,8)),('C',(35,8),(31,6),(33,6)),('L',(42,15))])
        # Five identical tooth runs; common spacing along the diagonal spine.
        for j in range(5):
            x=16+4*j;y=31-4*j
            self.add_line(f'tooth-{j}',(x,y),(x+7,y+7))
 """,omissions='Five teeth retained as a regular series; tiny handle irregularities removed.')

HELPERS='''
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
'''

def author(key,attempt='01'):
    s=SPECS[key];fix=ROOT/'icon_set/work/primitive-fix-thuan'/('solo__'+key)/'20260929T025914Z-thuan-mac'
    ref=next((fix/'reference').glob('*.svg')).relative_to(ROOT);uid=ref.stem[-36:]
    out=ROOT/'icon_set/work/primitive-make-ray'/uid/('20260929-meaning-thuan-mac-'+attempt);out.mkdir(parents=True,exist_ok=False)
    claim=json.loads((fix/'claim.json').read_text())['item']
    meta=dict(concept=ref.stem[:-37],source_uuid=uid,reference_path=str(ref),icon_id=key,author=AUTHOR,feedback=claim.get('feedback'),comparison=s['before'],changes=s['change'],construction_reference=s['refs'],omissions=s['omissions'],keyshape=s['keyshape'],fix_run=str(fix.relative_to(ROOT)))
    (out/(key+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
    (out/'review-before.md').write_text(s['before']+'\n\nFeedback: '+meta['feedback']+'\n\nRevision: '+s['change']+'\n')
    source=f'''"""{s['change']}\nSymbol plan: coherent named contours; repeated shapes use shared helpers.\nConstruction: {s['refs']}\nKeyshape: {s['keyshape']}; bounds checked and any deliberate optical deviation recorded.\nReduction: {s['omissions']}"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {'acro-yoga-folded-balance': '672c58c9-cf49-5d74-ba11-e6398667c047', 'adult-child-high-five-hands': 'b88757c2-b1ab-49df-9283-b755a2874066', 'airplane-rising-above-ground-line': '28bc625b-2596-540d-91c3-fb5e36336a56', 'baby-bottle-with-handles': '46fff59c-84bf-4526-bd9b-33201133c81c', 'box-delivery-truck': '0070eae2-79f7-4131-b3be-164ea822745d', 'briefcase-carrying-hailing-person': '459ca9bc-41c3-44a7-bd18-4322e40df660', 'broccoli-and-carrot': '1833535f-220e-490a-9e51-7058a14ac9db', 'browser-user-profile': '3a3e4d85-115c-4ccb-82d1-46fd45222b3a', 'canoe': '2f08daf6-071b-5ac7-9717-2239ffbb2925', 'hand-holding-wrench': '80b7765d-72c2-4b01-b0bf-6a084aa9bc97', 'hand-massaging-foot-8ab52d55': '8ab52d55-ae52-4c12-82e0-c8e7e2dc8409', 'hand-massaging-scalp-17e8bc26': '17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec', 'hand-over-heat': 'e2391138-4aaf-4587-83d5-f636e7ba5379', 'hand-playing-pad-controller': '2e9ddede-2e59-4491-8fa8-b1f79514c010', 'hand-playing-yoyo': '28a605e6-a545-47ed-ae21-f45557bb8374', 'hand-pointing-down-batch-024-04': '5a80cb54-e04f-5e41-ba53-6892a6852f05', 'hand-stealing-identity-card-solo-b005-06': '3ba267b5-9ca9-4999-a24d-b73d45e0c937', 'handcuffs-with-arched-connector': '404190ff-389e-4a15-a7fe-4b448b432ffd', 'handcuffs-with-curved-link': 'ad5f17ec-d6f2-402a-8907-dbd8532598e6', 'handled-comb-on-diagonal': 'dafdca17-4d27-4cd9-935d-01a08f4e53e2'}
SOURCE_PATH = {'acro-yoga-folded-balance': 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-folded-balance/20260929T025914Z-thuan-mac/reference/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg', 'adult-child-high-five-hands': 'icon_set/work/primitive-fix-thuan/solo__adult-child-high-five-hands/20260929T025914Z-thuan-mac/reference/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg', 'airplane-rising-above-ground-line': 'icon_set/work/primitive-fix-thuan/solo__airplane-rising-above-ground-line/20260929T025914Z-thuan-mac/reference/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg', 'baby-bottle-with-handles': 'icon_set/work/primitive-fix-thuan/solo__baby-bottle-with-handles/20260929T025914Z-thuan-mac/reference/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg', 'box-delivery-truck': 'icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260929T025914Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg', 'briefcase-carrying-hailing-person': 'icon_set/work/primitive-fix-thuan/solo__briefcase-carrying-hailing-person/20260929T025914Z-thuan-mac/reference/taxi wave businessman_459ca9bc-41c3-44a7-bd18-4322e40df660.svg', 'broccoli-and-carrot': 'icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260929T025914Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg', 'browser-user-profile': 'icon_set/work/primitive-fix-thuan/solo__browser-user-profile/20260929T025914Z-thuan-mac/reference/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg', 'canoe': 'icon_set/work/primitive-fix-thuan/solo__canoe/20260929T025914Z-thuan-mac/reference/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg', 'hand-holding-wrench': 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wrench/20260929T025914Z-thuan-mac/reference/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg', 'hand-massaging-foot-8ab52d55': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-foot-8ab52d55/20260929T025914Z-thuan-mac/reference/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg', 'hand-massaging-scalp-17e8bc26': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-scalp-17e8bc26/20260929T025914Z-thuan-mac/reference/massage head_17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec.svg', 'hand-over-heat': 'icon_set/work/primitive-fix-thuan/solo__hand-over-heat/20260929T025914Z-thuan-mac/reference/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg', 'hand-playing-pad-controller': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-pad-controller/20260929T025914Z-thuan-mac/reference/modern music mix touch_2e9ddede-2e59-4491-8fa8-b1f79514c010.svg', 'hand-playing-yoyo': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-yoyo/20260929T025914Z-thuan-mac/reference/playing yoyo_28a605e6-a545-47ed-ae21-f45557bb8374.svg', 'hand-pointing-down-batch-024-04': 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-down-batch-024-04/20260929T025914Z-thuan-mac/reference/hand pointer bottom_5a80cb54-e04f-5e41-ba53-6892a6852f05.svg', 'hand-stealing-identity-card-solo-b005-06': 'icon_set/work/primitive-fix-thuan/solo__hand-stealing-identity-card-solo-b005-06/20260929T025914Z-thuan-mac/reference/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg', 'handcuffs-with-arched-connector': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-arched-connector/20260929T025914Z-thuan-mac/reference/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg', 'handcuffs-with-curved-link': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-curved-link/20260929T025914Z-thuan-mac/reference/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg', 'handled-comb-on-diagonal': 'icon_set/work/primitive-fix-thuan/solo__handled-comb-on-diagonal/20260929T025914Z-thuan-mac/reference/hair dress comb_dafdca17-4d27-4cd9-935d-01a08f4e53e2.svg'}
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = {key!r}
    keyshape = Keyshape.{s['keyshape']}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = {tuple(key.split('-'))!r}

    def build(self):
'''+HELPERS+s['body']
    (out/(key.replace('-','_')+'_'+uid.replace('-','_')+'.py')).write_text(source)
    return out

if __name__=='__main__':
    selected=sys.argv[1:] or list(SPECS)
    paths=[str(author(k)) for k in selected]
    current=json.loads((BATCH/'runs.json').read_text()) if (BATCH/'runs.json').exists() else []
    (BATCH/'runs.json').write_text(json.dumps(current+paths,indent=2)+'\n')
    print('Authored',len(paths),'fresh runs.')
