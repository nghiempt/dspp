// // const axios = require("axios");

// // const apiUrl = "https://www.llama2.ai/api";

// const axios = require("axios");
// const fs = require("fs");

// const apiUrl = "https://www.llama2.ai/api";

// // Read prompts from input.json
// const prompts = JSON.parse(fs.readFileSync("/Users/nghiempt/Corporation/scientific_research/paper_policy/task/hungnn_llama/hungnn_llama_nodejs/input2.json"));

// // Define an array to store the results
// const results = [];

// // Define a function to make the API request and save the result
// function processPrompt(prompt) {

//   axios
//     .post(apiUrl, requestData, {
//       headers: {
//         "Content-Type": "application/json",
//       },
//     })
//     .then((response) => {
//       console.log("Response:", response.data);
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//     });

//   console.log("Processing:", prompt.prompt);
//   console.log("=============================================================================");
//   fs.writeFileSync("/Users/nghiempt/Corporation/scientific_research/paper_policy/task/hungnn_llama/hungnn_llama_nodejs/output.json", JSON.stringify("abc", null, 2));
//         console.log("Results saved to output.json");

// }

// // Loop through each prompt and process it
// prompts.forEach(processPrompt);

const axios = require("axios");
const fs = require("fs");

const apiUrl = "https://www.llama2.ai/api";

// Read prompts from input.json
const prompts = JSON.parse(fs.readFileSync("input2.json"));

// Define an array to store the results
const results = [];

// Define a function to make the API request and save the result
async function processPrompt(prompt) {
  let requestData = {
    prompt: `[INST] ${prompt.prompt} [/INST]`,
    version: "2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
    systemPrompt:
      "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store.",
    temperature: 0.75,
    topP: 0.9,
    maxTokens: 800,
    image: null,
  };

  console.log(requestData);
  console.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`");

  await axios
    .post(apiUrl, requestData, {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      console.log("Response:", response.data);

      // Add the response data to the results array
      results.push(response.data);

      console.log(results);
      console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");

      // Check if all prompts have been processed
      if (results.length === prompts.length) {
        // Save the results to output.json
        fs.writeFileSync("output.json", JSON.stringify(results, null, 2));
        console.log("Results saved to output.json");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Loop through each prompt and process it
prompts.forEach(processPrompt);
