N = ('\n') # newline
Q = ('"')  # double quote
row = 0    # row

### Create a empty output txt file
with open('fortigate_csv_to_services_output.txt', 'w') as f:
	f.write('')

### Append first line to output
with open('fortigate_csv_to_services_output.txt', 'a') as f:
    f.write('config firewall service custom' + N)

### Read input CSV and assign each column to a variable
with open('fortigate_csv_to_services_input.csv', 'r') as f:
    for line in f:
        values = line.split(';')        
        
        # Add comment to each column
        # Must be in format col0, col1, col2, etc.
        
        col0 = values[0].replace(N, '') # service
        col1 = values[1].replace(N, '') # protocol
        col2 = values[2].replace(N, '') # startport
        col3 = values[3].replace(N, '') # endport
        col4 = values[4].replace(N, '') # comment

        
        # First line is not added to the output
        if row >= 1:    
            with open('fortigate_csv_to_services_output.txt', 'a') as f:
                f.write('edit ' + Q + col0 + Q + N)
                f.write('set ' + col1 + '-portrange ' + col2 + '-' + col3 + N)
                f.write('set comment ' + Q + col4 + Q + N)
                f.write('next' + N)     
        row = row + 1

### Append and 'end' to the output
with open('fortigate_csv_to_services_output.txt', 'a') as f:
    f.write('end' + N)