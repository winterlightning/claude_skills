import revise as a
from author import *
D=a.D
D['mobile-phone-outgoing-arrow']['code']=D['mobile-phone-outgoing-arrow']['code'].replace('(28,30)','(28,31)').replace('(28,14)','(28,13)')
D['person-with-spiritual-enlightenment-symbols']['code']=D['person-with-spiritual-enlightenment-symbols']['code'].replace('(21,15),(24,18),(27,15)','(22,15),(24,17),(26,15)')
D['person-magnifying-glass']['human_construction']='bust'
D['person-magnifying-glass']['code']=D['person-magnifying-glass']['code'].replace("(12,33),[('A',(30,33),9,2,True)]","(12,33),[('A',(30,33),9,6,True)]").replace("join('shoulders','lens')","join('shoulders','lens');join('head','shoulders')").replace('# Head bottom23; shoulder apex31: exact4-unit ink gap.','# Circular head bottom23 and shoulder apex27 give exact touching-ink bust contact.')
D['person-magnifying-glass']['lucide']='search plus human_ref/user.svg: circular face, broad curved shoulders, touching-ink bust contact'
D['person-snowboarding-downhill-upload-52ddb7b225333f49']['code']='''
oval('head',32,10,4,4)
line('torso',(32,22),(32,30))
poly('front-leg',(32,30),(20,34),(16,40));join('front-leg','torso')
line('back-arm',(32,22),(20,24));join('back-arm','torso')
line('front-arm',(32,22),(42,24));join('front-arm','torso');join('front-arm','back-arm')
poly('rear-leg',(32,30),(40,34),(36,42));join('rear-leg','torso');join('rear-leg','front-leg')
path('board',(6,36),[('C',(16,40),(10,38),(12,39)),('C',(36,42),(24,42),(30,42)),('C',(42,40),(39,42),(41,41))]);join('board','front-leg');join('board','rear-leg')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''
D['kimono-sash-belt']['code']='''
box('buckle',10,10,38,38,4)
box('opening',20,20,28,28)
for s in (-1,1):
 x=lambda d:24+s*d
 for y in (18,30):line(f'strap{s}-{y}',(x(20),y),(x(14),y));join(f'strap{s}-{y}','buckle')
'''
D['kimono-sash-belt']['omissions']='Outer strap end walls omitted; rectangular buckle opening retained.'
D['person-with-halo']['human_construction']='bust'
D['person-with-halo']['code']=D['person-with-halo']['code'].replace("16,4,True)]","16,8,True)]").replace('# Head bottom32; shoulder apex40: exactly8 centerline /4 ink.',"join('head','shoulders')\n# Head bottom32; shoulder apex36: exact touching-ink bust contact.")
D['lightbulb-speech-bubble']['code']+="\nline('bulb-base',(24,25),(24,34));join('bulb-base','bulb');join('bulb-base','bubble')\n"
if __name__=='__main__':
 import author
 author.D=D;idx=json.loads((B/'runs.json').read_text());generate(sys.argv[1:] or [k for k in D if not idx[k]['valid']]+['kimono-sash-belt','person-with-halo','lightbulb-speech-bubble'])
