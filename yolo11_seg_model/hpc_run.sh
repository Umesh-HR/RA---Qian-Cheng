#!/bin/bash
#SBATCH --job-name=trraficc             # Job name
#SBATCH -p gpu
#SBATCH --gres=gpu:v100-sxm2:1
#SBATCH --nodes=1                    # Number of nodes
#SBATCH --cpus-per-task=10           # Number of CPUs per task
#SBATCH --mem=20G                    # Total CPU memory (not GPU memory)
#SBATCH --time=07:55:00              # Time limit hh:mm:ss
#SBATCH --output=output_%j.txt       # Standard output and error log
#SBATCH --error=error_%j.txt         # Standard error log

# Load any required modules
module load cuda/11.0
conda activate yolov11


# Training
python /work/NASASPaceResearch/seaqueue/yolo/yolo11_seg_train.py

# Predicting
# python /work/NASASPaceResearch/seaqueue/yolo/yolo11_seg_predict.py
