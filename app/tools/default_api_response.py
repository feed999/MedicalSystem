
    
async def default_api_response(message:str):
    return {
  "detail": {
    "status": 200,
    "message": message
  }
}
    
async def default_api_response_success():
    return {
  "detail": {
    "status": 200,
    "message": "success"
  }
}