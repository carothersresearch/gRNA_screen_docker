
# gRNA_screen
gRNA screening code and jupyter notebooks developed by the Carothers Lab. We make this software available under a CC BY-NC-ND license.

## Installation:
 - Easiest (and quickest: only a few minutes of setup) way to run this is through Docker + GitHub Codespace:
	- From the main repo page, one can launch a Codespace that automatically runs the dockerfile and sets up the environment
	- We have verified functionality in Codespaces run on Firefox v123.0.1 and Chrome v122.0.6261.112 in MacOSv13.6.1 and Chrome v121.0.6167.185 in Windows 10.
- Alternatively, one can install Docker locally, clone the repo, and run the dockerfile. In this case, refer to Docker for system requirements.

## Usage:
 - Once inside the Docker container:
 	- Open a terminal and run `jupyter notebook --allow-root` to start a jupyter server. Copy the resulting URL.
  	- If using Codespaces or Vs Code: in the Wayfinder_Algorithm_for_gRNA_Evaluation_DSY.ipynb jupyter notebook, select the new kernel:
   		- Select another kernel > existing jupyter server > enter the URL of a running jupyter server > paste copied URL
       		- A new Codespace might prompt you to install git or python + jupyter extensions: do this if prompted
     	- The notebook should be able to run at this point
 - Make sure to add your entire gRNA sequences into the input csv file(s) in the corresponding directories
 	- Formatting is important: see provided example files (one of which reproduces the scRNAs used in the paper cited below)
    	- You can edit the input files directly in the Codespace, or download an example file and edit it locally
       		- Local files can be dragged into the Explorer in the Codespace
 - In the notebook, make sure the file name variable (cell 3) points to your specific file
 - Expected runtime of analysis is less than 5 minutes for input files containing up to about 100 gRNAs (~30s for the example files)

## Screening gRNAs:
- **Two of the output parameters are most important: Folding Barrier (column B) and then Net Binding Energy (column E)**
- See Fontana, Sparkman-Yager, Faulkner _et al._ 2024 for explanations of many of these parameters, including correlation to CRISPRa expression
- **Primary screening: Folding Barrier should be less than 10 kcal/mol to avoid defective gRNAs**
- **Secondary screening: Net Binding Energy should generally be as low (more negative) as possible, e.g. -30 kcal/mol is a good target**
