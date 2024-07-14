import cv2
import numpy as np
import matplotlib.pyplot as plt
GRID_RESOLUTION = 0.1  # meters per grid cell
GRID_WIDTH = 30  # number of grid cells in width
GRID_HEIGHT = 30  # number of grid cells in height

# Initialize the occupancy grid
occupancy_grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=np.uint8)
def update_grid(x, y, width, height):
    global occupancy_grid
    
    # Convert detected object location to grid cells
    grid_x = int(x / GRID_RESOLUTION)
    grid_y = int(y / GRID_RESOLUTION)

    # Update grid cells around the detected object
    for i in range(max(0, grid_x - 1), min(GRID_WIDTH, grid_x + 2)):
        for j in range(max(0, grid_y - 1), min(GRID_HEIGHT, grid_y + 2)):
            occupancy_grid[i, j] = 255  # Mark cell as occupied
def process_image(frame):
    global occupancy_grid
    
    # Example: Convert to grayscale and apply a simple threshold
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours of objects
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Update grid based on detected objects
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        update_grid(x + w / 2, y + h / 2, w, h)
def main():
    cap = cv2.VideoCapture(0)  # Open camera (adjust index as needed)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        process_image(frame)

        # Display occupancy grid (for visualization)
        plt.figure(figsize=(8, 6))
        plt.imshow(occupancy_grid, cmap='gray', origin='lower', extent=(0, GRID_WIDTH * GRID_RESOLUTION, 0, GRID_HEIGHT * GRID_RESOLUTION))
        plt.title('Occupancy Grid Map')
        plt.xlabel('Width (m)')
        plt.ylabel('Height (m)')
        plt.colorbar(label='Occupancy')
        plt.grid(True)
        plt.pause(0.01)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if _name_ == '_main_':
    main()
