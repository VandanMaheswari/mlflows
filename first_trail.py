import mlflow


def calculate_sum(x,y):
    return x*y


if __name__ == "__main__":
    # starting the mlflow server so that can tracks
    with mlflow.start_run():
        x,y = 10,20
        z= calculate_sum(x,y)
        # tracking the experiment with mlflow
        mlflow.log_param("x" , x)
        mlflow.log_param("y" , y)
        mlflow.log_metric("z" ,z)
        
        

# it will create a folder name mlruns inside this it have 0 name folder
# whichh represents 1st file and containg information in a unqiue id
# it has all the information of param and metricd and manymore 