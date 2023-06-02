N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_routes_output.txt', 'w') as f:
	f.write('')

### Append first line to output
with open('fortigate_csv_to_routes_output.txt', 'a') as f:
    f.write('config router static' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_routes_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # dst
        col1 = values[1].replace(N, '') # gateway
        col2 = values[2].replace(N, '') # device
        col3 = values[3].replace(N, '') # distance
        col4 = values[4].replace(N, '') # priority
        col5 = values[5].replace(N, '') # comment
        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_routes_output.txt', 'a') as f:
                f.write('edit 0' + N)
                f.write('set dst ' + Q + col0 + Q + N)
                f.write('set gateway ' + Q + col1 + Q + N)
                f.write('set device ' + Q + col2 + Q + N)
                f.write('set distance ' + Q + col3 + Q + N)
                f.write('set priority ' + Q + col4 + Q + N)
                f.write('set comment ' + Q + col5 + Q + N)
                f.write('next' + N)     
        row = row + 1       

### Append and 'end' to the output
with open('fortigate_csv_to_routes_output.txt', 'a') as f:
    f.write('end' + N)
