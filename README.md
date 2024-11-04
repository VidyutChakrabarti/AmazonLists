# AmazonLists
An app to automate conversion of social media posts into amazon listed products.

## How to Run the App
1. To run the app, open the terminal inside the folder AmazonLists and use the following commands:

```powershell
npm install
```
```powershell
npm run dev
```

2. Open another powershell terminal and run the following commands: 
```powershell
cd frontend
```
```powershell
npm install
```
```powershell
npm run dev
```
3. Finally open another terminal and run the following commands: 

```powershell
cd backend
```
```powershell
python api.py
```

### Your .env in the AmzzonLists folder will have the following keys: 
VITE_GEMINI_API_KEY=
VITE_MODEL=gemini-1.5-flash