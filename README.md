# cahoots-project
**Shifting Response: Analyzing Trends of CAHOOTS in Diverting Police Calls**

The project aims to determine the proportion of emergency calls diverted from police to CAHOOTS and analyze how this proportion has changed over time. The primary objective is to evaluate the effectiveness of CAHOOTS by analyzing the changes in emergency call diversions from police to CAHOOTS.

**Installation**
To run the analysis scripts, ensure you have Python installed on your system. Additionally, install the required Python packages using the following command:

  ``pip install pandas seaborn matplotlib scipy``
  
**Usage**

Clone the repository to your local machine.
Ensure that the necessary CSV files containing call data are placed in the appropriate directories.
Run the Python scripts provided in the repository.

**Analytical Steps**

Cleaning CAD Data: The clean_cad_data() function reads and cleans the call data from the Computer Aided Dispatch (CAD) system. It drops rows with missing nature codes and irrelevant columns, and adds a binary column indicating if the call involved CAHOOTS.
Proportion Analysis: The cleaned CAD data is analyzed to determine the proportion of calls diverted to CAHOOTS over time. Chi-square test is performed to assess statistical significance.
Visualization: The analysis results are visualized using seaborn and matplotlib to generate bar plots showing the proportion of calls diverted to CAHOOTS over different weeks.

Feel free to explore the provided scripts to understand the analysis process and insights gained from the call data related to CAHOOTS service. For any inquiries or suggestions, please contact: Emerson Sullivan, emersons@uoregon.edu
