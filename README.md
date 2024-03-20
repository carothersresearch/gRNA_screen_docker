
# gRNA_screen
gRNA screening code and jupyter notebooks developed by the Carothers Lab.

## Installation:
 - Easiest way to run this is through Docker + GitHub Codespace:
	- From the main repo page, one can launch a Codespace that automatically runs the dockerfile and sets up the environment
- Alternatively, one can install Docker locally, clone the repo, and run the dockerfile 

## Usage:
 - Once inside the Docker container:
 	- Open a terminal and run `jupyter notebook --allow-root` to start a jupyter server. Copy the resulting URL.
  	- If using Codespaces or Vs Code: in the Wayfinder_Algorithm_for_gRNA_Evaluation_DSY.ipynb jupyter notebok, select the new kernel:
   		-  Select another kernel > existing jupyter server > enter the URL of a running jupyter server > paste copied URL  
     	-  The notebook should be able to run at this point
 - Make sure to add your sequences or gRNA csv files in the corresponding directories (formatting is important, see provided example files)
 - In the notebooks, make sure the file name variables point to your specific files

## gRNA selection guidelines
- In the first 300bp after start codon
- Better be closed to the promoter (Vigouroux-2020, Cui-2018, Wang-2018)
- Check this recent Calvo-Villamanan-2020 paper
- %GC? and seeding sequence?
	- 40-80% GC content?
	- AGGAA, TGACT, ACCCA, AAAGG, GAGGC, CGGAA, ATATG, AACTA, TGGAA, CACTC are 10 suggested seed sequences which attribute to toxic effect in E. coli
- Beware of the exact TSS --- Start with A or G rather than T or C
- Off-target binding? --- to essential gene up to 11bp with mismatch?
- WAYFINDER
	- **Choosing 2 good gRNAs with --- New Net Energy (+Bind Barrier)**
	- **Bind Barrier first and then New Net Energy**
	- **Bind barrier should be less than 10 and New Net Energy should be less than -30 (more negative) or as low as possible**
