from stress import *
D['smart-tv-and-phone']['code']=D['smart-tv-and-phone']['code'].replace('34,14,42,26,2','34,14,42,25,2')
D['tooth-with-dental-floss-upload-79ce34090d76e090']['code']='''
path('tooth',(18,10),[('C',(8,8),(14,10),(10,8)),('C',(4,18),(5,8),(4,13)),('L',(6,26)),('L',(8,36)),('A',(14,36),3,3,False),('L',(17,28)),('A',(23,28),3,3,True),('L',(26,36)),('A',(32,36),3,3,False),('L',(34,24)),('L',(34,18)),('C',(30,8),(34,13),(33,8)),('C',(18,10),(28,8),(23,10))],True)
path('floss',(34,18),[('C',(44,28),(40,18),(44,22)),('L',(44,38)),('A',(40,38),2,2,True)]);join('tooth','floss')
'''
if __name__=='__main__':generate(['smart-tv-and-phone','tooth-with-dental-floss-upload-79ce34090d76e090'])
