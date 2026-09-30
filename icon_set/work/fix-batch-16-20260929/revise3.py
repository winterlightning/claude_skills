from revise2 import *
D['spotify-logo-1']['code']=D['spotify-logo-1']['code'].replace('(33,19)','(32,18)')
D['stressed-person']['code']=D['stressed-person']['code'].replace('(12,8)','(14,8)').replace('(36,8)','(34,8)')
D['two-eggs-in-decorated-bowl']['code']=D['two-eggs-in-decorated-bowl']['code'].replace('(16,30)','(18,30)').replace('(32,30)','(30,30)')
D['police-officer-with-sunglasses-and-pocket']['issue']='The rejected glasses collapse into eye slits and the hat has sharp corners. Restore the broad rounded hat and separate sunglass lenses over a circular jaw. The pocket is omitted after spacing trials.'
if __name__=='__main__':generate(['spotify-logo-1','stressed-person','two-eggs-in-decorated-bowl'])
