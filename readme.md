Image Classifier with Deep Learning

Aim: 
All adjectives are subjective. What is messy to one is acceptable to another. 
In a bid to get residents under the same roof (my kids) to clean up their mess, this classifier aims to get everyone in the household to come to a consensus of what is clean/tidy vs messy with synonyms used on google when scrapping images. WHen they fail, the child is allowed to write a petition stating his reasons. These petitions/notes form my 3rd class which I termed "Bad_Excuse". At the moment, my kids are unaware that I set the rules such that every petition will lead to the same one outcome - "Bad_Excuse". In the process, hopefully their handwriting and their persuasiveness will also improve.

Process: 
1. Scrap and convert images from google for 1) Clean/Tidy room, 2) messy rooms and 3)excuses for written notes.
2. Eyeball and remove images with "before"/"after" and cartoons and sort them into i)Bad_Excuse, ii) Clean_Room, iii) Messy_Room.
2b. Dataset available at https://drive.google.com/open?id=1YVlio16nUdvqSxzYw36719Ns8oYb0fox
3. Build machine learning model with 8 different algo. XGBoost yields the best F1 score.
4. Build a simple neural network as base model for deep learning.
5. Build a Convoluted NN with SGD optimizer and early stopping
6. Build a Convoluted NN with 'adam' optimizer and early stopping
7. Experiment with transfer learning using the vgg16.
8. Compare the F1 across all models
9. Run trial with test images in images folder. Noted that "CNN_excuse", "CNNCleanRoom" and "CNNMessyRoom" gets progressively accurately-classified with each progressive model but the ones with transfer learning were wrongly classified despite better scores of 0.9. This is due to overfitting.
10. Conclusion: CNN with 'adam' optimizer with best weights restore and early stopping is best. 
11. Blog available at https://bit.ly/2npUiNj