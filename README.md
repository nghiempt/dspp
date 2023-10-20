# Evaluating the Consistency Between Data Safety and Privacy Policies using Natural Language Processing

by
Nghiem P. T.;
Bang N. H.;
Hung N. N.;
Son X. H.;
Nghia T. D.;
Tuan L. T.;

This paper has been submitted for publication in *Some Journal*.

> Brief description of what this paper is about (2-3 sentences). Include a
> figure as well with the main result of your paper.

![](figure)

*Caption for the example figure with the main results.*


## Abstract

> Paste here the abstract.


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


## Dependencies

You'll need a working Python environment to run the code.
The recommended way to set up your environment is through the
`virtualenv Python` which
provides the `conda` package manager.
Virtualenv can be installed in your user directory and does not interfere with
the system Python installation.

We use `venv` virtual environments to manage the project dependencies in
isolation.
Thus, you can install our dependencies without causing conflicts with your
setup (even with different Python versions).

Run the following command in the repository folder (where `environment.yml`
is located) to create a separate environment and install all required
dependencies in it:

    virtualenv venv

## Reproducing the results

Before running any code you must activate the conda environment:

    source activate ENVIRONMENT_NAME

or, if you're on Windows:

    activate ENVIRONMENT_NAME

This will enable the environment for your current terminal session.
Any subsequent commands will use software that is installed in the environment.

To build and test the software, produce all results and figures, and compile
the manuscript PDF, run this in the top level of the repository:

    make all

If all goes well, the manuscript PDF will be placed in `manuscript/output`.

You can also run individual steps in the process using the `Makefile`s from the
`code` and `manuscript` folders. See the respective `README.md` files for
instructions.

Another way of exploring the code results is to execute the Jupyter notebooks
individually.
To do this, you must first start the notebook server by going into the
repository top level and running:

    jupyter notebook

This will start the server and open your default web browser to the Jupyter
interface. In the page, go into the `code/notebooks` folder and select the
notebook that you wish to view/run.

The notebook is divided into cells (some have text while other have code).
Each cell can be executed using `Shift + Enter`.
Executing text cells does nothing and executing code cells runs the code
and produces it's output.
To execute the whole notebook, run all cells in order.


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


Full dataset can be found in the file `result/final_dataset.csv`

## License

