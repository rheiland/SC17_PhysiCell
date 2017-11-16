# SC17_PhysiCell

A few scripts, images, input/output files, etc, related to https://doi.org/10.1101/196709 for http://www.scworkshops.net/cancer2017/.

The Anaconda Python 3 distribution (https://www.anaconda.com/download) was used to run the scripts that used numpy and/or matplotlib. The "pvpython" that was installed with the ParaView binary installation also (mostly) works. The version at the time of this repo's use (`$ pvpython --version` --> paraview version 5.4.1) seemed to be an earlier version of matplotlib than that in Anaconda's and apparently lacked one particular predefined colormap that was used in the "heatmap*" scripts. There may be other hiccups as well.

```
# parameter sweep with 9 params (where we vary 1,2,5) 
 cancer-immune-EMEWS [attachment_rate] [attachment_lifetime] 
                     [oncoprotein_detection_threshold] [oncoprotein_saturation] 
                     [migration_bias] [kill_rate] 
                     [detailed_output (0 or 1)] [omp_num_threads] [random seed value] 
  
 Attachment_rate = [0.033, 0.2, 1] - mean wait time, hours 
 Attachment_lifetime = [15, 60, 120] - mins 
 Migration_bias = [0.25, 0.5, 0.75] - random migration bias towards chemotactic gradients 
 ```
The `params_map_final.txt` file is the Rosetta Stone for mapping simulation runs to parameters used for those runs. Unfortunately, Argonne (ANL), who ran the simulations, had some runs that failed, so those are marked "missing" in `params_map_final.txt`, i.e., we didn't have data for those runs/parameters. But as we learned at the last minute, there were  a few other runs (not marked as "missing") that also failed to run. When creating animations of the .svg outputs (the Z=0 slices) corresponding to the corner cases of the heatmap parameter images, we had to sometimes mix runs using different random seed parameters, but that fulfilled the other parameters for those corner cases. Confusing? Yeah.
