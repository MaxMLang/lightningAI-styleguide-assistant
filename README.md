# Lightning ⚡️ AI Style Guide Assistant

<p align="center">
  <img src="assets/logo.png" alt="AI Style Guide Assistant Logo" width="200" height="200">
</p>

[![GitHub Stars](https://img.shields.io/github/stars/MaxMLang/lightningAI-styleguide-assistant?style=social)](https://github.com/MaxMLang/lightningAI-styleguide-assistant/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/MaxMLang/lightningAI-styleguide-assistant)](https://github.com/MaxMLang/lightningAI-styleguide-assistant/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/MaxMLang/lightningAI-styleguide-assistant)](https://github.com/MaxMLang/lightningAI-styleguide-assistant/pulls)
[![License](https://img.shields.io/github/license/MaxMLang/lightningAI-styleguide-assistant)](https://github.com/MaxMLang/lightningAI-styleguide-assistant/blob/main/LICENSE)

The Lightning ⚡️ AI Style Guide Assistant is a specialized adaptation of the [Lightning Chatbot](https://github.com/MaxMLang/lightningfast-ai-chat), designed to assist in maintaining consistency and accuracy in style guides. Leveraging Groq LPUs, it provides real-time style and grammar recommendations, making it an essential tool for editors and writers. This AI-powered assistant enhances productivity by automating the enforcement of writing standards and style consistency.

## Features

- ⚡ Real-time style and grammar recommendations powered by Groq LPUs.
- 📘 Supports custom style guide integration for personalized recommendations.
- 💬 Interactive editing experience with instant feedback.
- 🌐 Deploy easily using the Streamlit web framework.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/MaxMLang/lightningAI-styleguide-assistant.git
   ```
2. Navigate to the project directory:
   ```
   cd lightningAI-styleguide-assistant
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Configure the Groq API key:
   - Create a `.env` file in the project directory.
   - Add the following line, replacing `your_api_key` with your actual Groq API key:
     ```
     GROQ_API_KEY=your_api_key
     ```

5. Launch the assistant:
   ```
   streamlit run app.py
   ```

6. Open the provided URL in your browser to access the AI Style Guide Assistant interface.

## Usage

1. Select your custom style guide settings from the sidebar.
2. Type a block of text into the input field and submit.
3. Receive style and grammar recommendations based on your settings.
4. Apply or dismiss suggestions and see the edits in real-time.
5. Continue refining your text with further input and revisions.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Groq](https://groq.com) for the cutting-edge LPUs.
- [Langchain](https://github.com/hwchase17/langchain) for robust language modeling tools.
- [Streamlit](https://streamlit.io) for the user-friendly web application framework.

