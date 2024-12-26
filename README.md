
# **Unit Converter Using Tkinter**

This is a **Python-based Unit Converter application** created using the **Tkinter** library. It provides an intuitive graphical user interface (GUI) for converting measurements of weight, volume, length, and time into various units.

## **Features**

- **Weight Conversion:**
  - Input weight in kilograms.
  - Convert to grams, pounds, and ounces.

- **Volume Conversion:**
  - Input volume in liters.
  - Convert to milliliters, cubic meters, and gallons.

- **Length Conversion:**
  - Input length in meters.
  - Convert to centimeters, inches, and feet.

- **Time Conversion:**
  - Input time in hours.
  - Convert to minutes, seconds, and milliseconds.

## **Requirements**

- Python 3.x
- Tkinter (pre-installed with Python)

## **How to Run**

1. Clone or download the repository.
2. Open a terminal/command prompt and navigate to the project directory.
3. Run the following command:

   ```bash
   python unit_converter.py
   ```

4. The application window will launch with an intuitive interface for performing conversions.

## **Usage**

1. **Input a value** in the designated entry field.
2. Click the **"Convert"** button next to the field.
3. View the converted results in the corresponding text boxes.

## **Code Structure**

- **Tkinter Layout:** Organizes the GUI into rows and columns using the `grid()` method.
- **Conversion Functions:**
  - `from_kg()`: Converts weight.
  - `from_L()`: Converts volume.
  - `from_m()`: Converts length.
  - `from_hr()`: Converts time.
- **Interactive Widgets:**
  - Labels, Entry fields, Buttons, and Text widgets are utilized for a seamless user experience.

## **Customization**

You can extend this application by:
- Adding more units for conversion.
- Styling the GUI for a modern look using libraries like `ttk` or `ttkbootstrap`.

## **Contributing**

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Enjoy using the **Unit Converter**! 😊
