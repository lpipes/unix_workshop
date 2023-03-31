#!/Users/lpipes/anaconda2/bin/python
import glob
path = "Exercise_2"
dir_list = glob.glob(path + '/*_F_filt.fastq.gz')
counter=0
for x in dir_list:
	spl = x.split("/")
	spl = spl[1].split("_F_filt.fastq.gz")
	dir_list[counter]=spl[0]
	counter = counter + 1
print(dir_list)
counter=0
for i in range(1):
	slurm_file = open("Exercise_2_slurm/" + str(i) + ".slurm","w")
	tasks_file = open("Exercise_2_tasks/" + str(i) + ".tasks","w")
	slurm_file.write("#!/bin/bash\n")
	slurm_file.write("#SBATCH --job-name=" + str(i) + "\n")
	slurm_file.write("#SBATCH --partition=savio2_htc\n")
	slurm_file.write("#SBATCH --account=fc_popgen\n")
	slurm_file.write("#SBATCH --nodes=1\n")
	slurm_file.write("#SBATCH --cpus-per-task=1\n")
	slurm_file.write("#SBATCH --ntasks-per-node=1\n")
	slurm_file.write("#SBATCH --time=72:00:00\n")
	slurm_file.write("cd /global/scratch/users/lpipes/unix_workshop\n")
	slurm_file.write("module load gcc openmpi\n")
	slurm_file.write("module load bowtie2\n")
	slurm_file.write("ht_helper.sh -t /global/scratch/users/lpipes/unix_workshop/run_" + str(i) + ".tasks\n")
	slurm_file.close()
	for j in range(25):
		tasks_file.write("bowtie2 " + dir_list[counter] + "\n")
		counter = counter + 1
	tasks_file.close()
