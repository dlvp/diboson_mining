#!/bin/bash

#SBATCH --job-name=als
#SBATCH --output=log_alices_all_tight_%a.log
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=61GB
#SBATCH --time=3-00:00:00

source activate madminer
cd /scratch/jb6504/diboson_mining/cluster

python -v ./train.py scandal_all_tight_${SLURM_ARRAY_TASK_ID} scandal ${SLURM_ARRAY_TASK_ID} --mades 3 --layers 1 --alpha 0.01
