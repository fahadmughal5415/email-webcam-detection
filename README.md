# Email Webcam Detection

This project captures an image using a webcam and sends it via email when a new customer shows up.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/fahadmughal5415/email-webcam-detection
    cd email-webcam-detection
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - `EMAIL`: Your email address (sender and receiver).
    - `PASSWORD`: Your email account password.

    You can set these variables in your terminal or create a `.env` file in the project directory:
    ```sh
    EMAIL=your-email@gmail.com
    PASSWORD=your-password
    ```

4. Ensure less secure app access is enabled for your Gmail account:
    - Go to your Google Account.
    - Select Security.
    - Under "Less secure app access," turn on "Allow less secure apps."

## Usage

Run the script to capture an image and send it via email:
```sh
python emailing.py
```

## Troubleshooting

- If you encounter an `SMTPAuthenticationError`, ensure that your email and password are correct and that less secure app access is enabled.
- If you see an error related to environment variables, make sure `EMAIL` and `PASSWORD` are set correctly.

## License

This project is licensed under the MIT License.

