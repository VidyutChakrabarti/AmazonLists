import express from "express";
import cors from 'cors';
import bodyParser from 'body-parser';
import axios from 'axios';

const app = express();

app.get("/", (req, res) => {
    res.send("Server is ready")
})

app.use(cors())
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/submit', async (req, res) => {
    const { profileLink, postLinks, productName, description } = req.body;

    try {
        const response = await axios.post('http://127.0.0.1:5000/process', {
            profileLink,
            postLinks,
            productName,
            description
        });
        res.status(200).json({
            message: 'Form submitted successfully!',
            data: response.data
        });
    } catch (error) {
        res.status(500).json({ message: 'Error processing data', error: error.message });
    }
});


app.listen(8501, () => { console.log("Server initiated."); }); 
