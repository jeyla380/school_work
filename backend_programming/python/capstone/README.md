# Book Title Translation Project

### Table of Contents:
| [Project Proposal Plan](#project-proposal-plan) | [Post-Implementation Report](#post-implementation-report) | [Sources](#sources) | [Additional Notes](#additional-notes) |
| :--: | :--: | :--: | :--: |

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

### 6. Projected Timeline of Project*
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


### 7. Outline of Project
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

[Return to the Top](#book-title-translation-project)

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

### 2. Machine Learning

The application that was created is a Book Title Translation tool that uses a machine learning model to translate book titles between English, French, and Japanese. It takes a book title in one language as input and generates the translated book title in the two other languages as output.

The models are trained using a large dataset of identical sentences in English, French, and Japanese. Additional algorithms and libraries that were used to create the models include:

- `BeautifulSoup` – Web scraping library used to scrape the data needed to train the model.
- `deep_translator` – Library used to translate the English sentences to French using `GoogleTranslator`.
- `NLTK` – Natural language processing library used mainly used for tokenization in this project.
- `scikit-learn` – Machine learning library used for data preprocessing and evaluation.
- `torch` (PyTorch) – Deep learning framework used for building and training models through seq2seq.

The implementation plan for the application involved several steps:
- Scrape data from Tangorin (Section E) to collect a large dataset of identical sentences in English, French, and Japanese amounting to 150,000 sentences total (50,000 sentences in each language).
- Translate the data using GoogleTranslator for French sentences (using English sentences), and create dataframes for each language.
- Save each dataframe as a .csv file that will be used to avoid re-running the scraping and translation code; turn .csv files into a dataframe to make it easier to read.
- Merge the dataframes into a single dataframe so each row of sentences are identical in each language.
- Clean the data of the merged dataframe to remove non-alphabetical characters (except very limited punctuation like apostrophes and hyphens) in English and French, and non-Latin characters in Japanese.
- Split the data into training, valid, and testing sets to make it more suitable for seq2seq.
- Create the encoder, attention layer, and decoder that will be used to create models through the seq2seq neural network.
- Train the models by creating training and evaluation loops (through epochs) through each fold to avoid overfitting and/or underfitting.
- Evaluate the models using the BLEU score metric and the confusion matrix to assess their performance on how well they translated.
- The models can be further improved by gathering more data and having more processing power, as well as possibly fine-tuning the hyperparameters.

Using PyTorch as the deep learning framework provided a wide range of functionality and usability for building and training neural networks, it made it a simple choice to use. 

Overall, the decisions made in this Book Title Translation application were driven by the need of using a large and diverse dataset and the choice of using a suitable deep learning framework that could handle gathering and trying my own data.

### 3. Validation
In order to assess the model’s accuracy, `NLTK`’s BLEU was used to compare translations. BLEU is specifically used for machine-translated text, which is why this is used to evaluate the model rather than F-1 Score, Accuracy, etc.

The result of a BLEU score is between 0 and 1, where 0 is low quality translation, and 1 means extremely high-quality translation. However, it needs to be noted that human translators don’t achieve a perfect score of 1.

|BLEU Score | Interpretation* |
| :--: | :--: |
| 0 - 0.09| Essentially useless |
| 0.1 - 0.19| Hard to understand |
| 0.2 - 0.29 | The idea is there, but has significant grammatical errors |
| 0.3 - 0.39 | Understandable, good translations |
| 0.4 - 0.49| High quality translations |
|0.5 - 0.59 | Very high-quality translations, adequate, fluent |
|> 0.6 | Quality better than human |

<span style="font-size:10pt">*From Evaluating Models (Sources)</span>

### 4. Solution Summary 

**Problem:**
- The Simple Bookstore is expanding globally with new locations in Paris, France and Tokyo, Japan along with new locations in the United States. They are looking to update their list of popular books with translated versions for all their stores.

**Results:**
- The results of the models are not as expected. There may be couple reasonings for this: 
   - The dataset may not be large or diverse enough to train the model.
      - English and French are both Latin-based languages, so they may not need large datasets for their models to translate efficiently.
   - The vocabulary may be too diverse where it may be difficult for the model to translate effectively.
   - The computer’s processing power isn’t enough to handle batch sizes greater than 32. Therefore, if the batch size was larger, it may have been able to reduce the overfitting and/or underfitting of the models.

**Solution:**
- These different set of solutions are all based on hypotheses that may help reduce overfitting and/or underfitting for models, which in turn will allow for more accurate translations.
   - Web scrape at least 150,000 sentences or more for each language or find a dataset that already contains 150,000 or more sentences.
      - Especially since Japanese uses three different alphabets, for a more efficient translation, a large database of sentences should be used.
   - Ensure that the sentences are not too overly diverse if the dataset is smaller, keep the sentences simple. The larger the dataset, the more diverse the sentences can be.
   - Increase the batch size to at least 128 or more. More time and processing power will be required, so a computer with faster processing speed is highly recommended so the computer doesn’t need to run over the course of days or weeks.

### 5. Data Summary
- The data was provided by Tangorin (found in Sources) by web scraping the sentences in Japanese and their English translations.
- The French sentences were translated using the deep_translator’s GoogleTranslator API by translating the sentences from English to French as Tangorin didn’t have any French translations.
- The sentences in each language were turned into dataframes for each language, which was in turn merged into an entire language dataframe that contained the translated sentences next to each other.
- Each of the dataframes were saved as a .csv file in order to prevent running the code again as it took hours and days to create the dataframes for each language.
- The rest of the project used the .csv files that were created to prevent any issues or errors when running the entire project.


### 6. Visualizations

*Note: The visualizations can be viewed in the `Book Title Translation.ipynb` file.*

**Train Loss and Validation Loss:**
- Based on the results of the graphs, English to French, and French to English seems to have good results for the first fold, but folds afterwards tend to become either overfitted and/or underfitted.
- Any translation that involves Japanese does not do well at all. This could be due to a variety of reasons, but the best guess is most likely due to not having enough data to train the model properly as Japanese is not a Latin-based language like English and French.

<span style="font-size:10pt">*To view examples on what an overfitting, underfitting, and good fit graphs look like when training models: https://www.baeldung.com/cs/training-validation-loss-deep-learning </span>

**Machine Translation vs. Native Translation for Basic Sentences:**
- A good translation model will usually have most 1s concentrated diagonally. The French to English model is a good example of how the heatmap should look when compared to the rest of the models.
- If a model has a 1 that is not diagonal, this means there was an error in translation. The French to Japanese model is an example of this as there were no 1s concentrated along the diagonal.

**BLEU Scores:**
- As seen in the graph, the English and French translations seemed to do well when translating basic sentences and complex sentences. 
   - However, when looking at the English to French translation, it did worse than the French to English translation. This could mean that a variety of French sentences can mean the same thing in English, but it doesn’t work from English to French.
- Any model that included Japanese did not do well with their BLEU score, and all models had a score of 0. Examples of what the sentences look like can be seen in the previous visualization of the heatmap.


[Return to the Top](#book-title-translation-project)

<br>

## Sources
- Example sentences - Japanese Dictionary Tangorin. (n.d.). Tangorin. https://tangorin.com/sentences
- Best Books of the 20th Century (7827 books). (n.d.). https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century
- Les 200 meilleurs livres du XXe siècle - Liste de 200 livres - Babelio. (n.d.). Babelio. https://www.babelio.com/liste/3044/Les-200-meilleurs-livres-du-XXe-siecle
- 【2021年に読みたい!】読者が選ぶ、おすすめ名作小説ベスト100ランキング! - キャンペーン・特集 - 漫画・ラノベ(小説)・無料試し読みなら、電子書籍・コミックストア ブックライブ. (n.d.). 株式会社BookLive. https://booklive.jp/feature/index/id/novel100#
- 人気書店が選ぶいま読んでおきたい100冊– LITERATURE – | Discover Japan | ディスカバー・ジャパン. (2017, April 14). Discover Japan | 日本の魅力、再発見 ディスカバー・ジャパン. https://discoverjapan-web.com/article/23141
- Language Translation with TorchText — PyTorch Tutorials 1.7.1 documentation. (n.d.). https://pytorch.org/tutorials/beginner/torchtext_translation_tutorial.html
- Tatoeba: Collection of sentences and translations. (n.d.). https://tatoeba.org/en
- Evaluating models. (n.d.). Google Cloud. https://cloud.google.com/translate/automl/docs/evaluate

[Return to the Top](#book-title-translation-project)


<br>
<hr>

### Additional Notes
- The actual models of each language pair is not located in the files as the file size for each one is too large.
- The password for the SQL database is partially removed.

[Return to the Top](#book-title-translation-project)
