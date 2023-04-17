#!/usr/bin/python
import glob
import sys
number_of_parallel_jobs_to_run=int(sys.argv[1])
path = "Exercise_2"
dir_list = glob.glob(path + '/*_F_filt.fastq')
counter=0
for x in dir_list:
	spl = x.split("/")
	spl = spl[1].split("_F_filt.fastq")
	dir_list[counter]=spl[0]
	counter = counter + 1
counter=0
size_of_dir=len(dir_list)
number_of_slurm_jobs=float(size_of_dir)/number_of_parallel_jobs_to_run
number_of_slurm_jobs = int(number_of_slurm_jobs) + 1
for i in range(number_of_slurm_jobs):
	slurm_file = open("Exercise_2_slurm/" + str(i) + ".slurm","w")
	tasks_file = open("Exercise_2_tasks/" + str(i) + ".tasks","w")
	slurm_file.write("#!/bin/bash\n")
	slurm_file.write("#SBATCH --job-name=" + str(i) + "\n")
	slurm_file.write("#SBATCH --partition=savio3_htc\n")
	slurm_file.write("#SBATCH --account=fc_popgen\n")
	slurm_file.write("#SBATCH --nodes=1\n")
	slurm_file.write("#SBATCH --cpus-per-task=1\n")
	slurm_file.write("#SBATCH --ntasks-per-node=" + str(number_of_parallel_jobs_to_run) + "\n")
	slurm_file.write("#SBATCH --time=72:00:00\n")
	slurm_file.write("#SBATCH --mail-type=START,END,FAIL\n")
	slurm_file.write("#SBATCH --mail-user=lpipes@berkeley.edu\n")
	slurm_file.write("cd /global/scratch/users/lpipes/unix_workshop\n")
	slurm_file.write("module load gcc openmpi\n")
	slurm_file.write("module load bowtie2\n")
	slurm_file.write("ht_helper.sh -t /global/scratch/users/lpipes/unix_workshop/Exercise_2_tasks/run_" + str(i) + ".tasks\n")
	slurm_file.close()
	for j in range(number_of_parallel_jobs_to_run):
		if ( counter == size_of_dir ):
			break
		tasks_file.write("bowtie2 -x Exercise_2_bowtie_db/MT738585.1.fasta -1 Exercise_2/" + dir_list[counter] + "_F_filt.fastq -2 Exercise_2/" + dir_list[counter] + "_R_filt.fastq -S Exercise_2/" + dir_list[counter] + ".sam\n")
		counter = counter + 1
	tasks_file.close()
