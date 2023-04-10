## Install WFDB Software Package
     Follow instructions in: https://physionet.org/physiotools/wfdb-linux-quick-start.shtml 


## Install requirements
    > pip install -r requirements.txt

## Download Dataset
    > get data from https://www.physionet.org/content/afpdb/1.0.0/

## Copy paste afpdb folder to current directory 
    >  rename data dir name afpdb  

## Go to src folder
    > cd src

## Create CSV files 
    > python dat2csv.py

## Create training and test dataset
    > mkdir training test
    
## Create .npy files 
    >  python create_dataset.py

## Create Neural Network model and train it 
    > python train.py

## Best Model
     Rename the best model from my_model.h5 to best.h5
     

## Make predictions with best model (90% accuracy)
    > python predict.py

