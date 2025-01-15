# techstax-webhook-repo
<!-- How to run backend -->
1. Create Environment 
# python -m venv env_name
2. Activate Environment 
   # cd env
   # Scripts/activate
3. Install Dependencies Present in requirement.txt
   # pip install -r requirement.txt

4. Run the backend(first go to the dir where run.py is present)
   # python run.py

<!-- Set ngrok for live url -->
1. Download Ngrok
2. Setup the path for Ngrok
3. Run command to get live url
   #  ngrok http 5000
4. set ngrok live url in webhook url of techstak-action-repo

<!-- How to run front-end -->
1. Go to the frontend dir
2. Install node_modules
 # npm i
3. Run the Project
 # npm run start 