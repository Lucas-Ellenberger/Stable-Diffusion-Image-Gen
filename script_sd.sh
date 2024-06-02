export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export OUTPUT_DIR="CSE144/lora/large-test/"
export HUB_MODEL_ID="CSE144-large-lora-test"
export DATASET_NAME="CSE144/Chemistry-Images-For-Lora"

accelerate launch --mixed_precision="fp16"  train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$DATASET_NAME \
  --dataloader_num_workers=8 \
  --resolution=512 --center_crop \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --mixed_precision="fp16" \
  --max_train_steps=60 \
  --learning_rate=1e-04 \
  --max_grad_norm=1 \
  --lr_scheduler="cosine" --lr_warmup_steps=0 \
  --output_dir=${OUTPUT_DIR} \
  --push_to_hub \
  --hub_model_id=${HUB_MODEL_ID} \
  --report_to=wandb \
  --checkpointing_steps=20 \
  --validation_prompt="small beaker with purple liquid" \
  --seed=1337

