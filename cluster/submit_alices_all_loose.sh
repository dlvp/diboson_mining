#!/bin/bash

#SBATCH --job-name=als-loose
#SBATCH --output=log_alices_all_loose_%a.log
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=61GB
#SBATCH --time=3-00:00:00

source activate higgs_inference
cd /scratch/jb6504/diboson_mining/cluster

python -v ./train.py alices_all_loose_${SLURM_ARRAY_TASK_ID} alices ${SLURM_ARRAY_TASK_ID} --alpha 0.0001 --loose
