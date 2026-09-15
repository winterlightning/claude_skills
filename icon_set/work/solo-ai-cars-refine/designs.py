SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-next100/batch.json'
AUTHOR='gpt-6'
design('car','HRECT_L','Fuller body and inset wheels','car','Restore full round wheels inside the lower body silhouette and a broader compact cabin. Coherent curved shoulders replace thin projecting bumpers.', """
path('body',(6,34),[('C',(4,24),(4,32),(4,28)),('C',(10,18),(4,20),(6,18)),('L',(14,10)),('C',(18,8),(15,8),(16,8)),('L',(26,8)),('L',(32,18)),('C',(44,24),(40,18),(44,20)),('C',(42,34),(44,28),(44,32)),('A',(36,40),6,6,True),('A',(30,34),6,6,True),('L',(18,34)),('A',(12,40),6,6,True),('A',(6,34),6,6,True)],True)
for x in (12,36):
 path(f'wheel-{x}',(x-6,34),[('A',(x,28),6,6,True),('A',(x+6,34),6,6,True)]);join(f'wheel-{x}','body')
""")
# Every car uses full round tyres integrated into its body, with matching quarters.
def car_design(name,roof,belt=False,pillar=None,handle=False,label='Restored car proportions'):
 front=[('C',(4,24),(4,32),(4,28)),('C',(10,18),(4,20),(6,18))]
 back=[('C',(44,24),(40,18),(44,20)),('C',(42,34),(44,28),(44,32)),('A',(36,40),6,6,True),('A',(30,34),6,6,True),('L',(18,34)),('A',(12,40),6,6,True),('A',(6,34),6,6,True)]
 body=f"path('body',(6,34),{front+roof+back!r},True)\n"
 body+="""
for x in (12,36):
 path(f'wheel-{x}',(x-6,34),[('A',(x,28),6,6,True),('A',(x+6,34),6,6,True)]);join(f'wheel-{x}','body')
"""
 if belt:
  nodes=[(10,18)]+([(pillar,18)] if pillar else [])+[(38,18)]
  body+=f"poly('windshield-base',*{nodes!r});join('windshield-base','body')\n"
 if pillar:body+=f"line('pillar',({pillar},8),({pillar},18));join('pillar','body');join('pillar','windshield-base')\n"
 if handle:body+="line('door-handle',(18,20),(24,20))\n"
 design(name,'HRECT_L',label,'car','Preserve the original car silhouette with a full lower body, broad round wheels and smooth shoulders. The roof profile and windshield treatment retain this variant’s identity.',body)
car_design('car-2',[('L',(14,10)),('C',(18,8),(15,8),(16,8)),('L',(22,8)),('L',(27,8)),('C',(31,10),(29,8),(30,8)),('L',(38,18))],True,22,label='Compact hatchback')
car_design('car-5e6ba5b0',[('L',(14,12)),('C',(20,8),(15,9),(17,8)),('L',(28,8)),('C',(34,12),(31,8),(33,9)),('L',(38,18))],True,label='Rounded sedan')
car_design('car-796e3289',[('L',(14,12)),('C',(20,8),(16,9),(18,8)),('L',(27,8)),('C',(31,13),(29,8),(30,11)),('L',(34,18)),('L',(38,18))],label='Soft compact car')
car_design('car-9e5f3201',[('L',(13,12)),('C',(18,8),(14,9),(15,8)),('L',(30,8)),('C',(35,12),(33,8),(34,9)),('L',(38,18))],True,label='Wide cabin sedan')
car_design('car-eaa7f06c',[('L',(14,10)),('C',(17,8),(15,8),(16,8)),('L',(27,8)),('C',(31,11),(29,8),(30,9)),('L',(35,18)),('L',(38,18))],True,label='Short cabin hatchback')
car_design('car-side',[('L',(16,8)),('L',(29,8)),('L',(37,18)),('L',(38,18))],True,label='Angular side-view car')
car_design('car-transportation',[('L',(14,10)),('C',(20,8),(16,8),(18,8)),('L',(27,8)),('C',(31,11),(29,8),(30,10)),('L',(38,18))],handle=True,label='Compact utility car')
car_design('car-e1ae9ac1',[('L',(12,18)),('C',(24,8),(12,12),(18,8)),('C',(36,18),(30,8),(36,12)),('L',(38,18))],True,24,label='Round roof compact')
car_design('car-retro',[('L',(14,18)),('C',(26,8),(14,12),(20,8)),('C',(38,18),(32,8),(38,12))],True,26,label='Offset vintage roof')
car_design('convertible',[('L',(16,18)),('C',(23,24),(17,22),(19,24)),('C',(30,18),(27,24),(29,22)),('L',(38,18))],label='Open-top convertible')
k,label,ref,plan,body=DESIGNS['convertible'];DESIGNS['convertible']=(k,label,ref,plan,body+"\nline('windshield',(12,8),(12,18));join('windshield','body')\nline('seat',(27,8),(30,18));join('seat','body')\n")
k,label,ref,plan,body=DESIGNS['convertible'];DESIGNS['convertible']=(k,label,ref,plan,body.replace("('C', (23, 24), (17, 22), (19, 24))","('C', (23, 22), (17, 20), (19, 22))").replace("('C', (30, 18), (27, 24), (29, 22))","('C', (30, 18), (27, 22), (29, 20))"))
