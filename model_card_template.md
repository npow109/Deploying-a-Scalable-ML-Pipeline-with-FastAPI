# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is trained on census data from 1994. It uses the RandomForestClassifier.
## Intended Use
To predict whether a person has higher or lower than a 50k salary. 
## Training Data
Census data from 1994. 
## Evaluation Data
The evaluation data came from using data splits.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
The metrics used are.
Fbeta score: 0.6626
precision: 0.7280,
recall: 0.6079

The model also outputs the slices with all three metrics in the slice_output.txt. 

## Ethical Considerations
An ethical consideration is to use this model knowing that it is not flawless and making sure that people know that no matter what is made using this model, the data comes from 1994.

## Caveats and Recommendations
50k was a good salary back in 1994 but is not so much today. Today we should have a much higher salary cut off.