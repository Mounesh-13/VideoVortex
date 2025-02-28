# VideoVortex - Multi-Platform Media Downloader

VideoVortex is a web application built with Flask and `yt-dlp` that allows users to download videos from YouTube, Instagram, and Twitter. It provides a simple and intuitive interface for seamless media downloading.

## Features

* **Multi-Platform Support:** Download videos from YouTube, Instagram, and Twitter.
* **Best Quality Download:** Automatically downloads the highest available quality for each platform.
* **User-Friendly Interface:** Clean and intuitive web interface for easy navigation.
* **Efficient Downloading:** Utilizes `yt-dlp` for fast and reliable downloads.

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/your-username/VideoVortex.git](https://www.google.com/search?q=https://github.com/your-username/VideoVortex.git)
    cd VideoVortex
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    * **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    * **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Install FFmpeg:**

    * FFmpeg is required for `yt-dlp` to function correctly.
    * Download and install FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
    * Add the FFmpeg `bin` directory to your system's PATH environment variable.

6.  **Run the Application:**

    ```bash
    python app.py
    ```

7.  **Access the Application:**

    * Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1.  **Enter URL:** Paste the URL of the video you want to download from YouTube, Instagram, or Twitter into the input field.
2.  **Download:** Click the "Download" button.
3.  **Download Location:** The downloaded video will be saved in the `downloads` directory within the project folder.

## Dependencies

* Flask
* yt-dlp
