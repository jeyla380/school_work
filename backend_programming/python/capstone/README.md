# Book Title Translation Project

<br>

## Project Proposal Plan

### 1. Summary of Problem
The Simple Bookstore is expanding their store globally starting in Paris, France and Tokyo, Japan, in addition to the multiple locations in the United States. They are wanting to update their list of popular books with various translations within all their stores and need to know what books to purchase (if they exist).

### 2. Description of Product Benefits
The Simple Bookstore is looking for a book title translator application that has the ability to translate various titles of books in English, French, or Japanese into each of the languages so they can purchase the translated titles and carry the books in all their locations in the United States, Paris (France), and Tokyo (Japan).

### 3. Description of Data Used
1. Model Training Data
   1. 50,000 sentences in French that are translated from English using Python’s deep translator API.
   2. 50,000 sentences in English (which is the direct Japanese translations) scraped from Tangorin Japanese Dictionary & Translation.
   3. 50,000 sentences in Japanese are scraped from Tangorin Japanese Dictionary & Translation.
2. Book Titles Data
   1. Top 50 popular book titles in each language: English, French, and Japanese.
   2. Includes the publication dates, the author, and language the book was originally written in for each book. *

<span style="font-size:10pt">*All the information will be translated into English.</span>

### 4. Objectives and Hypotheses
**Objectives:**
-	Develop a language translation model that is able to translate book titles between English, French, and Japanese.
-	Enable users to discover and purchase books in various languages based on title searches.

**Hypotheses:**
-	The translation model’s accuracy will improve with larger and more diverse datasets.
-	Longer titles may be more challenging to translate in maintaining fluency and accuracy.
-	Book titles with cultural references and/or localized context may be difficult to translate accurately.

### 5. Outline of Project Methodology
1. Define the needs and requirements of the stakeholders.
2. Gather and scrape sentences for English, French, and Japanese.
3. Develop and train language translation models in order to translate and properly implement them.
4. Integrate the language translation model into a simple graphical user interface (GUI) for users to use.
5. Gather feedback from users to determine whether necessary changes are needed for the models.

### 6.	Projected Timeline of Project*
| Deliverable | Duration | Project Start Date | Anticipated End Date |
| :--: | :--: | :--: | :--: |
| Data Collection | 6 Days | July 1, 2024 | July 8, 2024 |
| Data Cleaning | 2 Days | July 9, 2024 | July 11, 2024 |
| Data Tokenization | 2 Days | July 12, 2024 | July 16, 2024 |
| Book Information | 8 Days | July 17, 2024 | July 29, 2024 |
| Model Training | 15 Days | July 30, 2024 | August 20, 2024 |
| User Interface | 3 Days | August 21, 2024 | August 26, 2024 |
| Model Evaluation | 2 Days | August 27, 2024 | August 29, 2024 |
| Data Analysis | 5 Days | August 30, 2024 | September 6, 2024 |

<span style="font-size:10pt">*This projected timeline is based on typical business days which exclude Saturdays and Sundays</span>


### 7.	Outline of Project
1. Data Collection
   1. Web scrape data for English, French, and Japanese.
2. Data Cleaning
   1. Tidy data so no special characters, missing data, etc., are included.
3. Data Tokenization
   1. Tokenize each language separately by words.
      1. Remove all punctuation from all languages with the exception of apostrophes and hyphens in English and French (i.e. “I’ll”, “est-ce”, “well-known”, etc.)
      2. Add special tokens to the words to make training the model easier.
   2. Map tokenized data to numbers (indices).
4. Book Information - Data Entry
   1. Find the top 50 books in each language and input them into a database.
      1. Each book should contain the title, author, language it was written in, and publishing date.
5. Model Training
   1. Convert tokenized data into tensors.
   2. Split the tensor data into train, valid, and test sets.
   3. Create a Seq2Seq model that will translate the source language to the target language.
      1. Create Encoder, Attention Layer, and Decoder for the model.
      2. Initialize model weight.
      3. Define loss function and optimizer for models.
   4. Train the language models (i.e. English to French, English to Japanese, French to Japanese, French to English, Japanese to English, and Japanese to French).
      1. Create training and evaluation function for models.
      2. Incorporate K-Fold cross validation to reduce model overfitting.
   5. Save the models and any relevant information.
   6. Test translation from source to target language to ensure models work.
6. User Interface
   1. Allow users* to input book title.
   2. Translate it into English, French, and Japanese and display all 3 languages.
7. Quality Assurance and Evaluation
   1. Evaluate the book title translation model using Bilingual Evaluation Understudy (BLEU).
8. Data Analysis
   1. Analyze the differences between languages by using descriptive and predictive methods.
      1. Descriptive:
         1. Visualize the differences of train loss and valid loss through each fold and epoch for each model.
         2. Compare and analyze the differences of each translation for each evaluation metric using a scatterplot.
         3. Create a confusion matrix of the model’s translation compared to a more accurate translation.
      2. Predictive:
         1. If a user is looking for a title in English, the model recommends its Japanese and French translations as well.
         2. Train language models using machine learning libraries like PyTorch.

<span style="font-size:10pt">* ”Users” in the project are not customers, but rather employees that work for Simple Bookstore.</span>


### 8. Resources and Costs

The only cost associated with the book title translation models, as of right now, are related to procedures, documentation, and testing. 

**Procedures, Documentation, and Training:**
- Time and cost need to be considered for creating and training custom language models.
- Allocate cost and time for testing and debugging, as well as costs for regular maintenance and ongoing updates.
- Create user guides and training materials for Simple Bookstore’s employees, so costs and time will need to be determined.

However, there are additional factors that needs to be considered as Simple Bookstore continuously expands.

**Infrastructure:**
- Implement the book title translation model within Simple Bookstore’s website and mobile application to allow customers to search for book titles.
- Over time, the database that contains all book information will need to be expanded, so a larger database will need to be implemented.
- Associated costs:
   - Microsoft Azure – Starts at around $177 per month based on our current needs.
   - Snowflake – Starts at $23 per TB per month.

**Translation Services:**
- Book titles that are longer or contain localized context may require translation services if the translation model metrics fail.
- Translated book titles that don’t have enough language data to train may require translation services.
- Associated costs: 
   - DeepL – Free
   - Amazon Translate – Starts at $15 per million characters.
   - SunTec AI – Prices vary depending on the amount of data that needs to be evaluated.

### 9. Ethical and Legal Considerations
- Ensure book title translations are still able to preserve original context and intent.
- Remain unbiased when translating book titles that contain controversial or politically charged content.

<br>

## Post-Implementation Report

### 1. User Guide
If you have not installed any of the following applications or libraries, please follow each section. Any applications you have installed you can skip, and any libraries you’ve installed will just be updated if you re-run the code.

**Anaconda:**
- The download option is meant for Windows only. If you would like, you can download Anaconda on Mac or Linux, however, this program would be better to be run on Windows. 

**PyTorch:**
- The installation for PyTorch can be found here: https://pytorch.org/get-started/locally/
   - Make sure Python is updated to 3.8 or later before installing.
- To verify PyTorch has been installed, select “Environment” within the Anaconda Navigator, then type “pytorch” in the search bar. Look for “pytorch”, if it’s there, it’s been installed. 

**CUDA & cuDNN:**
- After installing PyTorch, CUDA and cuDNN (a CUDA library) will need to be installed as well. You can install/update both using these commands in Anaconda’s CMD.exe Prompt as well:
   - `conda install -c anaconda cudatoolkit`
   - `conda install -c anaconda cudnn`
- To verify CUDA has been installed, type “cuda-version” in the search bar. If it appears, it means it has been installed. It should be the exact same version as “pytorch-cuda” (you’ll need to type this in the search bar to check). Make sure those match or there may be issues.
- To verify cuDNN has been installed, do the same thing by typing “cudnn”. If it’s there, it’s been installed correctly.
- If there are any issues with installing either CUDA and/or cuDNN, follow this installation guide: https://medium.com/@afierror14/how-to-install-cuda-11-8-cudnn-9-1-pytorch-on-windows-anaconda-bf6af1a16aa6. This will go through downloading CUDA and cuDNN through NVIDIA’s website.

**Additional Libraries:**
If these libraries are not installed already, run the code in Anaconda’s CMD.exe Prompt.
- `conda install -c anaconda beautifulsoup4`
- `pip install scikit-learn`
- `pip install pymysql`
- `pip install deep-translator`
- `pip install mecab-python3`
- `pip install fugashi`
- `pip install urllib3`
- `pip install ipywidgets`

Once everything has been completed, run the code by selecting Jupyter Notebook in the Anaconda Navigator.                                                                    



