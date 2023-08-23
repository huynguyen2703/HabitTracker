from tkinter import *
from tkinter import ttk
import simpleaudio
from datetime import datetime
from registration import Registration
from graph import Graph
from pixel import Pixel

# Define constants for background color and word color
BG = '#B200ED'
WORD_COLOR = '#FFD700'
initial_hour = '0'

# Get the current date and time in UTC
today = datetime.now().utcnow()
print(today.strftime('%Y%m%d'))

# Create instances of Registration, Graph
account = Registration()
the_graph = Graph()

# Register the user
account.register()

# Create a graph for tracking coding hours
the_graph.create_graph()


def call_add():
    """
    Callback function for the 'Add' button.
    Adds coding hours for the current date or the date specified in the input field.
    """
    play_sound('/Users/nguyenquoctoan/PycharmProjects/PasswordGenerator/button.wav')
    if user_entry.get() != '':
        the_pixel = Pixel(today, user_entry.get())
    else:
        the_pixel = Pixel(today, initial_hour)
    the_pixel.create_pixel()
    label_text.config(text=f'Today You Have Coded For {user_entry.get()} Hours')


def call_delete():
    """
    Callback function for the 'Delete' button.
    Deletes coding hours for the specified date.
    """
    play_sound('/Users/nguyenquoctoan/PycharmProjects/PasswordGenerator/button.wav')
    if user_entry.get() != '':
        the_pixel = Pixel(today, user_entry.get())
    else:
        the_pixel = Pixel(today, initial_hour)
    date_str = date.get()
    try:
        date_obj = datetime.strptime(date_str, '%Y%m%d')
    except ValueError:
        print("Invalid date format. Please enter a date in 'yyyymmdd' format.")
        return
    the_pixel.delete_pixel(date_obj)

    if date.get() == today.strftime('%Y%m%d'):
        label_text.config(text=f'Today You Have Coded For 0 Hours')


def call_update():
    """
    Callback function for the 'Update' button.
    Updates coding hours for the specified date.
    """
    play_sound('/Users/nguyenquoctoan/PycharmProjects/PasswordGenerator/button.wav')
    if user_entry.get() != '':
        the_pixel = Pixel(today, user_entry.get())
    else:
        the_pixel = Pixel(today, initial_hour)
    date_str = date.get()
    try:
        date_obj = datetime.strptime(date_str, '%Y%m%d')
    except ValueError:
        print("Invalid date format. Please enter a date in 'yyyymmdd' format.")
        return

    the_pixel.update_pixel(date_obj, {'quantity': user_entry.get()})

    if date.get() == today.strftime('%Y%m%d'):
        label_text.config(text=f'Today You Have Coded For {user_entry.get()} Hours')


def play_sound(filename):
    """
    Play an audio file using the simpleaudio library.

    This function takes a `filename` parameter representing the path to an audio file
    and uses the simpleaudio library to play the sound.

    Parameters:
        filename (str): The path to the audio file to be played.

    Raises:
        FileNotFoundError: If the specified audio file is not found.

    Returns:
        None.
    """
    try:
        # The WaveObject represents the audio file specified by the filename.
        # It is responsible for playing the sound.
        wave_obj = simpleaudio.WaveObject.from_wave_file(filename)
        wave_obj.play()
    except FileNotFoundError as e:
        print(f"Sound file not found: {e}")
    except Exception as e:
        print(f"Error while playing sound: {e}")


# Create the main Tkinter window
window = Tk()
window.title("Coding Tracker")  # Set the window title
window.config(padx=40, pady=40, bg=BG)  # Configure padding and background color

# Create a ttk Style object for custom styling of Tkinter widgets
style = ttk.Style()

# Configure a style for buttons with no focus color, no border, and white foreground text
style.configure("NoFocus.TButton", focuscolor="none", borderwidth=0, foreground='white')

# Set the default theme for styling
style.theme_use('default')

# Map the 'elder.TButton' style to change the background color to gold when the button is active (pressed)
style.map('elder.TButton', background=[('active', 'gold')])

# The main Tkinter GUI window is now configured and styled


# Create a canvas for displaying an image
canvas = Canvas(width=300, height=250, highlightthickness=0, bg=BG)

# Load and display an image on the canvas
background_pic = PhotoImage(file='/Users/nguyenquoctoan/PycharmProjects/HabitTracker/coding.png')
coding_pic = canvas.create_image(150, 100, image=background_pic)

# Position the canvas in the Tkinter window
canvas.grid(column=1, row=1)

# Create a label for displaying coding hours
label_text = Label(text='Today You Have Coded For 0 Hours', fg=WORD_COLOR, bg=BG, font=('Courier', 25, 'bold'))
label_text.grid(column=1, row=0)

# Create labels for user input
label_day = Label(text='Enter Date Here', fg=WORD_COLOR, bg=BG, font=('Courier', 17, 'bold'))
label_day.grid(column=0, row=2, pady=20, sticky='e')

label_hour = Label(text='Enter Hour\n\n⬇', fg=WORD_COLOR, bg=BG, font=('Courier', 17, 'bold'))
label_hour.grid(column=2, row=1, sticky='s')

# Create an entry field for date input
date = Entry(width=25, bg='white', fg='black', font=("Playfair Display", 15, "bold"))
date.insert(string='YYYYmmdd', index=0)
date.focus_set()
date.grid(column=0, row=2, pady=20, columnspan=3)

# Create an entry field for coding hour input
user_entry = Entry(width=10, bg='white', fg='black', font=("Playfair Display", 15, "bold"))
user_entry.insert(string='', index=0)
user_entry.grid(column=2, row=2)

# Create buttons for Add, Update, and Delete operations
add_button = ttk.Button(text='Add', width=10, style="elder.TButton", command=call_add)
add_button.grid(column=0, row=3)

update_button = ttk.Button(text='Update', width=10, style="elder.TButton", command=call_update)
update_button.grid(column=1, row=3)

delete_button = ttk.Button(text='Delete', width=10, style="elder.TButton", command=call_delete)
delete_button.grid(column=2, row=3)

# Start the Tkinter main loop to display the GUI
window.mainloop()
