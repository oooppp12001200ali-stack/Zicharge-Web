from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Zicharge Backend")

class OTPRequest(BaseModel):
    phone: str

@app.get("/")
def read_root():
    return {"message": "Zicharge Backend Active"}

@app.post("/auth/request-otp")
def request_otp(request: OTPRequest):
    otp = "1234"
    return {"otp": otp, "phone": request.phone}

class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: float

@app.post("/wallet/transfer")
def transfer(request: TransferRequest):
    return {"status": "success", "from": request.from_account, "to": request.to_account, "amount": request.amount}
