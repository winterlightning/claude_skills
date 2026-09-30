from revise3 import *
D['smart-tv-and-phone']['code']=D['smart-tv-and-phone']['code'].replace("('L',(25,34))","('L',(42,34))").replace("34,14,42,34,2","34,14,42,26,2")
D['tooth-with-dental-floss-upload-79ce34090d76e090']['code']='''
path('tooth',(17,10),[('C',(8,8),(14,10),(10,8)),('C',(4,18),(5,8),(4,13)),('L',(6,26)),('L',(8,36)),('A',(14,36),3,3,False),('L',(15,28)),('A',(21,28),3,3,True),('L',(21,36)),('A',(27,36),3,3,False),('L',(30,24)),('L',(30,18)),('C',(26,8),(30,13),(29,8)),('C',(17,10),(24,8),(21,10))],True)
path('floss',(30,18),[('C',(44,28),(40,18),(44,22)),('L',(44,36)),('A',(36,36),4,4,True)]);join('tooth','floss')
'''
if __name__=='__main__':generate(['smart-tv-and-phone','tooth-with-dental-floss-upload-79ce34090d76e090'])
