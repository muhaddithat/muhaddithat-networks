# muhaddithat-networks

This is a semester-long project by Ayah Aboelela and Remy LeWinter for a graduate class on digital humanities. This project aims to highlight teacher-student (or narrator-receiver) networks between muhaddithat (female scholars and transmitters of hadith) within the first 4 centuries of Islamic history. Data for this is sourced from the <a href="https://www.kaggle.com/fahd09/hadith-narrators" title="A2"> Hadith Narrators Dataset on Kaggle </a>.

## Running the app

Before running the app, we strongly recommend reading the <a href="https://github.com/muhaddithat/muhaddithat-networks/blob/main/userguide.pdf" title="A2"> User Guide </a> for details on the relevant historical context, glossary of Arabic terms, user instructions, references and work cited, and other necessary background information for understanding and using the app. 

### Required packages:

Running the scripts for this project requires a Python environment with the following packages installed:

- python=3.8.8
- jupyter
- dash
- jupyter_dash
- dash_cytoscape
- plotly
- pandas
- networkx
- json
- python-graphviz

### How to run the app:

After downloading the repository, open the app.ipynb JupyterNotebook and run all cells. You should be directed to this link: http://127.0.0.1:8050/. Open this in your preferred web browser and the app should be displayed. Refer to the <a href="https://github.com/muhaddithat/muhaddithat-networks/blob/main/userguide.pdf" title="A2"> User Guide </a> if you need navigation instructions. 

## Potential future improvements

Since this was only a semester-long project, we didn't have time to explore all possibile options for integrating in our app. Here is a list of things we might consider for the future:
- Including more muhaddithat, or women narrators, in the app. This would entail writing bios about them, selected hadiths they narrated, and generating and displaying their graphs.
- Adding more layouts and features that would be unique to individual subgraphs
- Making use of all the collected metadata on hadiths and bios. Currently, our hadith.json and bios.json files have extra metadata associated with each biography and hadith (including the hadith's narration chains, the narrators' places of stay, and others). This information is not integrated with the app currently, but can be done in the future.
- Deploying the app so that it is hosted on the web instead of requiring any downloads or installations
