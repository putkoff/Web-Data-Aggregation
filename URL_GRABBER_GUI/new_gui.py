from net_tools import *
from dynamic_gui import expandable,get_gui_fun,get_thread,start_thread,verify_thread,thread_alive
import PySimpleGUI as sg
def get_url_frame(key, type: str = "Text",layout=[]):
     """
    Function to generate a GUI frame for a URL with an associated key and type.

    Args:
    key: The key associated with the URL.
    type: The type of GUI element to generate. Default is 'Text'.
    layout: Optional layout list to specify GUI component layout. 

    Returns:
    A GUI Frame with the specified properties.
     """
     layout_component = [get_gui_fun(type, {'text': key, "key": f"-URL_{key}-", "enable_events": True})]
     if len(layout) >0:
        layout=list(layout)
        for each in layout:
            layout_component.append(each)
     return get_gui_fun('Frame', {'title': key, 'layout': [layout_component]})
def get_url_input_frame():
    """
    Function to generate a GUI frame for URL input.

    Returns:
    A GUI frame with input fields and buttons for URL manipulation.
    """
    return [mk_component([], [
            get_gui_fun('Frame', {'title': "INPUT", 'layout': [[get_gui_fun('Input', {"default":'www.example.com', "key": '-URL_INPUT-', "enable_events": True})]]}),
            get_url_frame('FORMATTED'),
            get_url_frame('URL'),
            get_url_frame('STATUS'),
            get_url_frame('WARNING'),
        ]),get_gui_fun('Frame', {'title': "SITE_MAP", 'layout': [[get_gui_fun('Listbox',{"values":[],"key":"-URL_LIST-", "enable_events": True, **expandable()}),sg.Button('USE URL')]], **expandable()})]

def combine_all_for_vert(ls):
    """
    Function to combine all elements of a list vertically in a new GUI component.

    Args:
    ls: The list of GUI components to be combined.

    Returns:
    A new GUI component containing all original elements combined vertically.
    """
    new_component,ls =list(list(ls)[0]), list(ls)[1:]
    for each in ls:
        each = list(each)
        for part in each:
            new_component.append(part)
    return new_component
def get_check_frame(key):
    """
    Function to generate a GUI frame for a checkbox and combo box with an associated key.

    Args:
    key: The key associated with the checkbox and combo box.

    Returns:
    A GUI Frame with a checkbox and combo box.
    """
    return [get_gui_fun('Frame', {'title': key,"layout":[[get_gui_fun('Checkbox', {'text': '', "default": False, "key": f'-CHECK_{key}-', "enable_events": True}),
            get_gui_fun('Combo', {"values": [], "size": (15, 1), "key": f'-SOUP_{key}-', "enable_events": True})]]})]
def get_find_soup_frame():
    """
    Function to generate a GUI frame for finding soup elements.

    Returns:
    A GUI Frame with checkboxes for different soup element types and a multiline output area.
    """
    check_frames = [
        get_check_frame('TAG'),
        get_check_frame('ELEMENT'),
        get_check_frame('TYPE'),
        get_check_frame('CLASS'),
        [
        sg.Button('all soup')
    ]
    ]
    check_frames_layout = combine_all_for_vert(check_frames)
    return [get_gui_fun('Frame', {'title': 'find soup', 'layout': [check_frames_layout,get_multi_line({"key": "-FIND_ALL_OUTPUT-"})], **expandable()})]
def get_source_layout():
    """
    Function to generate the main source layout for the GUI.

    Returns:
    A list of GUI components representing the main source layout.
    """
    layout = [
        get_url_input_frame(),
        get_find_soup_frame()
        ]
def mk_component(ls, component_ls):
    """
    Function to append components from a list to another list.

    Args:
    ls: The list to append components to.
    component_ls: The list of components to append.

    Returns:
    The modified list with appended components.
    """
    for k in range(0, len(component_ls)):
        ls.append(component_ls[k])
    return ls
def update_status(window,js):
    """
    Function to update the status of a GUI window.

    Args:
    window: The GUI window to update.
    js: The status values to update.
    """
    for k in range(0,len(list(js.keys()))):

        window[list(js.keys())[k]].update(value=js[list(js.keys())[k]])
def fetch_url(window, url, user_agent):
    """
    Function to fetch a URL with specified user agent.

    Args:
    window: The GUI window to update.
    url: The URL to fetch.
    user_agent: The user agent to use when fetching the URL.
    """
    try:
        r = requests.get(url, headers={'User-Agent': user_agent})
        js_valid = {"-URL_FORMATTED-": url, "-URL_WARNING-": 'valid', "-URL_STATUS-": r.status_code, '-URL_URL-': True}
        window['-URL_LIST-'].update(values=break_set(get_all_website_links(url)))
    except:
        js_valid = {"-URL_FORMATTED-": url, "-URL_WARNING-": 'invalid', "-URL_STATUS-": 'fail', '-URL_URL-': False}
    update_status(window, js_valid)
import threading
def break_set(obj):
    """
    Function to convert a set object into a list.

    Args:
    obj: The set to convert.

    Returns:
    A list containing the elements of the original set.
    """
    ls=[]
    for item in obj:
        ls.append(item)
    return ls
def debounce(wait):
    """
    Decorator that postpones a function's execution until after 'wait' seconds have elapsed since the last time it was invoked.

    Args:
    wait: The wait time in seconds.
    """
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
            if hasattr(debounced, '_timer'):
                debounced._timer.cancel()
            debounced._timer = threading.Timer(wait, call_it)
            debounced._timer.start()
        return debounced
    return decorator
@debounce(0.5)  # wait half a second after the last call to run the function
def handle_url_input(window, values):
    """
    Function to handle URL input events.

    Args:
    window: The GUI window to update.
    values: The dictionary of GUI values.
    """
    url = format_url(values['-URL_INPUT-'])
    if url == None:
        url = ''
    try:
        r = requests.get(url)
        js_valid = {"-URL_FORMATTED-":url,"-URL_WARNING-":'valid','-URL_STATUS-':r.status_code,'-URL_URL-':True}
        window['-URL_LIST-'].update(values=break_set(get_all_website_links(url)))
    except:
        js_valid = {"-URL_FORMATTED-":url,"-URL_WARNING-":'invalid','-URL_STATUS-':'fail','-URL_URL-':False}
    update_status(window,js_valid)     
def sources_frames():
    """
    Function to generate a GUI frame for source code and React source.

    Returns:
    A list of GUI frames for source code and React source.
    """
    return [get_gui_fun('Frame', {'title': "SOURCE_CODE", 'layout': [[get_gui_fun('Multiline',{"values":[],"key":"-SOURCE_CODE-", **expandable()})]], **expandable()}),
    get_gui_fun('Frame', {'title': "REACT_SOURCE", 'layout': [[get_gui_fun('Multiline',{"values":[],"key":"-REACT_SOURCE-", **expandable()})], [sg.Slider(range=(0, 1), default_value=0, size=(50, 10), orientation="h", enable_events=True, key="slider")]], **expandable()})]

# In your event loop

def while_source_top(window, event, values):
    """
    Function to handle events in the source code top window.

    Args:
    window: The GUI window to update.
    event: The triggered event.
    values: The dictionary of GUI values.
    """
    tls_adapter_instance = TLSAdapter()
    if 'CHECK_' in event:
            if values[event] == True:
                globals()['curr_check'] = event.split('CHECK_')[1]
                keys = list(values.keys())
                for k in range(0, len(keys)):
                    key = keys[k]
                    if 'CHECK_' in key and key != event:
                        window[key].update(value=False)
                if event == 'all soup':
                    window['-FIND_ALL_OUTPUT-'].update(value=find_all_soup(values[f'-SOUP_{globals()["curr_check"]}']))
                if event == 'get soup':
                    window['-FIND_ALL_OUTPUT-'].update(value=all_soup(values['-SOUP_OUTPUT-'], values['-SOUP_TAG-'], values['-SOUP_TYPE-'], values['-SOUP_CLASS-'], values['-SOUP_INPUT-']))
    if event == '-URL_INPUT-':
        handle_url_input(window, values)
    if event == 'formatted url':
        window['-URL_INPUT-'].update(value=format_url(values['-URL_INPUT-']))
    # Now you can call the get_ciphers() method on the instance
    if event in tls_adapter_instance.get_ciphers():
        # Do something
        pass
        ls = []
        for k in range(len(TLSAdapter.get_ciphers())):
            if values[TLSAdapter.get_ciphers()[k]] == True:
                ls.append(TLSAdapter.get_ciphers()[k])
        window['-CIPHERS_OUTPUT-'].update(value=create_ciphers_string(ls=ls))
    if event == '-PARSER-':
        display_soup(window, event, values)
    if event == '-BS4_PARSER-':
        while_action(window, event, values)
def while_site_map(window, event, values):
    """
    Function to handle events in the site map window.

    Args:
    window: The GUI window to update.
    event: The triggered event.
    values: The dictionary of GUI values.
    """
    if "USE URL" in event:
        parsed_html = get_parsed_html(url=values["-URL_LIST-"][0])
        window["-SOURCE_CODE-"].update(value=parsed_html)
        react_source = parse_react_source(parsed_html)
        # Initialize the slider with the number of react sources
        window["slider"].update(range=(0, len(react_source) - 1))
        # Display the first source by default
        if len(react_source)>0:
            window["-REACT_SOURCE-"].update(value=react_source[0])
    elif event == "slider":  # Event when slider value changes
        # Use the slider value as an index to select a react source
        window["-REACT_SOURCE-"].update(value=parse_react_source(values["-SOURCE_CODE-"])[int(values["slider"])])

def url_grabber_component():
    """
    Function to initialize the URL Grabber GUI and handle its events.

    Returns:
    A GUI window with a URL Grabber interface.
    """
    layout = [get_url_input_frame(),[sources_frames()]]
    window = get_gui_fun(name='Window', args={'title': 'URL Grabber', 'layout': layout, **expandable()})
    while True:
        event, values = window.read()
        while_source_top(window, event, values)
        while_site_map(window, event, values)
        if event == sg.WINDOW_CLOSED:
            break
            window.close()
def get_multi_line(args):
    """
    Function to generate a multiline GUI element.

    Args:
    args: The arguments to use when generating the multiline element.

    Returns:
    A multiline GUI element with the specified properties.
    """
    return [get_gui_fun('Multiline', {**args, **expandable()})]
url_grabber_component()
