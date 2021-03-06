#!/bin/bash
#SBATCH --job-name uda_pred_test
#SBATCH -n 4 # Number of cores
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -D /home/grupo07/M5/yolov3 # working directory
#SBATCH --partition mhigh,mlow
#SBATCH --mem 20000 # 16GB solicitados.
#SBATCH --gres gpu:1 # Para pedir Pascales MAX 8
#SBATCH -o /home/grupo07/logs/detection/%x_%u_%j.out # File to which STDOUT will be written
#SBATCH -e /home/grupo07/logs/detection/%x_%u_%j.err # File to which STDERR will be written
#SBATCH -q masterlow
sleep 5
/usr/local/cuda-9.2/samples/bin/x86_64/linux/release/deviceQuery
nvidia-smi
cd ~/M5/yolov3
python3 test.py --cfg cfg/udacity.cfg --data-cfg data/udacity_data/udacity_predict_test.data --weights weights/udacity/latest.pt --dataset_name udacity_predict_test --save-json
