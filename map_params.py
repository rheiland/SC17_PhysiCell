# map_params.py - pretty-print the mapping between sets of params and ANL runs (Instance* dirs)
#
from glob import glob

print('              attach  attach           migrate ')
print('               rate  lifetime           bias')
for idx in range(1,271):
  fdir = "instance_%d" % idx
  fname = "%s/params.txt" % (fdir)
#  print(fdir + ": ",end='')
  try:
    with open(fname,'r') as f:
      l = f.readline()
#    print(l.split(),end='')
      v = l.split()
#    print(float(v[0]),int(v[1]),float(v[2]), sep='\t')
      print('{:13}: {:6}: {:4}: {:4}: {:3}: {:5}: {:6}: {:3}: {:3}: {:6}'.format(fdir,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8]))
#    print(l,sep='\t',end='')
  except:
    print('{:13}: {:10}'.format(fdir,"--- missing ---"))
#    print(fdir,': --- missing ---')
    pass
