# Best practices in coding - Study case : Nutrition analysis of the Open Food Facts data
## Project purpose
This project aims to identify the main patterns across selected features by using PCA and analyze nutritional aspects of the Open Food Facts data while showing the best way of coding.
This project aims to be : 
- Readable
- Reproducible
- Optimised by using modularity
- Clear about errors
- Aligned with ethical principles

Data source : [Open Food Facts](https://fr.openfoodfacts.org/)

## Installation with 'Lab2venv'
To install the project environment :
1. Clone the repository and open the complete folder in VS Code.
2. Recreate and activate `Lab2venv`.
3. Install `requirements.txt` and select `Lab2venv` as the notebook kernel.

## Folder organization
The folder is organized in sub-folders as follow :
- **Config** : Contains the file config.yaml keeps track of all variables useful for the functions and classes. They are configured at the beginning of the project and can be adapted to different projects.
- **Data** : Contains the data files .csv
- **Notebooks** : Contains all Jupyter Notebooks
- **SRC** : Regroups all functions and classes used in notebooks

In the root project can be found the following files :
- .gitignore : Prevents certain files from being tracked by Git
- requirements.txt : All the modules needed to be installed in the recreated environment.

## Notebook execution
What you need to know for the Notebook execution : 
1. The notebook is to be find in : `Notebooks/Lab2_Best_Practices_Student.ipynb`
2. Choose `Lab2venv`as kernel
3. Run all cells from top to bottom
4. The data path and parameters are loaded from the `config.yaml` file.
5. The notebook will import the functions and classes contained in the `SRC` folder and will return a PCA analysis with variance explained bar chart. Another nutrient analysis will be run and will display a summary of sugar and proteins in food

## Contributors
Chloé RUIZ\
(No partner to do it with)\
![Logo](logo.png)\
[ENTPE](https://entpe.fr)