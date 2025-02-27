# 🎬 Crisis Management Workflow with DeepSeek and LangChain

## 🚀 Business Scenario

In today’s fast-paced world, companies often face crises that require immediate and professional communication to maintain trust with stakeholders. This project leverages DeepSeek (via OpenRouter API) and LangChain to automate the generation of two critical press statements:

- **Crisis Management Statement**: A professional acknowledgment of the crisis, reassurance to stakeholders, and an outline of steps being taken to resolve the issue.
- **Legally Safe Press Statement**: A refined version of the initial statement, edited by a legal expert to avoid admissions of fault or liability while maintaining professionalism.

This workflow is designed to assist:

- **Corporate Communications Teams**: To quickly draft and refine press statements during crises.
- **Legal Teams**: To ensure statements are legally compliant and protect the company from liability.
- **Executives**: To maintain trust and transparency with customers, stakeholders, and the public.

## 🧠 Business Problem

During a crisis, companies often struggle to:

1. **Respond quickly**: Delays in communication can damage reputation and trust.
2. **Maintain professionalism**: Crafting a well-worded statement under pressure is challenging.
3. **Avoid legal risks**: Statements must be carefully reviewed to prevent admissions of fault or liability.

By automating this process, we can:

- **Accelerate response times**: Generate professional statements in seconds.
- **Ensure consistency**: Provide clear, concise, and legally safe communication.
- **Reduce human error**: Minimize the risk of poorly worded or legally risky statements.

## 🛠️ Solution Approach

This project uses LangChain to orchestrate a multi-agent workflow, where:

- A **Crisis Management Expert** drafts an initial press statement.
- A **Legal Expert** refines the statement to ensure it is legally safe.

### Below are the key steps involved:

1. **User Input**: The user describes the crisis scenario in a text box.
2. **Crisis Management Statement**: A prompt is sent to the DeepSeek model (via OpenRouter API) to generate a professional press statement. The statement acknowledges the issue, reassures stakeholders, and outlines steps being taken to resolve the crisis.
3. **Legal-Safe Press Statement**: The initial statement is reviewed by a Legal Expert (another DeepSeek model call). The legal expert edits the statement to:
   - Deny direct culpability.
   - Remove language that could put the company in legal liability.
   - Add notes explaining the changes made.
4. **Output**: Both statements are displayed to the user. The statements are also saved to a JSON file for future reference.

## 📊 Workflow Overview

| Step                         | Description                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| **User Input**               | User describes the crisis scenario in a text box.               |
| **Crisis Management Expert** | Generates a professional press statement addressing the crisis. |
| **Legal Expert**             | Refines the statement to ensure it is legally safe.             |
| **Output**                   | Displays both statements and saves them to a JSON file.         |

## 🔖 Key Features

- **Multi-Agent Workflow**: Combines the expertise of a crisis management expert and a legal expert.
- **Real-Time Generation**: Produces professional and legally safe statements in seconds.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Error Handling**: Includes retries and error messages for API failures.

## ⚠️ Limitations

1. **API Dependencies**: The app relies on the OpenRouter API, which may have rate limits or downtime.
2. **Model Limitations**: The quality of the statements depends on the capabilities of the DeepSeek model.
3. **Legal Compliance**: While the legal expert refines the statement, it should still be reviewed by a human legal professional for critical cases.

## 🔄 Key Skills Demonstrated

- 🔹 Multi-Agent Workflow Design
- 🔹 API Integration with OpenRouter
- 🔹 Streamlit App Development
- 🔹 Error Handling and Retry Logic
- 🔹 Prompt Engineering for LLMs

## 🛠️ Technical Tools & Libraries

- **Python**: Core programming language.
- **Streamlit**: For building the interactive web app.
- **OpenRouter API**: To access the DeepSeek model.
- **LangChain**: For orchestrating the multi-agent workflow.
- **Requests**: For making API calls.
- **JSON**: For saving the output to a file.

## 🚀 Final Thoughts

This project demonstrates how AI-powered workflows can streamline crisis communication, enabling companies to respond quickly and professionally while minimizing legal risks. With further refinement and integration into corporate systems, this tool can become a valuable asset for crisis management teams.
