import time

def stopwatch():
    try:
        print("Stopwatch started.")  # Print a message indicating that the stopwatch has started
        start_time = time.time()  # Get the current time
        while True:  # Loop indefinitely
            current_time = time.time()  # Get the current time
            elapsed_time = current_time - start_time  # Calculate the elapsed time
            # Format the elapsed time as HH:MM:SS
            hours, rem = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(rem, 60)
            elapsed_time_str = f"{int(hours):02d}:{int(minutes):02d}:{seconds:.2f}"
            print(f"\r{elapsed_time_str}", end="")  # Print the elapsed time,
            time.sleep(0.1)  # Wait for 0.1 seconds
    except KeyboardInterrupt:
        # If the user presses Ctrl+C, print a message and exit the function
        print("\nStopwatch stopped.")
        return

stopwatch()  # Call the stopwatch function to start the stopwatch
