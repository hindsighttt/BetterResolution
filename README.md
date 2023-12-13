# Better Resolution - Blender Extension

This Blender extension allows users to set the resolution of their renders in millimeters, offering a more intuitive way for those used to working with physical print sizes.

## Features

- Set the width and height of the render resolution in millimeters.
- Define the dots per inch (DPI) for the render output.
- Real-time conversion of millimeters to pixels based on the DPI value.
- Intuitive user interface integrated into the Output Properties panel.

## Installation

To install this extension, follow these steps:

1. Download the script file for the "Better Resolution" extension.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click `Install` and navigate to the downloaded script file.
4. Select the script and click `Install Add-on`.
5. Enable the add-on by ticking the checkbox next to its name.

## Usage

After installing the extension, you can access the "Better Resolution" settings in the Output Properties panel within Blender.

1. Navigate to the `Output Properties` tab.
2. Locate the `Better Resolution` panel.
3. Adjust the `Width in mm`, `Height in mm`, and `DPI` properties as needed.
4. The pixel resolution of the render will update automatically.

## Prerequisites

This extension requires Blender 3.0.0 or higher.

## Customization

The default values are set to an A4 paper size at 300 DPI, but you can easily modify the `default_x`, `default_y`, and `default_dpi` variables within the script to suit your preferences.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. If you find a bug or have a feature request, please open an issue.

## Authors

- Hindsight - Initial work

## Acknowledgments

- Blender Community - For providing an excellent platform for 3D modeling and rendering.
