from revise2 import *
SPECS[6]['code']='''
circle('head',24,14,10)
bez('smile',(23,14),((23,16),(25,16),(25,14)))
line('body-left-side',(8,44),(8,36));arc('body-left',(8,36),(24,28),16,8)
arc('body-right',(24,28),(40,36),16,8);line('body-right-side',(40,36),(40,44))
join('body-left-side','body-left');join('body-right-side','body-right')
join('head','body-left');join('head','body-right')
poly('emblem',(18,44),(14,40),(18,36),(24,36),(30,36),(34,40),(30,44))
line('collar',(24,28),(24,36));join('collar','body-left','body-right','emblem')
'''
SPECS[6]['note']='The rejected superhero has a small blank head and generic arched shoulders. No written feedback. Restored a smile, broad cape shoulders and an open shield-like chest panel connected to the collar. Tiny eyes and hair seams are omitted; the panel remains open at the bottom as in the cropped source.'
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
