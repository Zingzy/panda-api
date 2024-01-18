
<table align="right">
    <tr>
        <td align="center"><img src="https://pandaa.vercel.app/raw_pic" style="height: 220px;"></td>
    <tr>
    <tr>
        <td>😉 random pic using our api ⬆️</td>
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

### Random Panda Picture (Raw)
- **Endpoint:** `/raw_pic`
- **Method:** `GET`
- **Description:** Experience the panda cuteness with a streaming response of a random panda picture. 🎥🐼

### Random Fact and Picture Combo
- **Endpoint:** `/both`
- **Method:** `GET`
- **Description:** Get both a random panda fact and the URL of a matching panda picture. Double the cuteness! 🤩🐼

### All Panda Facts
- **Endpoint:** `/all-facts`
- **Method:** `GET`
- **Description:** Explore a collection of all panda facts. Impress your friends with a wealth of panda trivia! 📚🐼

### All Panda Pictures URLs
- **Endpoint:** `/all-pics`
- **Method:** `GET`
- **Description:** Access URLs of all panda pictures available in the API. Share the love for pandas with these adorable images. 🌈🐼

### Specific Panda Picture
- **Endpoint:** `/i/{file_name}`
- **Method:** `GET`
- **Description:** Retrieve a specific panda picture by filename. Customize your panda experience! 🖼️🐼

_For a more detailed API visit : https://pandaa.vercel.app/docs_

<h2>🛠️ Installation</h2>

### Direct Deployment

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/Zingzy/panda-api)

### Manual Setup
1. Clone the repository `git clone https://github.com/Zingzy/panda-api.git`.
2. Install the required packages using `pip install -r requirements.txt`.
3. Install [uvicorn](https://www.uvicorn.org/) using `pip install uvicorn`.
4. Run the server using `uvicorn main:app --reload`.

<h2>🤝 Contributing</h2>

Feel free to contribute to the Panda API by adding more panda facts, pictures, or improving the code. Create a pull request, and let's make the panda world even more delightful! 🎉🐼

**Enjoy the Panda API! 🐼✨**
