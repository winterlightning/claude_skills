from mochi import *
D['police-officer-with-sunglasses-and-pocket']['code']='''
path('hat',(12,12),[('L',(14,8)),('A',(18,4),4,4,True),('L',(30,4)),('A',(34,8),4,4,True),('L',(36,12))])
poly('brim',(8,12),(12,12),(24,12),(36,12),(40,12));join('hat','brim')
path('jaw',(40,12),[('A',(8,12),16,16,True)]);join('jaw','brim')
for n,l,r in [('left',8,24),('right',24,40)]:
 path(n+'lens',(l,12),[('A',(r,12),8,8,False)]);join(n+'lens','brim');join(n+'lens','jaw')
join('leftlens','rightlens')
path('body',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('jaw','body')
'''
if __name__=='__main__':generate(['police-officer-with-sunglasses-and-pocket'])
