import os


n_estimators =[110,100,150,200,210]
max_depth =[20,25,15,10,5]


for n in n_estimators:
    for m in max_depth:
        os.system(f"python basic_ml_model.py -n{n} -m{m}")
        
        # this is the file which have custom grid search by using every combination
        # and we have doing nothing just running run.py which have the code
        # which runs the basic_ml_model.py file in a for loop
        # by passing every combination which we passed by using os.system()
        # inside system we pass (f"python basic_ml_model.py -n{n} -m{m}")
        # and different experiment will creatd