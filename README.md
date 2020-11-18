# LightStage

LightStage is a simple, portable lighting tool to efficiently generate a large dataset of lighting on a face using just the webcam.

### Draw shapes
1. To draw shapes on the canvas, **click and drag** to create a shape.
    - Press **R** key for rectangle, and **C** key for circle/oval
    - **Right click** over shape to change its color or delete it

### Run Sequence
2. To run a sequence of lights, **right click** on an empty space and select **Sequence**
    - Choose number of rows and columns (suggested 2-10)
    - Choose number of milliseconds each should appear (suggested 100 - 1000 ms)
    - Choose color of rectangle
    - Update rectangle to view its true size

### Gradient
3. To show a gradient, **right click** on an empty space and select **Gradient**
    - Choose two colors and orientation
    - **Right click** over gradient to delete it
    
### Config Files
4. To import a configuration file, **right click** on an empty space and select **Import Config**
  - Config File Format:
   - **For shapes:**
      - [Shape] [X_start] [Y_start] [X_end] [Y_end] [Color] [Start_time] [End_time]
      - **Shape:** R for rectangle, C for circle
      - **X_start, Y_start, X_end, Y_end:** starting and ending coordinates
      - **Color:** Color of shape
      - **Start_time, End_time:** (Optional) If no end time specified, then shape will not be deleted
      
   - **For gradients:**
      - G [color1] [color2] [Orientation] [Start_time] [End_time]
      - **color1, color2:** 2 colors for gradient
      - **Start_time, End_time:** (Optional) If no end time specified, then shape will not be deleted
