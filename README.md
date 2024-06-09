# CS224N Custom Final Project

## Description

We run Direct Preference Optimization (DPO) training on an existing sleeper agent built on Llama-3-8B. Our study reveals that DPO is effective at removing unwanted behavior even when the exact misaligned behavior is unknown. This is particularly important as it is, to our knowledge, the first attempt at using DPO in this setting. <br>

Our sleeper agent model can be found on HuggingFace at [this link](https://huggingface.co/ksw1/llama-3-8b-sleeper-agent). <br>

### Models
Each of our models use DPO to explore how effective it is at removing the misalignment within a sleeper agent. We have three different models, each fine-tuned with DPO using a different dataset:<br>
1. [DPO-1-10k](https://huggingface.co/ksw1/DPO-1-10k)
2. [DPO-1-1k](https://huggingface.co/ksw1/DPO-1-1k)
3. [DPO-2-10k](https://huggingface.co/ksw1/DPO-2-10k)
4. [DPO-2-1k](https://huggingface.co/ksw1/DPO-2-1k)
5. [DPO-3-10k](https://huggingface.co/ksw1/DPO-3-10k)
6. [DPO-3-1k](https://huggingface.co/ksw1/DPO-3-1k)<br>

Details about these models can be read in our report for CS224N, which is made available by request.<br>

## Authors

[Katherine Worden](mailto:worden@stanford.edu) <br>
[Jeong Shin](mailto:jyshin@stanford.edu) <br>

Commits are joint.

## Acknowledgments

We would like to acknowledge [Unsloth AI](https://huggingface.co/unsloth) as a starting point for our DPO fine-tuning. We wrote the original code for all data generation, processing, and evaluation. We heavily modified the Unsloth DPO notebook to process and fit our dataset and objectives appropriately. We wrote our own inference section to load, adapt, and call our model. We primarily used the Unsloth notebook to take advantage of the Unsloth's native PatchDPOTrainer, LoRA adapters, and FastLanguage model.<br>

We would also like to acknowledge the [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) repository for helping us evaluate the competency of our model after DPO fine-tuning. <br>
