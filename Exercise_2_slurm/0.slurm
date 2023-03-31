#!/bin/bash
#SBATCH --job-name=0
#SBATCH --partition=savio2_htc
#SBATCH --account=fc_popgen
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=72:00:00
cd /global/scratch/users/lpipes/unix_workshop
module load gcc openmpi
module load bowtie2
ht_helper.sh -t /global/scratch/users/lpipes/unix_workshop/run_0.tasks
