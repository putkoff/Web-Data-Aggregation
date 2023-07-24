---
# URL Grabber GUI

URL Grabber is a dynamic Python-based GUI application that provides utilities for URL manipulation and content extraction from webpages. It utilizes the power of PySimpleGUI and BeautifulSoup to offer a user-friendly interface for these tasks. 
![Screenshot 2023-07-24 091028](https://github.com/putkoff/Web-Data-Aggregation/assets/57512254/c168e757-4631-46e2-b17a-c12cf658a170)
## Features

1. **URL Input**: This section of the GUI allows users to input a URL, which is then validated and processed.

2. **Site Map**: This part displays all the website links found within the provided URL. You can choose a specific URL from the site map for further analysis.

3. **Source Code Viewer**: Allows viewing the source code of the provided URL. It has two parts, "SOURCE_CODE" and "REACT_SOURCE". It also features a slider that helps users to navigate through the react sources (if any).

4. **Find Soup**: This section lets you extract specific elements from the website's HTML soup. You can select elements by tag, class, or type. The result will be shown in the multiline output area.

## Getting Started

### Prerequisites

The application depends on several Python packages. You can install them using pip:

```bash
pip install PySimpleGUI requests BeautifulSoup4
```

### Running the Script

You can start the application by running the script:

```bash
python3 main.py
```

Replace `main.py` with the actual name of your script.

## Usage

To use URL Grabber:

1. Enter a URL in the URL Input field and press Enter. The application will fetch the URL and display its status.
2. The site map will populate with all the links found on the webpage. You can select a specific link for further analysis.
3. The source code and react source (if any) of the selected URL will be shown in the Source Code Viewer.
4. In the Find Soup section, you can select elements by tag, class, or type. The results will be shown in the multiline output area.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the terms of the MIT license.

---
