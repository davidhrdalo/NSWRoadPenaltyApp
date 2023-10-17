import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


#get today's date
dt = date.today()

#date in (Year, month , day)
#first date input
startDate = date(2012, 1, 1)  #select minimum date
#second date input
endDate = date(2017, 11, 1)  #selects maximum date


class NSWRoadPenaltyApp(tk.Tk):
    # Main application class for NSWRoadPenaltyApp.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a container frame
        container = tk.Frame(self)

        # Set the initial window dimensions
        self.geometry("995x600")

        # Pack the container to fill the entire window
        container.pack(side="top", fill="both", expand=True)

        # Configure rows and columns for resizing
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    # Create empty dictionary
        self.frames = {}

        # Initialize frames for different pages
        for F in (homePage, TaskOne, TaskTwo, TaskThree, TaskFour, TaskFive):
            frame = F(container, self)
            self.frames[F] = frame
            #make grid stick to all sides of frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame (homePage)
        self.show_frame(homePage)

    def show_frame(self, cont):
        # Show the specified frame.
        # Args:
        #     container (class): The class of the frame to be shown.
        frame = self.frames[cont]
        frame.tkraise()



class homePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        """""""""
        TITLES
        """""""""

        #Create main title
        label = tk.Label(self, text="NSW Traffic Insight System")
        label.place(x=120, y=60)
        label.config(font=("Verdana", 35, "bold"))

        label = tk.Label(self, text="2810ICT Software Technologies Part 2: Isaac Wright, Mitchell Howard and David Hrdalo")
        label.place(x=50, y=135)
        label.config(font=("Verdana", 15))

        """""""""
        NAV BUTTONS
        """""""""

        # Function to change button background color to white on hover
        def on_enter(event):
            event.widget.configure(bg="white")
            event.widget.configure(fg="black")

        # Function to change button background color back to its original color when the mouse leaves
        def on_leave(event):
            event.widget.configure(bg=button_color)
            event.widget.configure(fg=button_label_color)

        #Style the buttons blue
        button_color = "#21315B"
        button_label_color = "white"

        button1 = tk.Button(self, width=27, height=3,
                            text="Information on All Penalty Cases", fg=button_label_color, bg=button_color, command=lambda: controller.show_frame(TaskOne))
        button1.grid(row=0, column=0)
        button2 = tk.Button(self, width=27, height=3,
                            text="Offence Code Analysis", fg=button_label_color,  bg=button_color, command=lambda: controller.show_frame(TaskTwo))
        button2.grid(row=0, column=1)
        button3 = tk.Button(self, width=27, height=3,
                            text="Camera and Radar Analysis", fg=button_label_color,  bg=button_color, command=lambda: controller.show_frame(TaskThree))
        button3.grid(row=0, column=2)
        button4 = tk.Button(self, width=27, height=3,
                            text="Mobile Phone Incident Analysis", fg=button_label_color, bg=button_color, command=lambda: controller.show_frame(TaskFour))
        button4.grid(row=0, column=3)
        button5 = tk.Button(self, width=27, height=3,
                            text="Location Analysis", fg=button_label_color, bg=button_color, command=lambda: controller.show_frame(TaskFive))
        button5.grid(row=0, column=4)


        # Bind events for mouse hovering and not hovering anymore
        button1.bind("<Enter>", on_enter)
        button1.bind("<Leave>", on_leave)

        button2.bind("<Enter>", on_enter)
        button2.bind("<Leave>", on_leave)

        button3.bind("<Enter>", on_enter)
        button3.bind("<Leave>", on_leave)

        button4.bind("<Enter>", on_enter)
        button4.bind("<Leave>", on_leave)

        button5.bind("<Enter>", on_enter)
        button5.bind("<Leave>", on_leave)


        """""""""
        IMAGE
        """""""""

        # Open the image and resize it to the desired dimensions
        original_image = Image.open("nsw_logo.png")
        resized_image = original_image.resize((778, 296), Image.LANCZOS)

        # Convert the resized image to a tkinter PhotoImage
        nsw_resized_logo = ImageTk.PhotoImage(resized_image)
        logoLabel = tk.Label(self, image=nsw_resized_logo)
        logoLabel.place(x=120, y=220)
        logoLabel.image = nsw_resized_logo


class TaskOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        """""""""
        STYLES
        """""""""
        #Style the buttons blue and text white
        button_color = "#21315b"
        button_label_color = "white"

        """""""""
        HEADING
        """""""""

        label = tk.Label(self, text="Information on All Penalty Cases")
        label.place(x=300, y=20)
        label.config(font=("Verdana", 20, "bold", "underline"))

        """""""""
        BACK BTN
        """""""""
        #Add back button
        backButton = tk.Button(self, width=12, height=2, text="Back Home", fg=button_label_color, bg=button_color, command=lambda: controller.show_frame(homePage))
        backButton.place(x=20, y=30)

        """""""""
        DATE SELECT
        """""""""
        selectDateLabel = tk.Label(self, text="Please select a" + "\n" "period to" + "\n" + "view data from:")
        selectDateLabel.place(x=20, y=135)

        # Create Calendars for start and end date period
        #Format is in YYYY/MM/DD Format
        self.task1_Start_Calendar = DateEntry(self, selectmode='day', mindate=startDate, maxdate=endDate)
        self.task1_Start_Calendar.set_date(date(2012, 1, 1))
        self.task1_Start_Calendar.place(x=15, y=195)

        label1 = tk.Label(self, text="to")
        label1.place(x=55, y=220)

        self.task1_End_Calendar = DateEntry(self, selectmode='day', mindate=startDate, maxdate=endDate)
        self.task1_End_Calendar.set_date(date(2017, 11, 1))
        self.task1_End_Calendar.place(x=15, y=245)

        #Submit Button
        submitButton = tk.Button(self, width=10, height=2, text="Submit", fg=button_label_color, bg=button_color, command=self.display_filtered_data)
        submitButton.place(x=22, y=280)

    def task1Function(self, start_date, end_date):
        # Check dates
        start_date = pd.to_datetime(start_date, format="%d/%m/%Y")
        end_date = pd.to_datetime(end_date, format="%d/%m/%Y")

        penalty_df = pd.read_csv("penalty_data_set_2.csv", parse_dates=["OFFENCE_MONTH"], dayfirst=True, low_memory=False)

        # Filter the data
        mask = (penalty_df['OFFENCE_MONTH'] >= start_date) & (penalty_df['OFFENCE_MONTH'] <= end_date)
        filtered_df = penalty_df.loc[mask]

        return filtered_df  # Return the filtered DataFrame

    def display_filtered_data(self):
        input_date1 = self.task1_Start_Calendar.get_date().strftime("%d/%m/%Y")
        input_date2 = self.task1_End_Calendar.get_date().strftime("%d/%m/%Y")

        filtered_df = self.task1Function(input_date1, input_date2)

        # Create a new frame for the table
        table_frame = tk.Frame(self)
        table_frame.place(x=200, y=100, height=400, width=700)  # Adjust x, y, height, and width as needed

        # Create Treeview to display data
        tv = ttk.Treeview(table_frame)
        tv['columns'] = list(filtered_df.columns)
        tv['show'] = 'headings'

        for column in filtered_df.columns:
            tv.heading(column, text=column)
            tv.column(column, width=100)

        # Load data into Treeview
        for index, row in filtered_df.iterrows():
            tv.insert('', 'end', values=row.tolist())

        tv.pack(fill='both', expand=True)

        # Add scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tv.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tv.xview)
        tv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')


class TaskTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        """""""""
        STYLES
        """""""""
        #Style the buttons blue and text white
        button_color = "#21315B"
        button_label_color = "white"

        """""""""
        HEADING
        """""""""

        label = tk.Label(self, text="Offence Code Analysis")
        label.place(x=375, y=20)
        label.config(font=("Verdana", 20, "bold", "underline"))

        """""""""
        BACK BTN
        """""""""
        #Add back button
        backButton = tk.Button(self, width=12, height=2, text="Back Home", fg=button_label_color, bg=button_color, command=lambda: controller.show_frame(homePage))
        backButton.place(x=20, y=30)

        """""""""
        DATE SELECT
        """""""""
        selectDateLabel = tk.Label(self, text="Please select a" + "\n" "period to" + "\n" + "view data from:")
        selectDateLabel.place(x=20, y=135)

        # Create Calendars for start and end date period
        #Format is in YYYY/MM/DD Format
        task2_Start_Calendar = DateEntry(self, selectmode='day', mindate=startDate, maxdate=endDate)
        task2_Start_Calendar.set_date(date(2012, 1, 1))
        task2_Start_Calendar.place(x=15, y=195)

        label1 = tk.Label(self, text="to")
        label1.place(x=55, y=220)

        task2_End_Calendar = DateEntry(self, selectmode='day', mindate=startDate, maxdate=endDate)
        task2_End_Calendar.set_date(date(2017, 11, 1))
        task2_End_Calendar.place(x=15, y=245)

        #Submit Button
        submitButton = tk.Button(self, width=10, height=2, text="Submit", fg=button_label_color, bg=button_color, command=lambda: generate_chart())
        submitButton.place(x=22, y=280)

        #Import and read dataset converting the datetime
        df = pd.read_csv("penalty_data_set_2.csv", dtype='unicode', usecols=['OFFENCE_CODE', 'OFFENCE_MONTH'])
        df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'])

        #function to chart chart and draw it on the page
        def generate_chart():

            #Create colors array for chart
            colors = [
                "#FF5733", "#33FF57", "#5533FF", "#FFD700", "#FF33CC",
                "#33FFFF", "#FF5733", "#3399FF", "#FF7F50", "#00CED1",
                "#8A2BE2", "#D2691E", "#20B2AA", "#FF8C00", "#DDA0DD",
                "#FF4500", "#1E90FF", "#87CEEB", "#6A5ACD", "#FF1493"
            ]

            """""""""
            FORMAT DATE INPUTS
            """""""""
            # get the date values from the selection
            sDate = task2_Start_Calendar.get_date().strftime("%Y/%m/%d")
            eDate = task2_End_Calendar.get_date().strftime("%Y/%m/%d")

            df = pd.read_csv("penalty_data_set_2.csv", dtype="unicode")
            df = df.astype(str)
            df["OFFENCE_MONTH"] = pd.to_datetime(df["OFFENCE_MONTH"], format="%d/%m/%Y")

            # Sort by date start - end
            mask = (df['OFFENCE_MONTH'] > sDate) & (df['OFFENCE_MONTH'] <= eDate)
            result = df.loc[mask]

            # Take top 15
            x = result["OFFENCE_CODE"].value_counts()[:15]
            offenceCodeOutput = dict(x)


            """""""""
            CREATE PIE CHART
            """""""""
            # Create a figure and subplot for the pie chart
            f = Figure(figsize=(6,6), dpi=100)
            ax = f.add_subplot(111)

            # Create a list of labels and a list of corresponding values
            labels = list(offenceCodeOutput.keys())
            values = list(offenceCodeOutput.values())

            # Create a pie chart
            ax.pie(
                values,
                autopct='%.1f%%',
                pctdistance=0.85,
                textprops={'fontsize': 7},
                colors=colors,
                startangle=90,
            )
            ax.legend(labels)

            # Create a canvas to display the pie chart
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().place(x=230, y=80)

            # Set chart title
            f.suptitle("Top 15 Most Frequent Offences Based on Offence Code" + "\n" + "Between " + sDate + " to " + eDate, fontsize=11, color='purple')

class TaskThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Styles for buttons: blue background and white text
        button_color = "#21315B"
        button_label_color = "white"

        # Heading label for the page
        label = tk.Label(self, text="Camera and Radar Analysis")
        label.place(x=365, y=20)
        label.config(font=("Verdana", 20, "bold", "underline"))

        # Back button to return to the home page
        backButton = tk.Button(self, width=12, height=2, text="Back Home", fg=button_label_color, bg=button_color,
        command=lambda: controller.show_frame(homePage))
        backButton.place(x=20, y=30)

        # Date selection section
        selectDateLabel = tk.Label(self, text="Please select a period to view data from:")
        selectDateLabel.place(x=20, y=135)

        # Instance attributes for date pickers
        self.task3_Start_Calendar = DateEntry(self, selectmode='day', mindate=startDate, maxdate=endDate)
        self.task3_Start_Calendar.set_date(date(2012, 1, 1))
        self.task3_Start_Calendar.place(x=15, y=195)

        label1 = tk.Label(self, text="to")
        label1.place(x=55, y=220)

        self.task3_End_Calendar = DateEntry(self, selectmode='day', mindate=startDate, maxdate=endDate)
        self.task3_End_Calendar.set_date(date(2017, 11, 1))
        self.task3_End_Calendar.place(x=15, y=245)

        # Submit button to initiate data processing
        submitButton = tk.Button(self, width=10, height=2, text="Submit", fg=button_label_color, bg=button_color,
        command=self.display_filtered_data)
        submitButton.place(x=22, y=280)

    def task3Function(self, start_date, end_date):
        # Ensure the dates are in datetime format
        start_date = pd.to_datetime(start_date, format="%d/%m/%Y")
        end_date = pd.to_datetime(end_date, format="%d/%m/%Y")

        penalty_df = pd.read_csv("penalty_data_set_2.csv", parse_dates=["OFFENCE_MONTH"], dayfirst=True, low_memory=False)


        # Filter the data based on date range and offense type (e.g., "Camera" or "Radar")
        mask = (penalty_df['OFFENCE_MONTH'] >= start_date) & (penalty_df['OFFENCE_MONTH'] <= end_date) & \
               (penalty_df['OFFENCE_DESC'].str.contains('radar|camera detected', case=False, na=False))

        filtered_df = penalty_df.loc[mask]

        return filtered_df  # Return the filtered DataFrame
    def display_filtered_data(self):
        input_date1 = self.task3_Start_Calendar.get_date().strftime("%d/%m/%Y")
        input_date2 = self.task3_End_Calendar.get_date().strftime("%d/%m/%Y")

        filtered_df = self.task3Function(input_date1, input_date2)

        # Create a new frame for the table
        table_frame = tk.Frame(self)
        table_frame.place(x=200, y=100, height=400, width=700)  # Adjust x, y, height, and width as needed

        # Create Treeview to display data
        tv = ttk.Treeview(table_frame)
        tv['columns'] = list(filtered_df.columns)
        tv['show'] = 'headings'

        for column in filtered_df.columns:
            tv.heading(column, text=column)
            tv.column(column, width=100)

        # Load data into Treeview
        for index, row in filtered_df.iterrows():
            tv.insert('', 'end', values=row.tolist())

        tv.pack(fill='both', expand=True)

        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tv.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tv.xview)
        tv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side='right', fill='y')
        hsb.pack(side='bottom', fill='x')

class TaskFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        """""""""
        STYLES
        """""""""
        #Style the buttons blue and text white
        button_color = "#21315B"
        button_label_color = "white"

        """""""""
        HEADING
        """""""""

        label = tk.Label(self, text="Mobile Phone Incident Analysis")
        label.place(x=350, y=20)
        label.config(font=("Verdana", 20, "bold", "underline"))

        """""""""
        BACK BTN
        """""""""
        #Add back button
        backButton = tk.Button(self, width=12, height=2, text="Back Home", fg=button_label_color, bg=button_color, command=lambda: controller.show_frame(homePage))
        backButton.place(x=20, y=30)

        """""""""
        CHART BTNs
        """""""""
        buttonChart1 = tk.Button(self, width=19, height=4, text="Trend Over Time",  fg=button_label_color, bg=button_color, command=lambda: getChartTrendline())
        buttonChart1.place(x=20, y=240)

        buttonChart2 = tk.Button(self, width=19, height=4, text="Top Offence Codes",  fg=button_label_color, bg=button_color, command=lambda: getCharTopOffence())
        buttonChart2.place(x=20, y=330)

        frame = pd.read_csv("penalty_data_set_2.csv", dtype="unicode")
        #
        # def filterMobileCase(df,b):
        #     # Filter where it only selects mobile phone incidents
        #     a = df[(df.MOBILE_PHONE_IND == b)]
        #     return a

        def filterMobileCase(df, b):
            # Filter where it only selects mobile phone incidents
            a = df[(df.MOBILE_PHONE_IND == b)]
            return a
        #Call the function to get the refined mobile offences
        data = frame.astype(str)
        filter = "Y"
        df = filterMobileCase(data, filter)
        # print(df)

        """""""""
        Trend over Time
        """""""""
        # Data source years and initial empty year_dict
        data_source_years = ["2012", "2013", "2014", "2015", "2016", "2017"]
        year_dict = {}

        """""""""
        Top Offence Codes
        """""""""

        # Calculate the number of offenses for each year in data source years
        for year in data_source_years:
            year_count = df['OFFENCE_MONTH'].str.contains(year).sum()
            year_dict[year] = year_count

        # Find the top 15 most common offense codes
        top_offense_codes = df["OFFENCE_CODE"].value_counts().nlargest(15)

        # Create a dictionary with the 15 most common offense codes and their counts
        offenceDict = dict(top_offense_codes)



        # Create colors array for chart
        colors = [
            "#FF5733", "#33FF57", "#5533FF", "#FFD700", "#FF33CC",
            "#33FFFF", "#FF5733", "#3399FF", "#FF7F50", "#00CED1",
            "#8A2BE2", "#D2691E", "#20B2AA", "#FF8C00", "#DDA0DD",
            "#FF4500", "#1E90FF", "#87CEEB", "#6A5ACD", "#FF1493"
        ]
        def getCharTopOffence():
            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(7, 5), dpi=100)

            # Create a bar plot using data from 'offenceDict' and custom colors
            offence_codes, amounts = zip(*offenceDict.items())
            ax.bar(offence_codes, amounts, color=colors)

            # Customize the appearance of the plot
            ax.grid(axis='y', linestyle='--', alpha=0.6)

            # Set y-label, x-label, and title
            ax.set_title("Top 15 Offence Codes With Incidents Involving\nMobile Phones", color='purple')
            ax.set_ylabel('Total Amount of Offences', fontsize=12, color='purple')
            ax.set_xlabel('Offence Code', fontsize=12, color='purple')

            # Create a canvas and draw the plot
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.draw()
            # Place the canvas in the tkinter window
            canvas.get_tk_widget().place(x=220, y=72)


        def getChartTrendline():
            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(7, 5), dpi=100)

            # Plot the data
            years, values = zip(*year_dict.items())
            years = [int(year) for year in years]
            line, = ax.plot(years, values, label='Offence Data', color='orange', marker='x')

            # Customize the appearance of the plot
            # ax.fill_between(years, lower_boundary_values, values, alpha=0.5, color='orange')
            ax.grid(True, linestyle='--', alpha=0.6)

            # Set y-label, x-label, and title
            ax.set_title("Dataset Trend Over Time for Offences Involving Incidents For\nMobile Phone Use",
            color='purple')
            ax.set_ylabel('Amount of Offences', fontsize=12, color='purple')
            ax.set_xlabel('Year', fontsize=12, color='purple')

            # Create a canvas and draw the plot
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.draw()
            # Place the canvas in the tkinter window
            canvas.get_tk_widget().place(x=220, y=72)

class TaskFiveLogic:
    def __init__(self, data_source="penalty_data_set_2.csv"):
        self.data_source = data_source

    def get_location_dict(self):
        """Return a location dictionary of top 3 locations"""
        return {
            9623: 'HINTERLAND WAY EWINGSDALE',
            9648: 'PACIFIC HIGHWAY WOODBURN',
            9636: 'NEW ENGLAND HIGHWAY LOCHINVAR',
        }

    def load_data(self):
        """Load data from the CSV file and filter out anomalies."""
        penalty_df = pd.read_csv(self.data_source, parse_dates=["OFFENCE_MONTH"], dayfirst=True, low_memory=False)

        # Filter out any rows with OFFENCE_MONTH in the year 1971 (or any other known anomalies)
        penalty_df = penalty_df[penalty_df['OFFENCE_MONTH'].dt.year != 1971]

        return penalty_df

    def filter_data_by_date(self, start_date, end_date):
        """Filter the data based on the provided start and end dates."""
        penalty_df = self.load_data()

        # Ensure the dates are in datetime format
        start_date = pd.to_datetime(start_date, format="%d/%m/%Y")
        end_date = pd.to_datetime(end_date, format="%d/%m/%Y")

        # Filter the data between start_date and end_date
        mask = (penalty_df['OFFENCE_MONTH'] >= start_date) & (penalty_df['OFFENCE_MONTH'] <= end_date)
        filtered_df = penalty_df.loc[mask]
        return filtered_df


class TaskFive(tk.Frame):
    def __init__(self, parent, controller, data_source="penalty_data_set_2.csv"):
        tk.Frame.__init__(self, parent)
        self.logic = TaskFiveLogic(data_source)
        self.controller = controller
        self.initialize_ui()

    def initialize_ui(self):

        """""""""
        STYLES
        """""""""
        button_color = "#21315b"
        button_label_color = "white"

        """""""""
        HEADING
        """""""""
        label = tk.Label(self, text="Location Analysis")
        label.place(x=375, y=20)
        label.config(font=("Verdana", 20, "bold", "underline"))

        """""""""
        BACK BTN
        """""""""
        backButton = tk.Button(self, width=12, height=2, text="Back Home", fg=button_label_color, bg=button_color,
                               command=lambda: self.controller.show_frame(homePage))
        backButton.place(x=20, y=30)

        """""""""
        DATE SELECT
        """""""""
        selectDateLabel = tk.Label(self, text="Please select a" + "\n" "period to" + "\n" + "view data from:")
        selectDateLabel.place(x=20, y=135)

        # Create Calendars for start and end date period
        self.task5_Start_Calendar = DateEntry(self, selectmode='day', mindate=date(2012, 1, 1),
                                              maxdate=date(2017, 11, 1))
        self.task5_Start_Calendar.set_date(date(2012, 1, 1))
        self.task5_Start_Calendar.place(x=15, y=195)

        label1 = tk.Label(self, text="to")
        label1.place(x=55, y=220)

        self.task5_End_Calendar = DateEntry(self, selectmode='day', mindate=date(2012, 1, 1), maxdate=date(2017, 11, 1))
        self.task5_End_Calendar.set_date(date(2017, 11, 1))
        self.task5_End_Calendar.place(x=15, y=245)

        # Submit Button
        submitButton = tk.Button(self, width=10, height=2, text="Submit", fg="white", bg="#21315b",
                                 command=lambda: self.plot_location_trend(
                                     self.task5_Start_Calendar.get_date().strftime("%d/%m/%Y"),
                                     self.task5_End_Calendar.get_date().strftime("%d/%m/%Y"),
                                 ))
        submitButton.place(x=22, y=280)

    def plot_location_trend(self, start_date, end_date):
        """Plot the location trend based on the filtered data."""
        filtered_df = self.logic.filter_data_by_date(start_date, end_date)

        # Ensure the OFFENCE_MONTH column is in datetime format
        filtered_df['OFFENCE_MONTH'] = pd.to_datetime(filtered_df['OFFENCE_MONTH'])

        # Filter the data to only include the specified location codes
        location_dict = self.logic.get_location_dict()
        filtered_df = filtered_df[filtered_df['LOCATION_CODE'].isin(location_dict.keys())]

        # Group and sum the data by location and date
        grouped_df = filtered_df.groupby(['LOCATION_CODE', 'OFFENCE_MONTH']).size().reset_index(name='CASE_COUNT')

        # Pivot the data to get locations as columns and dates as the index
        pivot_df = grouped_df.pivot(index='OFFENCE_MONTH', columns='LOCATION_CODE', values='CASE_COUNT').fillna(0)
        plt.figure()

        # Plot the data
        ax = pivot_df.plot(kind='line', figsize=(8, 5))

        # x-axis settings
        ax.set_xlim(pd.to_datetime(start_date, format="%d/%m/%Y"), pd.to_datetime(end_date, format="%d/%m/%Y"))
        ax.set_xlabel("Date")
        ax.set_ylabel("Case Count")

        # Set title with the date range using f-string
        ax.set_title(f"Case Location Trend from {start_date} to {end_date}")

        # Adjusted legend positioning and size
        labels = [location_dict[code] for code in pivot_df.columns]
        ax.legend(labels, title='Location', bbox_to_anchor=(1.01, 1), loc='upper left', fontsize='x-small',
                  title_fontsize='x-small', borderaxespad=0.)

        # Adjust right margin to make space for the legend
        plt.subplots_adjust(right=0.7)

        # Display the plot
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=150, y=80)
        canvas.draw()


root = NSWRoadPenaltyApp()
root.title("NSW Road Penalty App")

root.mainloop()