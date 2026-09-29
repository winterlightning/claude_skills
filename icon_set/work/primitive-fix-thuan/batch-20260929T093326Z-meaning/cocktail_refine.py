from final_shapes import *
k,n,p,c=DESIGNS[6]
c=c.replace("path('glass',(14,32),[('L',(34,32)),('A',(24,40),10,8,True),('A',(14,32),10,8,True)],True)","path('glass',(14,30),[('L',(34,30)),('A',(24,37),10,7,True),('A',(14,30),10,7,True)],True)")
c=c.replace("(24,40),(24,44)","(24,37),(24,44)")
replace(6,c)
author([6],'e')
