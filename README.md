## BANK MARKETING CAMPAIGN

* Dataset found on UCI Machine Learning Repository Website: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
* It makes reference to a marketing campaign performed from 2008 to 2010
* 'Y' column refers to if the customer finally contracted the product promoted:a term deposit

# Testing data
* Here I tried to pick the most convenient dataset among the 4th found once you download the files
* I finally selected bank-full.csv because its higher sample and more meaningful labels for my analysis and predictions (be careful if you try to predict with techniques such us KNN Classifier, it takes a lot of time to perform the calculations).

# Exploratory analysis
* There are Neither NaN nor duplicates
* Left skewness and a lot of outliers 

After performing these plots and aggregations we can conclude that the characteristics of the ideal customer which is the most likely to contract our deposit are:
* Works in **managemet**, moreover(taking into account their lower sample), **service**, **retired** and **students** have some bigger propension to contract this product more frequently.
* In total, there are more married people, however **singles** show a significant propension
* Same happen with education, secondary is the most numerous atribute but **tertitary** educated people tend to be more open.
* With default the tendency is sligh because of the little sample but seems that if you have **previous unpaid loan** you are less likely to contract it.
* No matter if you had a housing or **any other kind of loan**, you are **less likely** to want a deposit.
* Calling to the **celular** seem to have a higher success ratio
* **May** is the moth with **more contracts** signed but this and specially **July** show a *bad performance* getting sucess, while **april, february, october, september and march** is *good*.

# Transformations
* Remove outliers
* Power Transformer: to reduce skewness and have a more Gaussian-like distribution 
* Min Max Scaler: to make meaningful comarisons between categorical and numerical columns
* One Hot Encoder: to be able to 
* Oversampling and SMOTE: both used to reduce imbalance of target column and check with which method we obtain a better result

# Models:
* Logistic Regression: not a good performance low kappa cohen but better results with SMOTE. The model tends to predict "No" more or less good but really bad performance with yes and gives a lot of false positive and negetive
* KNN Classifier: tried many model but a clear elbow hasn't been seen computing neighbors from 2 to 14, it seems the best model tried has 3 neighbors, weight=uniform and p=1, but tends to overfit and predict really bad the possitive answers in the test set.
**In real life we wouldn't pick any of them to predict our taget label**

# Other things that I would like to try but I have not been able to because of time available:
* Reduce cardinality in the columns *job* grouping the less frequent proffesions and *month* grouping them by quarters.
* Perform an analysis by *age* creating bins 
* Try another methods to make more accurate predictions, but I don't have the tools to do it by the moment.
