from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
   
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mike salamokhen</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 0;
      background: linear-gradient(to right, #4facfe, #00f2fe);
      color: #333;
    }
    .container {
      max-width: 800px;
      margin: 40px auto;
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
    }
    h1, h2 {
      text-align: center;
    }
    .photo {
      display: flex;
      justify-content: center;
      margin-bottom: 20px;
    }
    .photo img {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid #00c6ff;
    }
    .info {
      margin-top: 20px;
    }
    .info p {
      font-size: 18px;
      margin: 10px 0;
    }
    @media (max-width: 600px) {
      .container {
        margin: 10px;
        padding: 20px;
      }
      .info p {
        font-size: 16px;
      }

}
  </style>
</head>
<body>

<div class="container">
  <h1>Bienvenue sur ma page</h1>
  
  <div class="photo">
    < src="IMG_20250207_121132-COLLAGE.jpg" alt="Ma photo">
  </div>

  <div class="info">
    <h2>Informations personnelles</h2>
    <p><strong>Nom :</strong> Mike</p>
    <p><strong>Âge :</strong> 22 ans</p>
    <p><strong>Profession :</strong> Développeur</p>
    <p><strong>Email :</strong> mike@email.com</p>
    <p><strong>À propos :</strong> Passionné par le code et la technologie.</p>
    <p><strong>programme en:</strong>python,HTML,</p>
    
  </div>
</div>

</body>
</html>

       

 '''

if __name__ == "__main__":
    app.run(host='localhost') #()
    