
<table align="right">
    <tr>
        <td align="center"><img src="https://panda.spoo.me/raw_gif" style="width: 300px;" alt="Please Reload"></td>
    <tr>
    <tr>
        <td align="center">⬆️ random gif using our api 😉</td>
    </tr>
</table>

<h1>🐼 Panda API 🌟</h1>

Welcome to the Panda API, where cuteness meets information about everyone's favorite black and white bears! This API serves random panda facts and adorable pictures to brighten up your day.

<h2>📖 Documentation</h2>

### Base URL
- **URL:** `https://pandaa.vercel.app`
- **Description:** The base URL for all endpoints.
- **Note:** All endpoints are relative to the base URL.

<h2>🚀 Endpoints</h2>

### Random Panda Fact
- **Endpoint:** `/fact`
- **Method:** `GET`
- **Description:** Get a random panda fact to amaze your friends with panda knowledge! 🧠🐼

### Random Panda Picture URL
- **Endpoint:** `/pic`
- **Method:** `GET`
- **Description:** Obtain the URL of a random panda picture for an instant dose of cuteness. 📸🐾

### Random Panda GIF URL
- **Endpoint:** `/gif`
- **Method:** `GET`
- **Description:** Get the URL of a random panda GIF to share the panda love! 🎁🐼

<table align="right">
    <tr>
        <td align="center"><img src="https://panda.spoo.me/raw_pic" style="height: 180px;"></td>
    <tr>
    <tr>
        <td align="center">⬆️ random pic using our api 😉</td>
    </tr>
</table>

### Random Panda Picture (Raw)
- **Endpoint:** `/raw_pic`
- **Method:** `GET`
- **Description:** Experience the panda cuteness with a streaming response of a random panda picture. 🖼️🐼

### Random Panda GIF (Raw)
- **Endpoint:** `/raw_gif`
- **Method:** `GET`
- **Description:** Experience the panda cuteness with a streaming response of a random panda GIF. 🎥🐼

### Random Fact, Picture URL, and GIF URL (All in One)
- **Endpoint:** `/all`
- **Method:** `GET`
- **Description:** Get a random panda fact, picture URL, and GIF URL in one request. 🎁🐼

### All Panda Facts
- **Endpoint:** `/all-facts`
- **Method:** `GET`
- **Description:** Explore a collection of all panda facts. Impress your friends with a wealth of panda trivia! 📚🐼

### All Panda Pictures URLs
- **Endpoint:** `/all-pics`
- **Method:** `GET`
- **Description:** Access URLs of all panda pictures available in the API. Share the love for pandas with these adorable images. 🌈🐼

### All Panda GIFs URLs
- **Endpoint:** `/all-gifs`
- **Method:** `GET`
- **Description:** Access URLs of all panda GIFs available in the API. Share the love for pandas with these adorable GIFs. 🌟🐼

### Specific Panda Picture
- **Endpoint:** `/i/{file_name}`
- **Method:** `GET`
- **Description:** Retrieve a specific panda picture by filename. Customize your panda experience! 🖼️🐼

### Specific Panda GIF
- **Endpoint:** `/g/{file_name}`
- **Method:** `GET`
- **Description:** Retrieve a specific panda GIF by filename. Customize your panda experience! 🎥🐼


_For a more detailed API visit : https://pandaa.vercel.app/docs_

<h2>🛠️ Installation</h2>

### Direct Deployment

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/Zingzy/panda-api)
<a href="https://render.com/deploy?repo=https://github.com/Zingzy/panda-api">
<img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render" height="30px"/>
</a>

### Manual Setup
1. Clone the repository `git clone https://github.com/Zingzy/panda-api.git`.
2. Install the required packages using `pip install -r requirements.txt`.
3. Install [uvicorn](https://www.uvicorn.org/) using `pip install uvicorn`.
4. Run the server using `uvicorn main:app --reload`.

<h2>🤝 Contributing</h2>

Feel free to contribute to the Panda API by adding more panda facts, pictures, or improving the code. Create a pull request, and let's make the panda world even more delightful! 🎉🐼

## Submission Guidelines

- Create a new branch for your changes.
- Make sure your code is formatted using [Black Formatter](https://pypi.org/project/black/)
- If you are adding a new panda fact, add it to the `facts.txt` file in a new line, ending with a full stop.
- If you are adding a new panda picture, add it to the `pics` folder.
- The picture filename should be in the format `{number}.jpg`, where `{number}` is the next number in the sequence.
- The picture should **not be more than 300 KB** in size.
- If you are adding a new panda GIF, add it to the `gifs` folder.
- The GIF filename should be in the format `{number}.gif`, where `{number}` is the next number in the sequence.
- The GIF should **not be more than 2 MB** in size.


**Enjoy the Panda API! 🐼✨**
