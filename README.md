# Unveiling Discrepancies in Android App Data Safety Declarations and Privacy Policies: An In-depth Analysis using Large Language Models

by
Nghiem Pham Thanh;
Bang Ngo Hai;
Hung Nguyen Nhat;
Xuan Son Ha;
Nghia Duong-Trung;
Tuan Le Thanh;

Official code implementation for ICDE 24 paper Unveiling Discrepancies in Android App Data Safety Declarations and Privacy Policies: An In-depth Analysis using Large Language Models.

> This paper identifies critical discrepancies in data safety declarations and privacy policies among 450 Android apps, raising concerns about user trust and legal implications. The study explores the potential of advanced techniques, like fine-tuning large language models, to monitor and verify app behaviors against their stated commitments. To promote transparency, the research provides a benchmark dataset and a list of examined Android apps, contributing to a more trustworthy app ecosystem.

![](figure)

*Caption for the example figure with the main results.*


## Abstract

This paper delves into the critical discrepancies observed between data safety declarations and privacy policies across 450 Android applications, bringing to light the issues of incompleteness, incorrectness, and inconsistency. 
Such misalignments undermine user trust and pose severe ethical and legal challenges. 
Our research is a pioneering effort in this domain, posing crucial questions about the potential of technology to rectify these disparities. 
We postulate whether advanced techniques, precisely fine-tuning large language models (LLMs), could be leveraged to monitor and verify app behaviors against their declared commitments, ensuring unity and fortifying trust. 
In our investigation, we comprehensively assess the flexibility and capability of LLMs across multiple training scenarios, establishing ten evaluation cases within four distinct strategies, including Zero-Shot, Manual Label Fine-Tuning, and LLM-generated label fine-tuning. 
As a commitment to transparency and furthering research in this domain, we release a benchmark dataset and maintain a curated list of the examined Android applications. 
Our findings contribute significantly to understanding the alignment of privacy policies and data safety declarations, setting the stage for future informed, transparent, and trustworthy app ecosystems.


## Software implementation

> Briefly describe the software that was written to produce the results of this
> paper.

All source code used to generate the results and figures in the paper are in
the `code` folder.
The calculations and figure generation are all run inside
[Jupyter notebooks](http://jupyter.org/).
The data used in this study is provided in `data` and the sources for the
manuscript text and figures are in `manuscript`.
Results generated by the code are saved in `results`.
See the `README.md` files in each directory for a full description.


## Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/nghiempt/dspp.git

or [download a zip archive](https://github.com/nghiempt/dspp/archive/refs/heads/main.zip).

A copy of the repository is also archived at *insert DOI here*


## Approach

We have somes way to collect data from browers. After, pre-proccessing data. This file below:

    approach/make_dataset/make_final_dataset_only_prompt.py
    approach/make_dataset/make_resource_dataset.py

## Evaluation

We have 10 cases. We use LLM models to generate result:

    evaluation/case_03/code/generate_completion_by_gpt3.0.py

As same as for cases 4,5,6,7,8,9,10


We convert chat json format to message json format in:

    helpers/convert_message_for_3.5.py

After that, we continue to convert to JSONL in:

    helpers/convert_json_to_jsonl.py

Follow for this step to fine tuning GPT 3.5 turbo:

1. Upload files
    curl https://api.openai.com/v1/files \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -F "purpose=fine-tune" \
        -F "file=@path_to_your_file"

2. Create a fine-tuning job
    curl https://api.openai.com/v1/fine_tuning/jobs \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -d '{
        "training_file": "TRAINING_FILE_ID",
        "model": "gpt-3.5-turbo-0613"
        }'

We can use terminal to follow fine tuning process:

    pip install --upgrade openai

    export OPENAI_API_KEY="<OPENAI_API_KEY>"

    openai api fine_tuning.job.follow -i <YOUR_FINE_TUNE_JOB_ID>

or

    openai api fine_tuning.job.get -i <YOUR_FINE_TUNE_JOB_ID>

You can check status for this proccess: validating-file -> running -> succeed

Finally, we use the model after fine tuned to predict result:

    case_03/code/predict_by_ft_gtp3.5.py


## Dataset detail
| id            | appN           | pkgN | iCr          | iCm         | iCs         |
| ------------- | -------------  | ------------ | ------------ | -----------  |-----------  |
| 1             | Once: Perfect Match Dating App | com.udates | 1 | 0 | 0 |
| 2             | Photo Collage Maker Editor | cornera.touchretouch | 0 | 1 | 0 |
| 3             | Pict2Cam | com.adriangl.pict2cam | 1 | 0 | 0 |
| 4             | Blend Photo Editor – Effects | com.multiphotoblender.photomixer | 1 | 0 | 0 |
| 5             | Wild Animal Photo Frames | com.appbites.wildanimalphotoframes | 1 | 0 | 0 |
| 6             | Baby Photo Nice Baby wallpaper | com.cuteBaby.BabyPhotos | 1 | 0 | 0 |
| 7             | Mobile Phone Photo Frames | freeappshouse.mobile.phone.photo.frames.editor | 1 | 0 | 0 |
| 8             | CSL – Meet, Chat, Pla‪y & Date | com.jaumo.casual | 1 | 0 | 0 |
| 9             | Body Plastic Surgery | com.ster.photo.surgery | 1 | 0 | 0 |
| 10            | Family Photo Frame | com.Family.Photoframee | 1 | 0 | 0 |

Full dataset can be found in the file `final_results/450_apps.csv`

|Category|Number of apps|
|---|---|
| Photography| 347 apps|
| Dating| 101 apps|
| PhotographyPlay Pass| 1 apps|
| Social| 1 apps|

| Number of downloads |Number of apps|
|---|---|
|100+ to 5k+| 27 apps|
|10K+ to 500K+| 295 apps|
|1M+ to 50M+| 118 apps|
|100M+ to 500M+| 10 apps|
