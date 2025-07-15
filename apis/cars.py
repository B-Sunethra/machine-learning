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
      "description": "Tata Nexon is known for its safety, compact design, and fuel efficiency."
    },
    {
      "brand": "Tata",
      "model": "Safari",
      "type": "7-seater",
      "description": "Tata Safari is a spacious SUV built for family adventures."
    },
    {
      "brand": "Audi",
      "model": "A4",
      "type": "5-seater",
      "description": "Audi A4 is a luxury sedan combining elegance and advanced tech."
    },
    {
      "brand": "Audi",
      "model": "Q5",
      "type": "7-seater",
      "description": "Audi Q5 is a premium SUV offering performance and comfort."
    },
    {
      "brand": "Benz",
      "model": "C-Class",
      "type": "5-seater",
      "description": "Mercedes-Benz C-Class delivers style, comfort, and performance."
    },
    {
      "brand": "Benz",
      "model": "GLC",
      "type": "7-seater",
      "description": "Mercedes-Benz GLC is a luxury SUV built for dynamic driving experiences."
    }
  ]
@app.get("/cars")
def car_details(name: str):
    res = []
    for model in models:
        if(model["brand"] == name):
            res.append(model)
    return res




