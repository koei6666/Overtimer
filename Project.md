# Overtimer

## Feature
1. Get the clock in time, get the clock out time
    - How to get the clock in time?
        How to:Make the program start as the system and record the timestamp when user login(When the program is started)
    - How to get the clock out time?
        :Make the program always running background and record the timestamp when its closed
    Module:Use datetime module to get the timestamp when program is started.
    Structure: 
        **Class**:Time
            attribute:start_time,end_time
            method: timestamp:to get the timestamp of certain event and return
2. Calculate the delta between 2 time and give the working time(overtime) back
3. Display the current overtime in the system tray(windows)
4. Calculate the compensation based on the overtime data collected
*Addtional*
1. Allow user to set overtime limit, when reached or passed, change the color of the icon to notify