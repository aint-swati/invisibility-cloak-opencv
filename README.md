# 🪄 Invisibility Cloak using Python & OpenCV

## Project Overview
This project implements an invisibility cloak effect inspired by the Harry Potter universe using Python and Computer Vision.  
By detecting a specific colored cloth in real-time video, the system replaces that region with the background, creating the illusion of invisibility.

## How It Works
- The webcam captures the background frame when no person is present.
- A predefined cloak color is detected in the live video feed.
- The detected area is masked and replaced with the stored background.
- This creates a real-time invisibility effect.

## Technologies Used
- Python
- OpenCV (cv2)
- NumPy

## Project Structure
Invisibility-Cloak/
├── invisibility_cloak.py
└── README.md

## Installation & Setup
1. Clone the repository
2. Install dependencies
   pip install opencv-python numpy
3. Run the project

## Learning Outcomes
- Basics of computer vision
- Color detection using HSV
- Image masking and background replacement
- Real-time video processing

## Usage Instructions
- Use a plain solid-colored cloth (here it is done for red).
- Ensure proper lighting for better detection.
- Stay out of the frame while the background is being captured.
- Cover yourself with the cloth to see the invisibility effect.

##Screenshots
<img width="1912" height="762" alt="Screenshot 2026-01-29 171952" src="https://github.com/user-attachments/assets/8ce1c51c-8789-4f4c-b86c-c7334e548398" />
<img width="1917" height="762" alt="Screenshot 2026-01-29 171941" src="https://github.com/user-attachments/assets/2f99048f-eea5-4ff4-a9fb-915306442a8d" />

![Cloak Demo](https://github.com/user-attachments/assets/5fe857ec-d632-466b-a110-b1eb91210c6c)
