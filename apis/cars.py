from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello, world!"}
models = [
    {
      "brand": "Tata",
      "model": "Nexon",
      "type": "5-seater",
      "description": "Tata Motors is known for safety and performance."
    },
    {
      "brand": "Audi",
      "model": "A4",
      "type": "5-seater",
      "description": "Audi is a German brand known for luxury and innovation."
    },
    {
      "brand": "Benz",
      "model": "C-Class",
      "type": "5-seater",
      "description": "Mercedes-Benz offers top-tier performance and comfort."
    }]
@app.get("/cars")
def car_details(name: str):
    res = {}
    if (name == "Benz"):
        res = models[2]
    elif (name == "Tata"):
        res = models[0]
    else:
        res = models[1]
    return res




