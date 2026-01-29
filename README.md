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

##Demo

![Cloak Demo]<img width="1912" height="762" alt="Screenshot 2026-01-29 171952" src="https://github.com/user-attachments/assets/e0545880-41ac-4644-ad77-b2f027fd89d9" />
<img width="1917" height="762" alt="Screenshot 2026-01-29 171941" src="https://github.com/user-attachments/assets/ae448091-a4ed-4ee6-976a-ed807e3b7740" />
(https://github.com/user-attachments/assets/5fe857ec-d632-466b-a110-b1eb91210c6c)
