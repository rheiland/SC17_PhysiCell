# find_corner_runs.py - find those runs (instance* dirs) that have some of the data we want to vis
#
from glob import glob

print('              attach  attach           migrate ')
print('               rate  lifetime           bias')
rand_seed_prev = "-1"
num_missing_in_seed = 0

for idx in range(1,271):
  fdir = "instance_%d" % idx
  fname = "%s/params.txt" % (fdir)
#  print(fdir + ": ",end='')
  try:
    with open(fname,'r') as f:
      l = f.readline()

# [attachment_rate] [attachment_lifetime]
# [oncoprotein_detection_threshold] [oncoprotein_saturation]
# [migration_bias] [kill_rate]
# [detailed_output (0 or 1)] [omp_num_threads] [random seed value]

      v = l.split()
      if (v[8] != rand_seed_prev):
        if (num_missing_in_seed == 0):
          print("")
          print("      NO MISSES  <<<<<<<<<<<<<")
          print("")
        print("=================")
        rand_seed_prev = v[8]
        num_missing_in_seed = 0
#    print(float(v[0]),int(v[1]),float(v[2]), sep='\t')

      modval = (idx-1) % 27
#      print("modval = ",modval)
      if (modval==0 or modval==2 or modval==6 or modval==8): 
        print('{:13}: {:6}: {:4}: {:4}: {:3}: {:5}: {:6}: {:3}: {:3}: {:6}'.format(fdir,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8]))
#        print(l,sep='\t',end='')
  except:
    print('{:13}: {:10}'.format(fdir,"--- missing ---"))
    num_missing_in_seed += 1
    pass
