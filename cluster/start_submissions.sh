#!/bin/bash

cd /scratch/jb6504/diboson_mining/scripts

sbatch --array=0-0 submit_alices_all_tight.sh
sbatch --array=0-0 submit_alices_phi_tight.sh
# sbatch --array=0-9 submit_alices_all_loose.sh
# sbatch --array=0-0 submit_scandal_all_tight.sh
# sbatch --array=0-9 submit_scandal_all_phi.sh
# sbatch --array=0-9 submit_scandal_all_loose.sh
