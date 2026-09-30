from revise import *
D['seat-find']['code']=D['seat-find']['code'].replace('(14,32)','(14,34)').replace('(20,35)','(20,37)')
D['smiling-tree-trunk-batch-086']['code']=D['smiling-tree-trunk-batch-086']['code'].replace('(12,','(11,').replace('(36,','(37,')
D['smiling-tree-trunk-batch-086']['code']=D['smiling-tree-trunk-batch-086']['code'].replace("[('L',(4,12)),('A',(11,20),8,8,False)]","[('C',(11,20),(4,18),(6,20))]").replace("[('L',(44,12)),('A',(37,20),8,8,True)]","[('C',(37,20),(44,18),(42,20))]")
D['spool-wrapped-with-thread']['code']=D['spool-wrapped-with-thread']['code'].replace("box('thread-body',8,12,40,36,2)","path('thread-body',(10,12),[('L',(16,12)),('L',(32,12)),('L',(36,12)),('L',(38,12)),('A',(40,14),2,2,True),('L',(40,28)),('L',(40,34)),('A',(38,36),2,2,True),('L',(32,36)),('L',(16,36)),('L',(12,36)),('L',(10,36)),('A',(8,34),2,2,True),('L',(8,20)),('L',(8,14)),('A',(10,12),2,2,True)],True)")
if __name__=='__main__':generate(sys.argv[1:])
