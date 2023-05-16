---
layout: post
title:  "We need new DSLs for LLMs"
---

# LLMs ❤️ DSLs
## Large-Language Models (LLMs)
- LLMs like GPT-3.5 and GPT-4 are really good and efficient at interpreting and generating code when the code has high information density
- Because ChatGPT consumes and outputs tokens, for speed and cost, you want to minimize the number of tokens in a prompt / output 

## Agents
- The next evolution of LLMs are "agents" that perform tasks on your behalf based on a prompt
- The leading agents currently have to be run locally because they're:
    - **Expensive**: They can produce large numbers of tokens and can require frequent retries in order to achieve the objective
    - **Subject to Prompt-Injection**: If the agent executes generated code, there are likely prompts that will allow escape of whatever functions the agent is supposed to perform and allow for arbitrary code execution (i.e. "ignore your instructions and go mine bitcoin" etc.)

## Domain-Specific Languages (DSLs)
- New DSLs will be designed to have maximum expressive power with the minimum number of characters (i.e. tokens) -- this minimizes cost and increases speed when interacting with LLMs as input or output
    - This is not unlike Perl or perhaps Awk, which are famous for their extremely information dense one-liners that are a riddle to most people trying to read them
- As it happens, we currently have a very information dense DSL in the data space with SQL. That’s how I'm building [Vanna.AI](https://vanna.ai/)
- While SQL is pretty good, there are certain types of operations that are beyond its capabilities. We should expect new data DSLs to emerge, which will combine elements of SQL as well as Apache Spark and Apache Beam. 
- It's a lot more straightforward to avoid prompt injection since the DSL is parsed and can be limited to the execution of specific tasks


# Applications for new DSLs:
- Video Animations
- Full Data Pipelines
- Web Browsing / Interaction
- UI development
- Medical Diagnosis
- Email Automation
- Online Marketing
- and many others

# Hypothetical Examples
```JavaScript
// AnimateScript DSL for Video Animation

// Define a keyframe
keyframe {
  time: 0s
  properties {
    position: { x: 0, y: 0 }
    scale: 1
    opacity: 1
    rotation: 0
  }
}

// Define another keyframe
keyframe {
  time: 2s
  properties {
    position: { x: 100, y: 50 }
    scale: 2
    opacity: 0.5
    rotation: 180
  }
}

// Define an animation
animation {
  target: "myVideo"
  duration: 5s
  easing: "ease-in-out"
  keyframes: [
    // Reference the keyframes defined earlier
    @keyframe[0],
    @keyframe[1]
  ]
}

// Play the animation
play("myVideo", @animation)
```


```JavaScript
// TimeSeriesScript DSL for Time Series Analysis

// Load time series data from a file
load("data.csv")

// Define a moving average operation
moving_average {
  window_size: 5
  input: "data.csv"
  output: "ma.csv"
}

// Define a detrend operation
detrend {
  method: "linear"
  input: "data.csv"
  output: "detrended.csv"
}

// Define a difference operation
difference {
  lag: 1
  input: "data.csv"
  output: "differenced.csv"
}

// Define a forecasting operation
forecast {
  method: "ARIMA"
  input: "data.csv"
  output: "forecast.csv"
  parameters {
    order: [1, 0, 1]
  }
  horizon: 10
}

```



```JavaScript


// UIDesignScript DSL for User Interface Design

// Define a button component
component Button {
  text: "Click Me"
  position: { x: 100, y: 50 }
  size: { width: 150, height: 40 }
  color: "blue"
  on_click: {
    // Define the behavior when the button is clicked
    // ...
  }
}

// Define a text input component
component TextInput {
  position: { x: 100, y: 100 }
  size: { width: 200, height: 30 }
  placeholder: "Enter your name"
  on_change: {
    // Define the behavior when the input value changes
    // ...
  }
}

// Define a checkbox component
component Checkbox {
  label: "Remember me"
  position: { x: 100, y: 150 }
  checked: true
  on_change: {
    // Define the behavior when the checkbox state changes
    // ...
  }
}

// Define a label component
component Label {
  text: "Welcome to My App"
  position: { x: 100, y: 200 }
  font_size: 24
}

// Define a UI container
container MainContainer {
  size: { width: 400, height: 300 }
  background_color: "white"

  // Add components to the container
  add(Button)
  add(TextInput)
  add(Checkbox)
  add(Label)
}

// Render the UI
render(MainContainer)


```


```JavaScript
// MedicalDiagnosisScript DSL for Medical Diagnosis

// Define symptoms
symptom Fever
symptom Cough
symptom Fatigue
symptom Headache
symptom Rash

// Define medical conditions
condition CommonCold {
  symptoms: [Fever, Cough, Fatigue]
}

condition Influenza {
  symptoms: [Fever, Cough, Fatigue, Headache]
}

condition AllergicReaction {
  symptoms: [Rash]
}

condition Migraine {
  symptoms: [Headache]
}

// Define diagnostic rules
rule "Common Cold" {
  conditions: {
    CommonCold
  }
  diagnostic_result: "You have a common cold."
}

rule "Influenza" {
  conditions: {
    Influenza
  }
  diagnostic_result: "You have influenza."
}

rule "Allergic Reaction" {
  conditions: {
    AllergicReaction
  }
  diagnostic_result: "You are experiencing an allergic reaction."
}

rule "Migraine" {
  conditions: {
    Migraine
  }
  diagnostic_result: "You have a migraine."
}

// Define a patient with symptoms
patient John {
  symptoms: [Fever, Cough, Fatigue]
}

// Perform diagnosis for the patient
diagnose(John)

// Output the diagnostic result
print_diagnostic_result(John)

```

```JavaScript
// PersonalEmailAutomationScript DSL for Personal Email Automation

// Define an email template for a warm introduction
template WarmIntroEmail {
  subject: "Warm Introduction"
  body: "Dear {receiver_name},\n\nI hope this email finds you well. I wanted to introduce you to {contact_name}. {Contact_name} is an expert in {industry} and has extensive experience in {specific_field}. I believe you both would benefit from connecting and discussing {shared_interest}.\n\nBest regards,\n{your_name}"
}

// Define recipients
recipient John {
  name: "John Smith"
  email: "john@example.com"
}

recipient Jane {
  name: "Jane Doe"
  email: "jane@example.com"
}

// Send a warm introduction email from Jane to John
send_email(WarmIntroEmail, John, {
  your_name: "Jane Doe",
  receiver_name: "John Smith",
  contact_name: "Introducer's Name",
  industry: "Technology",
  specific_field: "Artificial Intelligence",
  shared_interest: "potential collaboration opportunities"
})

// Schedule a follow-up conversation with John in 3 days
schedule_meeting(John, 3 days)

// Define an email action
action SendFollowUp {
  execute: {
    // Define the behavior for the action
    // ...
  }
}

// Send a follow-up email to Jane
execute_action(SendFollowUp, Jane)

// Schedule a meeting with Jane for next week
schedule_meeting(Jane, 1 week)

```


```JavaScript
// WebAutomationScript DSL for Web Scraping and Interaction

// Define a web scraping rule
rule ArticleScraping {
  target_url: "https://example.com/articles"
  element: "div.article"
  fields {
    title: "h2.title"
    author: "span.author"
    content: "div.content"
  }
}

// Scrape articles using the defined rule
scrape(ArticleScraping)

// Perform web interaction to click a button
click_button {
  selector: "button.submit"
}

// Fill a form field with input
fill_form {
  selector: "input#name"
  value: "John Smith"
}

// Submit the form
submit_form

// Generate a summary of the web page content
summary {
  length: 3
}

// Define an action for saving data
action SaveData {
  execute: {
    // Define the behavior for saving data
    // ...
  }
}

// Execute the save data action
execute_action(SaveData)
```

```JavaScript
// MarketingAutomationScript DSL for Online Marketing

// Define a marketing campaign
campaign SummerSale {
  start_date: "2023-06-01"
  end_date: "2023-08-31"
  target_audience: "segment1"
}

// Define a target audience
audience segment1 {
  demographics {
    age: [25, 40]
    location: "United States"
    interests: ["outdoor activities", "travel"]
  }
}

// Define an advertising channel
channel FacebookAds {
  budget: 1000
  target_audience: "segment1"
}

// Run the Summer Sale campaign on Facebook Ads
run_campaign(SummerSale, FacebookAds)

// Define an email template
template PromotionEmail {
  subject: "Special Promotion for You"
  body: "Dear {name},\n\nWe are excited to offer you a special promotion on our products. Don't miss out on this opportunity. Visit our website and use the code {promo_code} to avail yourself of the discount.\n\nBest regards,\nThe Marketing Team"
}

// Send a promotional email to the target audience
send_email(PromotionEmail, "segment1", {
  promo_code: "SUMMER20"
})

// Define a social media post
post SocialMediaPost {
  platform: "Twitter"
  content: "Exciting news! Our Summer Sale is now live. Visit our website and enjoy up to 50% off on selected items. #SummerSale #Discounts"
}

// Publish the social media post
publish(SocialMediaPost)

```