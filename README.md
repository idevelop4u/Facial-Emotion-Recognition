Installation & Setup

    Clone the repository:
    Bash


Install dependencies: It is recommended to use a virtual environment.
Bash

    pip install -r requirements.txt

    Verify Assets: Ensure the haarcascade_frontalface_default.xml file is present in the assets/ folder. If not, it can be downloaded from the official OpenCV repository.

How to Run

Execute the main script from the project root directory:
Bash

python main.py

The webcam will activate. Press 'q' on your keyboard to stop the video feed and close the application.

Testing Instructions

To verify the system functionality:

    Run the application in a well-lit room.

    Face the camera directly.

    Perform different facial expressions (smile, frown, look surprised).

    Verify that the text label above the bounding box changes to match your expression.

    Wait for 60 seconds and check the captured_faces/ folder to verify that a snapshot has been saved automatically.

Future Enhancements

    Integration with a web interface using Flask or Streamlit.

    Multi-face tracking with unique ID assignment.

    graphical dashboard to visualize emotion trends over time.
