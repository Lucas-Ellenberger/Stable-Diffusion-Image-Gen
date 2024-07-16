# Stable Diffusion Image Generation

This project aims to fine tune a pre-trained stable diffusion image generation model to perform better at generating instructional images. This project was for the class Applied Machine Learning: Deep Learning (CSE 144) at the University of California, Santa Cruz.

## Contributers

Lucas Ellenberger, Nia Balaji, Christopher Casarez, Thierry Nguyen

### Background and Problem

* Large amounts of texts are difficult to comprehend and causes bottlenecks in industry. This leads to wasted time and resources.
* We have massive amounts of text data at our fingertips, but making sense of it all can be difficult, so our ability to understand it is limited.
* Using images / visuals along with text helps to make content more digestible.
* This is why we need innovative solutions like our text-to-image model to unlock the potential of all that information.

### Goal

* Make learning easier
* Help everyone gain knowledge more effectively

### Approach

1. Research
2. Text Summarization
 * Summarize chapters from textbooks
3. Generating Prompts
 * Used BART CNN model
4. Dataset Preparation
 * Created custom dataset with 5k prompts
5. Fine-tuning the image generation model
 * Used the images from the custom dataset

### Methodology

#### Text Summarization

We used the open-source Hugging Face model Fine-Tuned T5 Small for Text Summarization. We believe it was much more accurate then what we could have made.

#### Summarization and Prompt Generation

We used a BART model to create summaries of large texts. We then identified key words by using a TF-IDF vectorizer. Finally, we generated prompts using key words and context from summaries.

#### Custom Dataset

We created our own dataset using Hugging Face, consisting of text prompts and corresponding images. We used Selenium and ChromeDriver to scrape Google Images.

#### Image Generation

We started with a pre-trained stable diffusion model. We chose the CompVis/stable-diffusion-v1-4 model from Hugging Face as our baseline model. We used the Parameter Efficient Fine-Tuning (PEFT) library to implement Low-Rank Adaptation (LoRA) fine tuning.

### Setbacks

Our main setback was the poor training data. After reviewing our data, we noticed some Google Image searches produced unrelated images. The worst example of this is when we used the prompt "bar chart showing the percentage of people who are using social media" and we got an image of a mermaid.

### Results

Although our models show promise in adding more detal to the explanatory images, they were not ready to help learners. The English text was illegible and many diagrams were muddled and unusable. A full analysis of every model we produced using this codebase can be found in the report.

### Limitations

#### LLM Obstacles

* Lack of prompt datasets
* Uncertainty about the adequacy of prompts
* 3-4 ML Models was too ambitious

#### Image Model Obstacles

* Lack of data
* Computational power (limited GPU usage and RAM)
* API query limits when building our custom datasets
* Limited information on this novel task

### Conclusion

We believe this project sets the stage for some exciting upgrades down the line - with better image quality, more detailed datasets, we can produce even more accurate results.

We used data analysis, machine learning, web scraping, and image processing to create a better dataset to train the stable diffusion v1 model.

Improvement by enhancing the model's practicality by developing our own tokenization and training it from scratch.

This would help generate legible text within images and produce more relevant visual content.

Thank you for reading and the full report can be found on this repository as well!
