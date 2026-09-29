"""Fresh second attempts after native visual review; source identity retained by author()."""
from pathlib import Path
import json
from _author import SPECS,author,BATCH
AUTHOR='gpt-6'
SOURCE_ICON_ID = {'acro-yoga-folded-balance': '672c58c9-cf49-5d74-ba11-e6398667c047', 'adult-child-high-five-hands': 'b88757c2-b1ab-49df-9283-b755a2874066', 'airplane-rising-above-ground-line': '28bc625b-2596-540d-91c3-fb5e36336a56', 'baby-bottle-with-handles': '46fff59c-84bf-4526-bd9b-33201133c81c', 'box-delivery-truck': '0070eae2-79f7-4131-b3be-164ea822745d', 'briefcase-carrying-hailing-person': '459ca9bc-41c3-44a7-bd18-4322e40df660', 'broccoli-and-carrot': '1833535f-220e-490a-9e51-7058a14ac9db', 'browser-user-profile': '3a3e4d85-115c-4ccb-82d1-46fd45222b3a', 'canoe': '2f08daf6-071b-5ac7-9717-2239ffbb2925', 'hand-holding-wrench': '80b7765d-72c2-4b01-b0bf-6a084aa9bc97', 'hand-massaging-foot-8ab52d55': '8ab52d55-ae52-4c12-82e0-c8e7e2dc8409', 'hand-massaging-scalp-17e8bc26': '17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec', 'hand-over-heat': 'e2391138-4aaf-4587-83d5-f636e7ba5379', 'hand-playing-pad-controller': '2e9ddede-2e59-4491-8fa8-b1f79514c010', 'hand-playing-yoyo': '28a605e6-a545-47ed-ae21-f45557bb8374', 'hand-pointing-down-batch-024-04': '5a80cb54-e04f-5e41-ba53-6892a6852f05', 'hand-stealing-identity-card-solo-b005-06': '3ba267b5-9ca9-4999-a24d-b73d45e0c937', 'handcuffs-with-arched-connector': '404190ff-389e-4a15-a7fe-4b448b432ffd', 'handcuffs-with-curved-link': 'ad5f17ec-d6f2-402a-8907-dbd8532598e6', 'handled-comb-on-diagonal': 'dafdca17-4d27-4cd9-935d-01a08f4e53e2'}
SOURCE_PATH = {'acro-yoga-folded-balance': 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-folded-balance/20260929T025914Z-thuan-mac/reference/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg', 'adult-child-high-five-hands': 'icon_set/work/primitive-fix-thuan/solo__adult-child-high-five-hands/20260929T025914Z-thuan-mac/reference/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg', 'airplane-rising-above-ground-line': 'icon_set/work/primitive-fix-thuan/solo__airplane-rising-above-ground-line/20260929T025914Z-thuan-mac/reference/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg', 'baby-bottle-with-handles': 'icon_set/work/primitive-fix-thuan/solo__baby-bottle-with-handles/20260929T025914Z-thuan-mac/reference/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg', 'box-delivery-truck': 'icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260929T025914Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg', 'briefcase-carrying-hailing-person': 'icon_set/work/primitive-fix-thuan/solo__briefcase-carrying-hailing-person/20260929T025914Z-thuan-mac/reference/taxi wave businessman_459ca9bc-41c3-44a7-bd18-4322e40df660.svg', 'broccoli-and-carrot': 'icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260929T025914Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg', 'browser-user-profile': 'icon_set/work/primitive-fix-thuan/solo__browser-user-profile/20260929T025914Z-thuan-mac/reference/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg', 'canoe': 'icon_set/work/primitive-fix-thuan/solo__canoe/20260929T025914Z-thuan-mac/reference/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg', 'hand-holding-wrench': 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wrench/20260929T025914Z-thuan-mac/reference/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg', 'hand-massaging-foot-8ab52d55': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-foot-8ab52d55/20260929T025914Z-thuan-mac/reference/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg', 'hand-massaging-scalp-17e8bc26': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-scalp-17e8bc26/20260929T025914Z-thuan-mac/reference/massage head_17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec.svg', 'hand-over-heat': 'icon_set/work/primitive-fix-thuan/solo__hand-over-heat/20260929T025914Z-thuan-mac/reference/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg', 'hand-playing-pad-controller': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-pad-controller/20260929T025914Z-thuan-mac/reference/modern music mix touch_2e9ddede-2e59-4491-8fa8-b1f79514c010.svg', 'hand-playing-yoyo': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-yoyo/20260929T025914Z-thuan-mac/reference/playing yoyo_28a605e6-a545-47ed-ae21-f45557bb8374.svg', 'hand-pointing-down-batch-024-04': 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-down-batch-024-04/20260929T025914Z-thuan-mac/reference/hand pointer bottom_5a80cb54-e04f-5e41-ba53-6892a6852f05.svg', 'hand-stealing-identity-card-solo-b005-06': 'icon_set/work/primitive-fix-thuan/solo__hand-stealing-identity-card-solo-b005-06/20260929T025914Z-thuan-mac/reference/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg', 'handcuffs-with-arched-connector': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-arched-connector/20260929T025914Z-thuan-mac/reference/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg', 'handcuffs-with-curved-link': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-curved-link/20260929T025914Z-thuan-mac/reference/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg', 'handled-comb-on-diagonal': 'icon_set/work/primitive-fix-thuan/solo__handled-comb-on-diagonal/20260929T025914Z-thuan-mac/reference/hair dress comb_dafdca17-4d27-4cd9-935d-01a08f4e53e2.svg'}

SPECS['adult-child-high-five-hands']['body']='''
        path('rear-thumb',(42,40),[('L',(38,35)),('L',(38,24)),('L',(36,12)),('C',(30,12),(35,7),(30,7)),('L',(30,17))])
        path('rear-index',(28,18),[('L',(15,8)),('C',(10,12),(11,3),(6,8)),('L',(17,19))])
        path('rear-middle',(10,12),[('C',(7,18),(5,10),(3,15)),('L',(13,23))])
        path('rear-little',(7,18),[('C',(8,28),(1,18),(4,24))])
        path('small-hand',(13,42),[('C',(6,34),(8,42),(6,39)),('C',(9,27),(6,31),(7,29)),('L',(20,16)),('C',(25,20),(25,11),(30,16)),('L',(29,17)),('C',(32,22),(34,13),(37,18)),('C',(35,28),(37,20),(40,24)),('L',(26,36)),('L',(30,35)),('C',(32,40),(35,33),(36,38)),('L',(21,42)),('C',(13,42),(18,43),(15,43))],True)
        self.add_line('finger-a',(25,20),(17,28))
        self.add_line('finger-b',(32,22),(24,30))
        self.relate('connect','small-hand','finger-a');self.relate('connect','small-hand','finger-b')
'''

s=SPECS['baby-bottle-with-handles'];s['body']=s['body'].replace("('C',(17,13),(10,10),(14,10))","('C',(17,18),(10,10),(14,12))")

SPECS['broccoli-and-carrot']['body']='''
        path('florets',(9,23),[('C',(4,18),(5,25),(2,22)),('C',(9,11),(4,13),(6,10)),('L',(12,11)),('C',(22,11),(14,3),(21,3)),('C',(26,16),(26,10),(28,13)),('C',(20,23),(28,21),(24,25)),('C',(14,24),(18,26),(16,26)),('L',(9,23))],True)
        path('stalk',(10,24),[('L',(14,34)),('L',(19,34)),('L',(21,24))])
        path('carrot',(36,22),[('C',(40,31),(41,22),(43,27)),('C',(27,42),(36,36),(30,40)),('C',(25,38),(24,44),(24,40)),('C',(30,25),(25,32),(28,26)),('C',(36,22),(32,23),(34,22))],True)
        self.add_polyline('greens',(36,22),(36,14),(42,12))
        self.add_line('leaf',(36,22),(44,19))
        self.relate('connect','carrot','greens');self.relate('connect','carrot','leaf');self.relate('connect','greens','leaf')
'''
SPECS['broccoli-and-carrot']['omissions']='Fine floret detail and carrot grooves omitted to separate the two vegetables clearly.'
SPECS['broccoli-and-carrot']['change']='Restored a tilted carrot with a leafy top and a distinct branching broccoli stalk beneath rounded florets; separated the two silhouettes.'

SPECS['browser-user-profile']['body']='''
        box('browser',8,4,40,44,4)
        self.add_line('toolbar',(8,14),(40,14));self.relate('connect','browser','toolbar')
        self.add_dot('control-a',(16,9));self.add_dot('control-b',(24,9))
        circle('head',24,23,3)
        path('shoulders',(16,37),[('C',(24,34),(16,35),(20,34)),('C',(32,37),(28,34),(32,35))])
'''
SPECS['browser-user-profile']['keyshape']='VRECT_L'
SPECS['browser-user-profile']['refs']='Lucide panels-top-left: continuous toolbar divider. human_ref/user.svg: circular head and broad open shoulders; head (24,23), r3 and shoulder apex (24,34) yield exactly 4px detached ink gap.'

SPECS['hand-stealing-identity-card-solo-b005-06']['body']='''
        path('card',(29,16),[('L',(9,16)),('A',(6,19),3,False),('L',(6,41)),('A',(9,44),3,False),('L',(33,44)),('A',(36,41),3,False),('L',(36,24))])
        circle('head',17,25,3)
        path('shoulders',(10,38),[('C',(17,36),(11,36),(14,36)),('C',(24,38),(20,36),(23,36))])
        path('hand-top',(42,6),[('L',(36,10)),('L',(28,10)),('C',(24,12),(26,10),(25,11)),('L',(20,16))])
        path('pinch',(31,16),[('L',(26,22)),('C',(30,27),(22,26),(27,30)),('L',(37,21)),('L',(42,19))])
'''
SPECS['hand-stealing-identity-card-solo-b005-06']['refs']='Lucide id-card and hand-grab: card/portrait hierarchy and grip. human_ref/user.svg: head (17,25), r3 and shoulder apex (17,36) yield exactly 4px detached ink gap.'

s=SPECS['handled-comb-on-diagonal'];s['body'] += '''
        self.add_line('inner-spine',(16,31),(32,15))
        self.relate('connect','spine','inner-spine')
        for j in range(5):self.relate('connect','inner-spine',f'tooth-{j}')
'''

s=SPECS['handcuffs-with-arched-connector']
s['body']=s['body'].replace("('left',13),('right',35)","('left',12),('right',36)").replace('x+8','x+10').replace('x-8','x-10').replace("(13,20)","(12,20)").replace("(13,16)","(12,16)").replace("(13,10)","(12,10)").replace("(35,16)","(36,16)").replace("(35,10)","(36,10)").replace("(35,20)","(36,20)")
s=SPECS['handcuffs-with-curved-link'];s['body']=s['body'].replace("13,34,9","13,34,10").replace("35,22,9","35,22,10")

keys=['adult-child-high-five-hands','baby-bottle-with-handles','broccoli-and-carrot','browser-user-profile','hand-stealing-identity-card-solo-b005-06','handled-comb-on-diagonal','handcuffs-with-arched-connector','handcuffs-with-curved-link']
paths=json.loads((BATCH/'runs.json').read_text())
for key in keys:
    p=author(key,'02')
    paths=[str(p) if Path(old).parent==p.parent else old for old in paths]
(BATCH/'runs.json').write_text(json.dumps(paths,indent=2)+'\n')
print('Revised',len(keys),'icons in fresh runs.')
