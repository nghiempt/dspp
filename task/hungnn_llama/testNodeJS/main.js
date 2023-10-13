const axios = require("axios");

const apiUrl = "https://www.llama2.ai/api";

const requestData = {
  prompt:
    "[INST] Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent.\nNotes when classifying:\n+ Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides.\n+ Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it.\n+ Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided.\nNote: always gives me the result (0 or 1) in the form below:\nIncomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)\nBelow is information for 2 parts:\nData Safety - Share section: No data shared with third parties;\nPrivacy Policy - Share section: The section that specifically mentions sharing information is:\n\"But under some criteria, your limited information is shared with us:-\nWe take location permission to support Geo tag feature of the app, This feature helps you to tag the location to the photos where they were taken.\nIf you submit bugs report to us at our email address then information such as your name, email address or any information you provide while contacting us is shared with us but we don't use any of the information provided by you in any ways for our own interest and it is kept limited to us only. Information provided by you will help us improve and develop higher quality products. We shall disclose your information with your prior permission only, with applicable law within or outside your country, by requesting the public or governmental authorities to protect our legal rights or interest.\nOur Apps uses third party ads provider to serve you ads based on your personal interest. Ads are shown by Admob that are relevant to you if you want to know more about them please visit https://www.google.com/settings/ads/.\nWe may collect and use your non-personal information such as Your phone's IMEI number, Android ID, CPN model, memory size, phone model, ROM memory size, Country, Mobile operator name etc.. We may use this information for understanding usage frequency, or solving bugs in our products and improve the user experience. This information we use to see install- uninstall rate of users on our app and also usage frequency.\nWhen manually requested, This app sends selected media(By You) from the device to a desired destination also selected by (you the user). such as email, social media, a different app, or other targets selected by you. here also, we do not collect/store/send/manage any data.\nWe use Firebase Analytics for monitoring our app's performance and users activities within our app to collect crashes or bugs in our app that help us to make our products more stable and better. You may visit Firebase policy to understand more about it https://firebase.google.com/policies/analytics/. [/INST]",
  version: "2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
  systemPrompt:
    "You are an assistant who analyzes and evaluates the correct, complete and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store.",
  temperature: 0.75,
  topP: 0.9,
  maxTokens: 800,
  image: null,
};

axios
  .post(apiUrl, requestData, {
    headers: {
      "Content-Type": "application/json",
    },
  })
  .then((response) => {
    console.log("Response:", response.data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
