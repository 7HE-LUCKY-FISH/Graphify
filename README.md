# Graphify

The project, uses the Spotify API to analyze a user's listening history and generate a Markov chain model of their genre preferences. This model is then visualized as a directed graph, showing the transitions between genres.

### V2

![Figure_1](https://github.com/user-attachments/assets/15b5527e-d1d0-4425-b6ef-c01aeb2652fc)


### V1
![Figure_1](https://github.com/user-attachments/assets/7d5d7e39-bcb1-496c-a90f-19691cb20a1e)



## Setup and Run Instructions

To get Graphify up and running, follow these steps:

### 1. Obtain Spotify API Credentials

*   Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.
*   Create a new app.
*   Take note of the **Client ID** and **Client Secret**. You'll need these later.
*   In your app settings, add `http://127.0.0.1:8000/callback` to the **Redirect URIs**.

### 2. Configure Environment Variables

*   Create a `.env` file in the root directory of the project.
*   Add the following lines to your `.env` file, replacing the placeholders with your actual credentials:

    ```
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    REDIRECT_URI=http://127.0.0.1:8000/callback
    ```

### 3. Install Dependencies

*   Make sure you have Python 3.6 or higher installed.
*   Open your terminal or command prompt and navigate to the project directory.
*   Run the following command to install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### 4. Run the Program

*   In your terminal or command prompt, run the following command:

    ```bash
    python main.py
    ```

*   Your browser will automatically open and prompt you to authorize the application to access your Spotify data.
*   After authorization, the program will analyze your listening history, generate the Markov chain model, and display the visualized graph.
