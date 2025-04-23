# Data Analysis Checklist

At Tacoma Power, I'm frequently presenting my own models and reviewing the models of others.  In many cases, we leap straight to the exciting stuff: what statistical model was selected and how it works.  But statistical modeling is a journey, and as a reviewer, I would like the full story of the road that was taken, the deadends that were explored, and the roads that were not taken.  The seven bullets below cover the major categories of decisions the modeler makes that I would want to see when reviewing a model.

1)	Problem definition, context, and description including identification of the key predicted variable.
2)	Exploratory data analysis of potential predictor and predicted variables.  Plots and summary statistics looking for non-linearities, distribution shapes (e.g., non-normalities), outliers and correlations.  
3)	Criteria used for evaluating models, such as squared error on unseen data.    
4)	Predictor variable selection and transformations. What predictor variables were selected and why.  What predictor variables were left out and why.  What transformations were used and why.  
5)	Model selection.  What model form was selected and why.  What forms were considered, but not selected, and why.
6)	Predictive checks such as residuals plots (predicted vs. actual) and counterfactual analysis (what does the model do if we change x).  
7)	Reproducibility and replication.  Everything needs to be documented and easily updated and modified!  A superficial analysis that is well documented and easily modified is far more useful than a perfect analysis that cannot be followed or recreated.      
