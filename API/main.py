from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io

app = FastAPI()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    
    if not file.filename.endswith(".csv"):
        return {"error": "Please upload a CSV file."}

    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    
    if 'age' not in df.columns:
        return {"error": "CSV must contain an 'age' column."}

    
    avg_age = df['age'].mean()


    return {
        "message": "File processed successfully!",
        "average_age": round(avg_age, 2),
        "total_users": len(df)
    }
