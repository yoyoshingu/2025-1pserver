import uvicorn
from fastapi import FastAPI

from irisModel import IrisMachineLearning, IrisSpecies

app = FastAPI()

model = IrisMachineLearning()

@app.get("/")
async def root():
    return {"message": "Hello, this is iris classfier 2025/3/10"}

@app.get("/predict")
async def predict():
    pred = model.predict_species(5.0, 3.4, 1.4, 0.2)
    return {"prediction":pred}

@app.post("/predict")
async def predict_species(iris:IrisSpecies):
    pred = model.predict_species(iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width)
    return pred

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
