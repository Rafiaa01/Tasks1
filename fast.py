from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()


class sentiment(BaseModel):
    text: str = Field(min_length=1)
    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty or contain only spaces")
        return value

@app.post("/sentiment")
def sentiment_analysis(data: sentiment):
    text = data.text.lower()

    if "love" in text:
        sentiment = "positive"
    elif "hate" in text:
        sentiment = "negative"
    else:
        sentiment = "missing"

    return {"sentiment": sentiment}
