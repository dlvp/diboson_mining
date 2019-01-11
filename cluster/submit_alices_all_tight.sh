#!/bin/bash

#SBATCH --job-name=als
#SBATCH --output=log_alices_all_tight_%a.log
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=61GB
#SBATCH --time=3-00:00:00

source activate madminer
cd /scratch/jb6504/diboson_mining/scripts

python -u ./train.py alices_all_tight_${SLURM_ARRAY_TASK_ID} alices ${SLURM_ARRAY_TASK_ID} --alpha 0.0001
