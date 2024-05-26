---

inference: false
co2_eq_emissions:
      emissions: 7540
      source: MLCo2 Machine Learning Impact calculator
      geographical_location: East USA
      hardware_used: TPU v3-8
tags:
- text-to-image
license: apache-2.0

language: en
model-index: 
  - name: dalle-mini
    results: []
---

# DALL·E Mini Model Card

This model card focuses on the model associated with the DALL·E mini space on Hugging Face, available [here](https://huggingface.co/spaces/dalle-mini/dalle-mini). The app is called “dalle-mini”, but  incorporates “[DALL·E Mini](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-mini-Generate-images-from-any-text-prompt--VmlldzoyMDE4NDAy)’’ and “[DALL·E Mega](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mega-Training-Journal--VmlldzoxODMxMDI2)” models (further details on this distinction forthcoming).

The DALL·E Mega model is the largest version of DALLE Mini. For more information specific to DALL·E Mega, see the [DALL·E Mega model card](https://huggingface.co/dalle-mini/dalle-mega).

## Model Details

* **Developed by:** Boris Dayma, Suraj Patil, Pedro Cuenca, Khalid Saifullah, Tanishq Abraham, Phúc Lê, Luke, Luke Melas, Ritobrata Ghosh
* **Model type:** Transformer-based text-to-image generation model
* **Language(s):** English
* **License:** Apache 2.0
* **Model Description:** This is a model that can be used to generate images based on text prompts. As the model developers wrote in the [project report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-mini-Generate-images-from-any-text-prompt--VmlldzoyMDE4NDAy) about DALL·E mini, “OpenAI had the first impressive model for generating images with [DALL·E](https://openai.com/blog/dall-e/). DALL·E mini is an attempt at reproducing those results with an open-source model.”
* **Resources for more information:** See OpenAI’s website for more information about [DALL·E](https://openai.com/blog/dall-e/), including the [DALL·E model card](https://github.com/openai/DALL-E/blob/master/model_card.md). See the [project report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-mini-Generate-images-from-any-text-prompt--VmlldzoyMDE4NDAy) for more information from the model’s developers. To learn more about DALL·E Mega, see the DALL·E Mega [training journal](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mega-Training--VmlldzoxODMxMDI2#training-parameters).
* **Cite as:** 
```bib text
@misc{Dayma_DALL·E_Mini_2021,
      author = {Dayma, Boris and Patil, Suraj and Cuenca, Pedro and Saifullah, Khalid and Abraham, Tanishq and Lê Khắc, Phúc and Melas, Luke and Ghosh, Ritobrata},
      doi = {10.5281/zenodo.5146400},
      month = {7},
      title = {DALL·E Mini},
      url = {https://github.com/borisdayma/dalle-mini},
      year = {2021}
}
```

## Uses

### Direct Use

The model is intended to be used to generate images based on text prompts for research and personal consumption.  Intended uses include supporting creativity, creating humorous content, and providing generations for people curious about the model’s behavior.  Intended uses exclude those described in the [Misuse and Out-of-Scope Use](#misuse-malicious-use-and-out-of-scope-use) section.

### Downstream Use

The model could also be used for downstream use cases, including:
* Research efforts, such as probing and better understanding the limitations and biases of generative models to further improve the state of science
* Development of educational or creative tools
* Generation of artwork and use in design and artistic processes. 
* Other uses that are newly discovered by users. This currently includes poetry illustration (give a poem as prompt), fan art (putting a character in various other visual universes), visual puns, fairy tale illustrations (give a fantasy situation as prompt), concept mashups (applying a texture to something completely different), style transfers (portraits in the style of), … We hope you will find your own application!

Downstream uses exclude the uses described in [Misuse and Out-of-Scope Use](#misuse-malicious-use-and-out-of-scope-use).

### Misuse, Malicious Use, and Out-of-Scope Use

The model should not be used to intentionally create or disseminate images that create hostile or alienating environments for people. This includes generating images that people would foreseeably find disturbing, distressing, or offensive; or content that propagates historical or current stereotypes. 

#### Out-of-Scope Use

The model was not trained to be factual or true representations of people or events, and therefore using the model to generate such content is out-of-scope for the abilities of this model.

#### Misuse and Malicious Use 

Using the model to generate content that is cruel to individuals is a misuse of this model. This includes:
* Generating demeaning, dehumanizing, or otherwise harmful representations of people or their environments, cultures, religions, etc.
* Intentionally promoting or propagating discriminatory content or harmful stereotypes.
* Impersonating individuals without their consent.
* Sexual content without consent of the people who might see it.
* Mis- and disinformation
* Representations of egregious violence and gore
* Sharing of copyrighted or licensed material in violation of its terms of use.
* Sharing content that is an alteration of copyrighted or licensed material in violation of its terms of use.


## Limitations and Bias

### Limitations

The model developers discuss the limitations of the model further in the DALL·E Mini [technical report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mini-Explained-with-Demo--Vmlldzo4NjIxODA):
* Faces and people in general are not generated properly.
* Animals are usually unrealistic.
* It is hard to predict where the model excels or falls short…Good prompt engineering will lead to the best results.
* The model has only been trained with English descriptions and will not perform as well in other languages


### Bias 

**CONTENT WARNING: Readers should be aware this section contains content that is disturbing, offensive, and can propagate historical and current stereotypes.**

The model was trained on unfiltered data from the Internet, limited to pictures with English descriptions. Text and images from communities and cultures using other languages were not utilized. This affects all output of the model, with white and Western culture asserted as a default, and the model’s ability to generate content using non-English prompts is observably lower quality than prompts in English.

While the capabilities of image generation models are impressive, they may also reinforce or exacerbate societal biases. The extent and nature of the biases of DALL·E Mini and DALL·E Mega models have yet to be fully documented, but initial testing demonstrates that they may generate images that contain negative stereotypes against minoritized groups. Work to analyze the nature and extent of the models’ biases and limitations is ongoing.

Our current analyses demonstrate that:
* Images generated by the model can include disturbing and harmful stereotypes across protected classes; identity characteristics; and sensitive, social, and occupational groups.
* When the model generates images with people in them, it tends to output people who we perceive to be white, while people of color are underrepresented. 
* Images generated by the model can contain biased content that depicts power differentials between people of color and people who are white, with white people in positions of privilege.
* The model is generally only usable for generating images based on text in English, limiting accessibility of the model for non-English speakers and potentially contributing to the biases in images generated by the model.

The [technical report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mini-Explained-with-Demo--Vmlldzo4NjIxODA) discusses these issues in more detail, and also highlights potential sources of bias in the model development process.


### Limitations and Bias Recommendations

* Users (both direct and downstream) should be made aware of the biases and limitations.
* Content that is potentially problematic should be filtered out, e.g., via automated models that detect violence or pornography.
* Further work on this model should include methods for balanced and just representations of people and cultures, for example, by curating the training dataset to be both diverse and inclusive.


## Training

### Training Data

The model developers used 3 datasets for the model:
* ﻿[Conceptual Captions Dataset](https://aclanthology.org/P18-1238/), which contains 3 million image and caption pairs.
* ﻿[Conceptual 12M](https://arxiv.org/abs/2102.08981), which contains 12 million image and caption pairs.
* The [OpenAI subset](https://github.com/openai/CLIP/blob/main/data/yfcc100m.md) of [YFCC100M](https://multimediacommons.wordpress.com/yfcc100m-core-dataset/), which contains about 15 million images and that we further sub-sampled to 2 million images due to limitations in storage space. They used both title and description as caption and removed html tags, new lines and extra spaces.

For fine-tuning the image encoder, a subset of 2 million images were used.
All images  (about 15 million) were used for training the Seq2Seq model.

### Training Procedure

As described further in the [technical report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mini-Explained-with-Demo--Vmlldzo4NjIxODA#our-dall-e-model-architecture) for DALL·E Mini, during training, images and descriptions are both available and pass through the system as follows:
* Images are encoded through a [VQGAN](https://arxiv.org/abs/2012.09841) encoder, which turns images into a sequence of tokens.
* Descriptions are encoded through a [BART](https://arxiv.org/abs/1910.13461) encoder.
* The output of the BART encoder and encoded images are fed through the BART decoder, which is an auto-regressive model whose goal is to predict the next token.
* Loss is the [softmax cross-entropy](https://wandb.ai/sauravm/Activation-Functions/reports/Activation-Functions-Softmax--VmlldzoxNDU1Njgy#%F0%9F%93%A2-softmax-+-cross-entropy-loss-(caution:-math-alert)) between the model prediction logits and the actual image encodings from the VQGAN.

The simplified training procedure for DALL·E Mega is as follows: 

* **Hardware:** 1 pod TPU v3-256 = 32 nodes of TPU VM v3-8 (8 TPU per node) = 256 TPU v3
* **Optimizer:** Distributed Shampoo
* **Model Partition Specificiations:** 8 model parallel x 32 data parallel
* **Batch:** 44 samples per model x 32 data parallel x 3 gradient accumulation steps =  4224 increasing samples per update
* **Learning rate:** warmup to 0.0001 for 10,000 steps and then kept constant until plateau
* Gradient checkpointing used on each Encoder/Decoder layer (ie, MHA + FFN)
* Distributed Shampoo + Normformer Optimizations have proved to be effective and efficiently scaling this model. 
* It should also be noted that the learning rate and other parameters are sometimes adjusted on the fly, and batch size increased over time as well.

There is more information about the full procedure and technical material in the DALL·E Mega [training journal](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mega-Training--VmlldzoxODMxMDI2#training-parameters).


## Evaluation Results

The model developers discuss their results extensively in their [technical report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-Mini-Explained-with-Demo--Vmlldzo4NjIxODA#the-results-of-our-dall-e-experiment) for DALL·E Mini, which provides comparisons between DALL·E Mini’s results with [DALL·E-pytorch](https://github.com/lucidrains/DALLE-pytorch), OpenAI’s [DALL·E](https://openai.com/blog/dall-e/), and models consisting of a generator coupled with the [CLIP neural network model](https://openai.com/blog/clip/). 

For evaluation results related to DALL·E Mega, see this [technical report](https://wandb.ai/dalle-mini/dalle-mini/reports/DALL-E-mini-Generate-images-from-any-text-prompt--VmlldzoyMDE4NDAy).

## Environmental Impact

### DALL·E Mini Estimated Emissions

*The model is 27 times smaller than the original DALL·E and was trained on a single TPU v3-8 for only 3 days.*

Based on that information, we estimate the following CO2 emissions using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). The hardware, runtime, cloud provider, and compute region were utilized to estimate the carbon impact.

* **Hardware Type:** TPU v3-8
* **Hours used:** 72 (3 days)
* **Cloud Provider:** GCP (as mentioned in the technical report)
* **Compute Region:** us-east1 (provided by model developers)
* **Carbon Emitted (Power consumption x Time x Carbon produced based on location of power grid):** 30.16 kg CO2 eq.

### DALL·E Mega Estimated Emissions

DALL·E Mega is still training. So far, as on June 9, 2022, the model developers report that DALL·E Mega has been training for about 40-45 days on a TPU v3-256. Using those numbers, we estimate the following CO2 emissions using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). The hardware, runtime, cloud provider, and compute region were utilized to estimate the carbon impact.

* **Hardware Type:** TPU v3-256
* **Hours used:** 960 - 1080 hours (40-45 days)
* **Cloud Provider:** Unknown
* **Compute Region:** Unknown
* **Carbon Emitted (Power consumption x Time x Carbon produced based on location of power grid):** Unknown

## Citation

```bibtext
@misc{Dayma_DALL·E_Mini_2021,
      author = {Dayma, Boris and Patil, Suraj and Cuenca, Pedro and Saifullah, Khalid and Abraham, Tanishq and Lê Khắc, Phúc and Melas, Luke and Ghosh, Ritobrata},
      doi = {10.5281/zenodo.5146400},
      month = {7},
      title = {DALL·E Mini},
      url = {https://github.com/borisdayma/dalle-mini},
      year = {2021}
}
```

*This model card was written by: Boris Dayma, Margaret Mitchell, Ezi Ozoani, Marissa Gerchick, Irene Solaiman, Clémentine Fourrier, Sasha Luccioni, Emily Witko, Nazneen Rajani, and Julian Herrera.*
