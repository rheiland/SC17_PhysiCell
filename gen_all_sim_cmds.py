# genall.py - one way to generate all param set runs (but ANL used their own which was different)
#
# << "cancer-immune-EMEWS [attachment_rate] [attachment_lifetime] ... " << std::endl
# << "\t[oncoprotein_detection_threshold] [oncoprotein_saturation]" << std::endl << std::endl
# << "\t[migration_bias] [kill_rate]" << std::endl << std::endl
# << "\t[detailed_output (0 or 1)] [omp_num_threads] [random seed value]" << std::endl << std::endl
# << "Good defaults: " << std::endl
# << "cancer-immune-EMEWS  0.2 60.0  0.5 2.0  0.5 0.067  0 8 0"

rate = (0.033, 0.2, 1.0)
lifetime = (15, 60, 120)
onco_thresh = 0.5
onco_sat = 2
migration_bias = (0.25, 0.5, 0.75)
kill_rate = 0.067
detailed_out = 0
num_threads = 32
# seed = [0,10]
for seed in range(0,10):
  for r in rate:
    for l in lifetime:
      for bias in migration_bias:
        print("cancer-immune-EMEWS ",r,l,onco_thresh,onco_sat,bias,kill_rate,detailed_out,num_threads,seed)
