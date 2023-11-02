const express = require('express');
const app = express();
const port = 3000;
const tf = require('@tensorflow/tfjs-node');
const fs = require('fs');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

async function loadModel() {
  const model = await tf.loadLayersModel('file://./model.json');
  return model;
}

const modelPromise = loadModel();

app.use(express.json());
// Define a basic route
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.post('/survey', async (req, res) => {
  try {
      //Recieve survey data
      const inputData = req.body;

      //check if survey is correct json format
      if (inputData == null || inputData == undefined) {
        res.status(400).json({ error: 'Invalid survey data' });
      }

      //append data to csv file
      const csvWriter = createCsvWriter({
        path: 'survey.csv',
        header: [Age,Gender,Country,self_employed,family_history,work_interfere,no_employees,remote_work,tech_company,benefits,care_options,wellness_program,seek_help,anonymity,leave,mental_health_consequence,phys_health_consequence,coworkers,supervisor,mental_health_interview,phys_health_interview,mental_vs_physical,obs_consequence, treatment]

      });



  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Prediction failed' });
  }
});

app.get('/predict', async (req, res) => {
  try {
    const inputData = {
        "Age": 0.30555556,
        "Gender": 1,
        "Country": -1.33482913,
        "self_employed": 0,
        "family_history": 0,
        "work_interfere": -1.82607739,
        "no_employees": 1.27362025,
        "remote_work": 0,
        "tech_company": 1,
        "benefits": 0,
        "care_options": 1,
        "wellness_program": 1,
        "seek_help": 1,
        "anonymity": 1,
        "leave": 1.05339184,
        "mental_health_consequence": 2,
        "phys_health_consequence": 0,
        "coworkers": 0,
        "supervisor": 0,
        "mental_health_interview": 0,
        "phys_health_interview": 0,
        "mental_vs_physical": 0,
        "obs_consequence": 1
      }
    const model = await modelPromise;
    const data = [Object.values(inputData)];
    //const inputTensor = tf.tensor([[ 0.30555556, 1. ,-1.33482913 ,0.  ,0. , -1.82607739 , 1.27362025 ,0. ,1. , 0. , 1. ,1. ,1. ,0. ,1.05339184  , 2. ,0. ,0. ,0. , 0. , 0. ,1. ,0.]]);
    const inputTensor = tf.tensor(data);
    const prediction = model.predict(inputTensor);
    res.json({ prediction: prediction.arraySync() }); // Send the prediction as a JSON response
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Prediction failed' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});