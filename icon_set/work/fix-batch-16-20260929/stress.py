from refine import *
D['stressed-person']['code']='''
oval('head',24,26,6,6)
path('shoulders',(8,44),[('A',(24,40),16,4,True),('A',(40,44),16,4,True)])
poly('stress-left',(8,4),(14,8),(8,14),(12,18));poly('stress-right',(40,4),(34,8),(40,14),(36,18))
'''
if __name__=='__main__':generate(['stressed-person'])
