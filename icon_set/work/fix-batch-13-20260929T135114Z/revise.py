import designs_more as a
from author import *
D=a.D
D['happy-chat-bubbles']['code']=D['happy-chat-bubbles']['code'].replace("(14,24),[('C',(20,24),(16,27),(18,27))]","(15,24),[('C',(19,24),(16,26),(18,26))]")
D['kimono-sash-belt']['code']='''
box('buckle',12,10,36,38,4)
oval('opening',24,24,3,3)
poly('left-strap',(12,16),(4,16),(4,32),(12,32));join('left-strap','buckle')
poly('right-strap',(36,16),(44,16),(44,32),(36,32));join('right-strap','buckle')
'''
D['kimono-sash-belt']['omissions']='Inner rectangular slot reduced to round opening to maintain clear spacing.'
D['mobile-phone-outgoing-arrow']['code']=D['mobile-phone-outgoing-arrow']['code'].replace('(34,14),(42,22),(34,30)','(36,16),(42,22),(36,28)')
D['person-with-radiant-aura']['human_construction']='bust'
D['person-with-radiant-aura']['code']=D['person-with-radiant-aura']['code'].replace('(9,27)','(8,28)').replace('(39,27)','(40,28)')
D['person-with-spiritual-enlightenment-symbols']['human_construction']='bust'
D['person-with-spiritual-enlightenment-symbols']['code']=D['person-with-spiritual-enlightenment-symbols']['code'].replace("(14,21),(16,23)","(15,22),(16,21)").replace("(34,21),(32,23)","(33,22),(32,21)")
D['performance-decrease']['shape']='HRECT_L'
D['performance-decrease']['code']='''
line('baseline',(4,40),(44,40))
for j,(x,top) in enumerate([(4,20),(20,28),(36,32)]):
 poly(f'bar{j}',(x,40),(x,top),(x+8,top),(x+8,40));join(f'bar{j}','baseline')
line('trend',(6,8),(42,22));poly('arrow',(34,20),(42,22),(40,12));join('trend','arrow')
'''
D['person-magnifying-glass']['code']=D['person-magnifying-glass']['code'].replace('21,18,4,4','21,19,4,4').replace("(12,33),[('A',(30,33),9,3,True)]","(12,33),[('A',(30,33),9,2,True)]").replace('bottom22; shoulder apex30','bottom23; shoulder apex31')
D['person-snowboarding-downhill-upload-52ddb7b225333f49']['code']='''
oval('head',32,10,4,4)
poly('torso',(32,22),(32,26),(24,30))
poly('front-leg',(24,30),(36,32),(32,40));join('front-leg','torso')
poly('back-arm',(32,22),(22,22),(14,28));join('back-arm','torso')
line('front-arm',(32,22),(40,26));join('front-arm','torso');join('front-arm','back-arm')
poly('rear-leg',(24,30),(16,30),(12,38));join('rear-leg','torso');join('rear-leg','front-leg')
path('board',(6,36),[('C',(32,42),(14,40),(24,42)),('C',(42,40),(37,42),(40,41))]);join('board','rear-leg');join('board','front-leg')
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
'''
D['person-with-round-hat-and-bob']['human_construction']='bust'
D['person-with-round-hat-and-bob']['code']='''
path('hat',(8,22),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,22))])
oval('head',24,21,7,7)
for s in (-1,1):
 x=lambda d:24+s*d
 path(f'hair{s}',(x(16),22),[('L',(x(16),32)),('L',(x(11),36))]);join(f'hair{s}','hat')
path('body',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('head','body')
join('hair-1','body');join('hair1','body')
'''
D['personal-hotspot-connection']['shape']='HRECT_L'
D['personal-hotspot-connection']['code']='''
path('upper-link',(4,18),[('A',(14,8),10,10,True),('L',(30,8)),('A',(30,28),10,10,True),('L',(26,28))])
path('lower-link',(24,20),[('L',(22,20)),('A',(22,40),10,10,False),('L',(34,40)),('A',(44,30),10,10,False)])
'''
if __name__=='__main__':
 import author
 author.D=D;idx=json.loads((B/'runs.json').read_text());generate(sys.argv[1:] or [k for k in D if not idx[k]['valid']])
